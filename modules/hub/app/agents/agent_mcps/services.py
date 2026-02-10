from typing import Annotated

from app.agents.agent_mcps.models import AgentMCP
from app.agents.agent_mcps.repos import AgentMCPRepository
from app.agents.agent_mcps.schemas import AgentMCPCreate, AgentMCPUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AgentMCPContextKwargs(BaseContextKwargs):
    pass


class AgentMCPService(
    BaseCreateServiceMixin[AgentMCPRepository, AgentMCP, AgentMCPCreate, AgentMCPContextKwargs],
    BaseGetMultiServiceMixin[AgentMCPRepository, AgentMCP, AgentMCPContextKwargs],
    BaseGetServiceMixin[AgentMCPRepository, AgentMCP, AgentMCPContextKwargs],
    BaseUpdateServiceMixin[AgentMCPRepository, AgentMCP, AgentMCPUpdate, AgentMCPContextKwargs],
    BaseDeleteServiceMixin[AgentMCPRepository, AgentMCP, AgentMCPContextKwargs],
):
    def __init__(self, repo: Annotated[AgentMCPRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AgentMCPRepository:
        return self._repo

    @property
    def context_model(self):
        return AgentMCPContextKwargs
