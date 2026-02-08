from typing import Annotated

from app.agents.agent_executions.models import AgentExecution
from app.agents.agent_executions.repos import AgentExecutionRepository
from app.agents.agent_executions.schemas import AgentExecutionCreate, AgentExecutionUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AgentExecutionService(
    BaseCreateServiceMixin[AgentExecutionRepository, AgentExecution, AgentExecutionCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[AgentExecutionRepository, AgentExecution, BaseContextKwargs],
    BaseGetServiceMixin[AgentExecutionRepository, AgentExecution, BaseContextKwargs],
    BaseUpdateServiceMixin[AgentExecutionRepository, AgentExecution, AgentExecutionUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[AgentExecutionRepository, AgentExecution, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[AgentExecutionRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AgentExecutionRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
