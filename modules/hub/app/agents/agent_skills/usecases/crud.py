from typing import Annotated

from app.agents.agent_skills.models import AgentSkill
from app.agents.agent_skills.schemas import AgentSkillCreate, AgentSkillUpdate
from app.agents.agent_skills.services import AgentSkillContextKwargs, AgentSkillService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAgentSkillUseCase(BaseGetUseCase[AgentSkillService, AgentSkill, AgentSkillContextKwargs]):
    def __init__(self, service: Annotated[AgentSkillService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAgentSkillUseCase(BaseGetMultiUseCase[AgentSkillService, AgentSkill, AgentSkillContextKwargs]):
    def __init__(self, service: Annotated[AgentSkillService, Depends()]) -> None:
        super().__init__(service)


class CreateAgentSkillUseCase(
    BaseCreateUseCase[AgentSkillService, AgentSkill, AgentSkillCreate, AgentSkillContextKwargs]
):
    def __init__(self, service: Annotated[AgentSkillService, Depends()]) -> None:
        super().__init__(service)


class UpdateAgentSkillUseCase(
    BaseUpdateUseCase[AgentSkillService, AgentSkill, AgentSkillUpdate, AgentSkillContextKwargs]
):
    def __init__(self, service: Annotated[AgentSkillService, Depends()]) -> None:
        super().__init__(service)


class DeleteAgentSkillUseCase(BaseDeleteUseCase[AgentSkillService, AgentSkill, AgentSkillContextKwargs]):
    def __init__(self, service: Annotated[AgentSkillService, Depends()]) -> None:
        super().__init__(service)
