from typing import Annotated

from app.agents.agent_mcps.models import AgentMCP
from app.agents.agent_mcps.schemas import AgentMCPCreate, AgentMCPUpdate
from app.agents.agent_mcps.services import AgentMCPService, BaseContextKwargs
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAgentMCPUseCase(BaseGetUseCase[AgentMCPService, AgentMCP, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentMCPService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAgentMCPUseCase(BaseGetMultiUseCase[AgentMCPService, AgentMCP, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentMCPService, Depends()]) -> None:
        super().__init__(service)


class CreateAgentMCPUseCase(BaseCreateUseCase[AgentMCPService, AgentMCP, AgentMCPCreate, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentMCPService, Depends()]) -> None:
        super().__init__(service)


class UpdateAgentMCPUseCase(BaseUpdateUseCase[AgentMCPService, AgentMCP, AgentMCPUpdate, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentMCPService, Depends()]) -> None:
        super().__init__(service)


class DeleteAgentMCPUseCase(BaseDeleteUseCase[AgentMCPService, AgentMCP, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentMCPService, Depends()]) -> None:
        super().__init__(service)
