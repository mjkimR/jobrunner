from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.features.scheduler.schemas import TickResponse
from app.features.scheduler.services import SchedulerService


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class TickUseCase:
    """Run due rules once.

    - Called by: POST /api/v1/tick, internal scheduler, cronjob worker
    - Owns orchestration (not HTTP concerns)
    """

    session: AsyncSession

    async def execute(
        self, now: datetime | None = None, limit: int = 100
    ) -> TickResponse:
        now = now or _utcnow()
        svc = SchedulerService(session=self.session)

        due_rules = await svc.list_due_rules(now=now, limit=limit)

        processed = 0
        succeeded = 0
        failed = 0
        execution_ids: list[str] = []

        for rule in due_rules:
            processed += 1
            execution = await svc.start_execution(rule_id=rule.id, executed_at=now)
            execution_ids.append(str(execution.id))

            # TODO: 실제 룰 실행기(스크립트 실행/아티팩트 업로드/콜백)
            try:
                await svc.finish_execution_success(
                    execution_id=execution.id, log_summary="tick skeleton: executed"
                )
                succeeded += 1
            except Exception:
                failed += 1
                await svc.finish_execution_failure(
                    execution_id=execution.id, log_summary="tick skeleton: failed"
                )

        await self.session.commit()

        return TickResponse(
            processed=processed,
            succeeded=succeeded,
            failed=failed,
            execution_ids=execution_ids,
        )
