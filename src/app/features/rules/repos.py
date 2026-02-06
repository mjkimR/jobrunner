from datetime import datetime

from sqlalchemy import Select, select

from app_base.base.repos.base import BaseRepository
from app.features.rules.models import Rule
from app.features.rules.schemas import RuleCreate, RuleUpdate


class RuleRepository(BaseRepository[Rule, RuleCreate, RuleUpdate]):
    model = Rule

    def _base_due_stmt(self, now: datetime) -> Select:
        return (
            select(Rule)
            .where(Rule.is_active.is_(True))
            .where(Rule.next_run_at <= now)
            .order_by(Rule.next_run_at.asc())
        )

    async def list_due(self, now: datetime, limit: int = 100) -> list[Rule]:
        stmt = self._base_due_stmt(now).limit(limit)
        res = await self.session.execute(stmt)
        return list(res.scalars().all())
