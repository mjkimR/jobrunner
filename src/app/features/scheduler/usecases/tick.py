"""Tick use case - executes due rules.

Called by POST /api/v1/tick endpoint or internal scheduler.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from app_base.core.log import logger
from sqlalchemy.ext.asyncio import AsyncSession

# Import scripts package to auto-register all rule handlers
import scripts  # noqa: F401
from app.features.scheduler.callbacks import CallbackContext, create_callback_handler
from app.features.scheduler.executor import RuleExecutor
from app.features.scheduler.schedule import calculate_next_run
from app.features.scheduler.schemas import TickResponse
from app.features.scheduler.services import SchedulerService

# Default scripts directory (relative to project root)
DEFAULT_SCRIPTS_PATH = Path(__file__).parents[4] / "scripts"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class TickUseCase:
    """Run due rules once.

    - Called by: POST /api/v1/tick, internal scheduler, cronjob worker
    - Owns orchestration (not HTTP concerns)
    """

    session: AsyncSession
    scripts_path: Path | None = None

    async def execute(
        self, now: datetime | None = None, limit: int = 100
    ) -> TickResponse:
        now = now or _utcnow()
        svc = SchedulerService(session=self.session)
        executor = RuleExecutor(
            scripts_base_path=self.scripts_path or DEFAULT_SCRIPTS_PATH
        )

        due_rules = await svc.list_due_rules(now=now, limit=limit)
        logger.info(f"Found {len(due_rules)} due rules to execute")

        processed = 0
        succeeded = 0
        failed = 0
        execution_ids: list[str] = []

        for rule in due_rules:
            processed += 1
            execution = await svc.start_execution(rule_id=rule.id, executed_at=now)
            execution_ids.append(str(execution.id))

            # Execute the rule script
            result = await executor.execute(
                script_path=rule.execution_script_path,
                payload=rule.payload,
            )

            # Build callback context
            callback_context = CallbackContext(
                rule_name=rule.name,
                rule_id=str(rule.id),
                execution_id=str(execution.id),
                success=result.success,
                message=result.message,
                data=result.data,
                payload=rule.payload,
            )

            if result.success:
                await svc.finish_execution_success(
                    execution_id=execution.id,
                    log_summary=result.message or "Executed successfully",
                )
                succeeded += 1
                logger.info(f"Rule '{rule.name}' succeeded: {result.message}")

                # Execute on_success callback
                await self._execute_callback(rule.on_success, callback_context)
            else:
                await svc.finish_execution_failure(
                    execution_id=execution.id,
                    log_summary=result.error or result.message or "Execution failed",
                )
                failed += 1
                logger.warning(f"Rule '{rule.name}' failed: {result.error}")

                # Execute on_failure callback
                await self._execute_callback(rule.on_failure, callback_context)

            # Update next_run_at based on schedule
            try:
                next_run = calculate_next_run(rule.schedule, now)
                await svc.update_next_run_at(rule.id, next_run)
                logger.debug(f"Rule '{rule.name}' next run: {next_run}")
            except ValueError as e:
                logger.error(f"Invalid cron for rule '{rule.name}': {e}")

        await self.session.commit()

        return TickResponse(
            processed=processed,
            succeeded=succeeded,
            failed=failed,
            execution_ids=execution_ids,
        )

    async def _execute_callback(
        self,
        callback_config: dict | None,
        context: CallbackContext,
    ) -> None:
        """Execute a callback if configured."""
        if not callback_config:
            return

        handler = create_callback_handler(callback_config)
        if handler:
            try:
                await handler.execute(context)
            except Exception as e:
                logger.error(f"Callback execution failed: {e}")
