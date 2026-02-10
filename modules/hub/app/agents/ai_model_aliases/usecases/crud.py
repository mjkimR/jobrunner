from typing import Annotated

from app.agents.ai_model_aliases.models import AIModelAlias
from app.agents.ai_model_aliases.schemas import AIModelAliasCreate, AIModelAliasUpdate
from app.agents.ai_model_aliases.services import AIModelAliasContextKwargs, AIModelAliasService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAIModelAliasUseCase(BaseGetUseCase[AIModelAliasService, AIModelAlias, AIModelAliasContextKwargs]):
    def __init__(self, service: Annotated[AIModelAliasService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAIModelAliasUseCase(BaseGetMultiUseCase[AIModelAliasService, AIModelAlias, AIModelAliasContextKwargs]):
    def __init__(self, service: Annotated[AIModelAliasService, Depends()]) -> None:
        super().__init__(service)


class CreateAIModelAliasUseCase(
    BaseCreateUseCase[AIModelAliasService, AIModelAlias, AIModelAliasCreate, AIModelAliasContextKwargs]
):
    def __init__(self, service: Annotated[AIModelAliasService, Depends()]) -> None:
        super().__init__(service)


class UpdateAIModelAliasUseCase(
    BaseUpdateUseCase[AIModelAliasService, AIModelAlias, AIModelAliasUpdate, AIModelAliasContextKwargs]
):
    def __init__(self, service: Annotated[AIModelAliasService, Depends()]) -> None:
        super().__init__(service)


class DeleteAIModelAliasUseCase(BaseDeleteUseCase[AIModelAliasService, AIModelAlias, AIModelAliasContextKwargs]):
    def __init__(self, service: Annotated[AIModelAliasService, Depends()]) -> None:
        super().__init__(service)
