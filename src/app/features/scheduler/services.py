import uuid
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.features.rule_executions.models import RuleExecutionStatus
from app.features.rule_executions.repos import RuleExecutionRepository
from app.features.rule_executions.schemas import (
    RuleExecutionCreate,
    RuleExecutionUpdate,
)
from app.features.rules.repos import RuleRepository
from app.features.rules.schemas import RuleUpdate


@dataclass
class SchedulerService:
    """Application service used by TickUseCase.

    We keep DB access encapsulated here so orchestration stays in the usecase.
    """

    session: AsyncSession

    async def list_due_rules(self, now: datetime, limit: int = 100):
        repo = RuleRepository(self.session)
        return await repo.list_due(now=now, limit=limit)

    async def start_execution(self, rule_id: uuid.UUID, executed_at: datetime):
        repo = RuleExecutionRepository(self.session)
        obj_in = RuleExecutionCreate(
            rule_id=rule_id,
            status=RuleExecutionStatus.running,
            executed_at=executed_at,
        )
        return await repo.create(obj_in=obj_in)

    async def finish_execution_success(
        self, execution_id: uuid.UUID, log_summary: str | None = None
    ):
        repo = RuleExecutionRepository(self.session)
        obj_in = RuleExecutionUpdate(
            status=RuleExecutionStatus.success,
            log_summary=log_summary,
        )
        return await repo.update(id=execution_id, obj_in=obj_in)

    async def finish_execution_failure(
        self, execution_id: uuid.UUID, log_summary: str | None = None
    ):
        repo = RuleExecutionRepository(self.session)
        obj_in = RuleExecutionUpdate(
            status=RuleExecutionStatus.failure,
            log_summary=log_summary,
        )
        return await repo.update(id=execution_id, obj_in=obj_in)

    async def update_next_run_at(self, rule_id: uuid.UUID, next_run_at: datetime):
        """Update the next_run_at field for a rule after execution."""
        repo = RuleRepository(self.session)
        obj_in = RuleUpdate(next_run_at=next_run_at)
        return await repo.update(id=rule_id, obj_in=obj_in)
