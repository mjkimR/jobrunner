from typing import Annotated, Optional
from uuid import UUID

from app.agents.agent_mcps.filters import filter_ids as mcp_filter_ids
from app.agents.agent_mcps.services import AgentMCPService
from app.agents.agent_skills.filters import filter_ids as skill_filter_ids
from app.agents.agent_skills.services import AgentSkillService
from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentUpdate
from app.agents.configured_agents.services import ConfiguredAgentContextKwargs, ConfiguredAgentService
from app_base.base.deps.filters.resolver import resolve_filter
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class GetConfiguredAgentUseCase(BaseGetUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentContextKwargs]):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class GetMultiConfiguredAgentUseCase(
    BaseGetMultiUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentContextKwargs]
):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class CreateConfiguredAgentUseCase(
    BaseCreateUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentCreate, ConfiguredAgentContextKwargs]
):
    def __init__(
        self,
        service: Annotated[ConfiguredAgentService, Depends()],
        service_skill: Annotated[AgentSkillService, Depends()],
        service_mcp: Annotated[AgentMCPService, Depends()],
    ) -> None:
        super().__init__(service)
        self.service_skill = service_skill
        self.service_mcp = service_mcp

    async def _execute(
        self,
        session: AsyncSession,
        obj_data: ConfiguredAgentCreate,
        context: Optional[ConfiguredAgentContextKwargs],
    ) -> ConfiguredAgent:
        update_fields = {}
        if obj_data.mcp_ids:
            mcps = await self.service_mcp.get_multi(
                session, limit=None, where=resolve_filter(mcp_filter_ids, obj_data.mcp_ids)
            )
            if len(mcps.items) != len(obj_data.mcp_ids):
                raise ValueError("One or more AgentMCP IDs are invalid.")
            update_fields["mcps"] = mcps.items

        if obj_data.skill_ids:
            skills = await self.service_skill.get_multi(
                session, limit=None, where=resolve_filter(skill_filter_ids, obj_data.skill_ids)
            )
            if len(skills.items) != len(obj_data.skill_ids):
                raise ValueError("One or more AgentSkill IDs are invalid.")
            update_fields["skills"] = skills.items

        return await self.service.create(session, obj_data, context, **update_fields)


class UpdateConfiguredAgentUseCase(
    BaseUpdateUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentUpdate, ConfiguredAgentContextKwargs]
):
    def __init__(
        self,
        service: Annotated[ConfiguredAgentService, Depends()],
        service_skill: Annotated[AgentSkillService, Depends()],
        service_mcp: Annotated[AgentMCPService, Depends()],
    ) -> None:
        super().__init__(service)
        self.service_skill = service_skill
        self.service_mcp = service_mcp

    async def _execute(
        self,
        session: AsyncSession,
        object_id: UUID,
        obj_data: ConfiguredAgentUpdate,
        context: Optional[ConfiguredAgentContextKwargs],
    ) -> ConfiguredAgent:
        update_fields = {}
        if obj_data.mcp_ids:
            mcps = await self.service_mcp.get_multi(
                session, limit=None, where=resolve_filter(mcp_filter_ids, obj_data.mcp_ids)
            )
            if len(mcps.items) != len(obj_data.mcp_ids):
                raise ValueError("One or more AgentMCP IDs are invalid.")
            update_fields["mcps"] = mcps.items

        if obj_data.skill_ids:
            skills = await self.service_skill.get_multi(
                session, limit=None, where=resolve_filter(skill_filter_ids, obj_data.skill_ids)
            )
            if len(skills.items) != len(obj_data.skill_ids):
                raise ValueError("One or more AgentSkill IDs are invalid.")
            update_fields["skills"] = skills.items
        return await self.service.update(session, object_id, obj_data, context, **update_fields)


class DeleteConfiguredAgentUseCase(
    BaseDeleteUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentContextKwargs]
):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)
