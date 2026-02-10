from typing import Annotated

from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.repos import ConfiguredAgentRepository
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class ConfiguredAgentContextKwargs(BaseContextKwargs):
    pass


class ConfiguredAgentService(
    BaseCreateServiceMixin[
        ConfiguredAgentRepository, ConfiguredAgent, ConfiguredAgentCreate, ConfiguredAgentContextKwargs
    ],
    BaseGetMultiServiceMixin[ConfiguredAgentRepository, ConfiguredAgent, ConfiguredAgentContextKwargs],
    BaseGetServiceMixin[ConfiguredAgentRepository, ConfiguredAgent, ConfiguredAgentContextKwargs],
    BaseUpdateServiceMixin[
        ConfiguredAgentRepository, ConfiguredAgent, ConfiguredAgentUpdate, ConfiguredAgentContextKwargs
    ],
    BaseDeleteServiceMixin[ConfiguredAgentRepository, ConfiguredAgent, ConfiguredAgentContextKwargs],
):
    def __init__(self, repo: Annotated[ConfiguredAgentRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> ConfiguredAgentRepository:
        return self._repo

    @property
    def context_model(self):
        return ConfiguredAgentContextKwargs
