from typing import Annotated

from app.agents.agent_executions.models import AgentExecution
from app.agents.agent_executions.schemas import AgentExecutionCreate, AgentExecutionUpdate
from app.agents.agent_executions.services import AgentExecutionService, BaseContextKwargs
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAgentExecutionUseCase(BaseGetUseCase[AgentExecutionService, AgentExecution, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentExecutionService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAgentExecutionUseCase(BaseGetMultiUseCase[AgentExecutionService, AgentExecution, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentExecutionService, Depends()]) -> None:
        super().__init__(service)


class CreateAgentExecutionUseCase(
    BaseCreateUseCase[AgentExecutionService, AgentExecution, AgentExecutionCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[AgentExecutionService, Depends()]) -> None:
        super().__init__(service)


class UpdateAgentExecutionUseCase(
    BaseUpdateUseCase[AgentExecutionService, AgentExecution, AgentExecutionUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[AgentExecutionService, Depends()]) -> None:
        super().__init__(service)


class DeleteAgentExecutionUseCase(BaseDeleteUseCase[AgentExecutionService, AgentExecution, BaseContextKwargs]):
    def __init__(self, service: Annotated[AgentExecutionService, Depends()]) -> None:
        super().__init__(service)
