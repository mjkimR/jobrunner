import uuid

from sqlalchemy import select

from app_base.base.repos.base import BaseRepository
from app.features.rule_executions.models import RuleExecution
from app.features.rule_executions.schemas import (
    RuleExecutionCreate,
    RuleExecutionUpdate,
)


class RuleExecutionRepository(
    BaseRepository[RuleExecution, RuleExecutionCreate, RuleExecutionUpdate]
):
    model = RuleExecution

    async def list_by_rule_id(
        self, rule_id: uuid.UUID, limit: int = 100
    ) -> list[RuleExecution]:
        stmt = (
            select(RuleExecution)
            .where(RuleExecution.rule_id == rule_id)
            .order_by(RuleExecution.executed_at.desc())
            .limit(limit)
        )
        res = await self.session.execute(stmt)
        return list(res.scalars().all())

    async def get_latest_for_rule(self, rule_id: uuid.UUID) -> RuleExecution | None:
        stmt = (
            select(RuleExecution)
            .where(RuleExecution.rule_id == rule_id)
            .order_by(RuleExecution.executed_at.desc())
            .limit(1)
        )
        res = await self.session.execute(stmt)
        return res.scalars().first()
