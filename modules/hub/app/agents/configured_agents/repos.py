from typing import Any

from app.agents.agent_mcps.models import AgentMCP
from app.agents.agent_skills.models import AgentSkill
from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentUpdate
from app_base.base.repos.base import BaseRepository
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ConfiguredAgentRepository(BaseRepository[ConfiguredAgent, ConfiguredAgentCreate, ConfiguredAgentUpdate]):
    model = ConfiguredAgent

    async def create(
        self, session: AsyncSession, obj_in: ConfiguredAgentCreate | dict[str, Any], **kwargs
    ) -> ConfiguredAgent:
        obj_in_data = jsonable_encoder(obj_in)
        skill_ids = obj_in_data.pop("skill_ids", None)
        mcp_ids = obj_in_data.pop("mcp_ids", None)

        db_obj = self.model(**obj_in_data)

        if skill_ids is not None:
            stmt = select(AgentSkill).where(AgentSkill.id.in_(skill_ids))
            result = await session.execute(stmt)
            db_obj.skills = list(result.scalars().all())

        if mcp_ids is not None:
            stmt = select(AgentMCP).where(AgentMCP.id.in_(mcp_ids))
            result = await session.execute(stmt)
            db_obj.mcps = list(result.scalars().all())

        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        session: AsyncSession,
        db_obj: ConfiguredAgent,
        obj_in: ConfiguredAgentUpdate | dict[str, Any],
        **kwargs,
    ) -> ConfiguredAgent:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        skill_ids = update_data.pop("skill_ids", None)
        mcp_ids = update_data.pop("mcp_ids", None)

        # Handle relationships
        if skill_ids is not None:
            stmt = select(AgentSkill).where(AgentSkill.id.in_(skill_ids))
            result = await session.execute(stmt)
            db_obj.skills = list(result.scalars().all())

        if mcp_ids is not None:
            stmt = select(AgentMCP).where(AgentMCP.id.in_(mcp_ids))
            result = await session.execute(stmt)
            db_obj.mcps = list(result.scalars().all())

        # Update other fields
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj
