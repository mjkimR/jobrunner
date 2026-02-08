from typing import Annotated

from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentUpdate
from app.agents.configured_agents.services import BaseContextKwargs, ConfiguredAgentService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetConfiguredAgentUseCase(BaseGetUseCase[ConfiguredAgentService, ConfiguredAgent, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class GetMultiConfiguredAgentUseCase(BaseGetMultiUseCase[ConfiguredAgentService, ConfiguredAgent, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class CreateConfiguredAgentUseCase(
    BaseCreateUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class UpdateConfiguredAgentUseCase(
    BaseUpdateUseCase[ConfiguredAgentService, ConfiguredAgent, ConfiguredAgentUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)


class DeleteConfiguredAgentUseCase(BaseDeleteUseCase[ConfiguredAgentService, ConfiguredAgent, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConfiguredAgentService, Depends()]) -> None:
        super().__init__(service)
