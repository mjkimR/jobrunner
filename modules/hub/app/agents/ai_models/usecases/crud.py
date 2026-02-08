from typing import Annotated

from app.agents.ai_models.models import AIModel
from app.agents.ai_models.schemas import AIModelCreate, AIModelUpdate
from app.agents.ai_models.services import AIModelService, BaseContextKwargs
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAIModelUseCase(BaseGetUseCase[AIModelService, AIModel, BaseContextKwargs]):
    def __init__(self, service: Annotated[AIModelService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAIModelUseCase(BaseGetMultiUseCase[AIModelService, AIModel, BaseContextKwargs]):
    def __init__(self, service: Annotated[AIModelService, Depends()]) -> None:
        super().__init__(service)


class CreateAIModelUseCase(BaseCreateUseCase[AIModelService, AIModel, AIModelCreate, BaseContextKwargs]):
    def __init__(self, service: Annotated[AIModelService, Depends()]) -> None:
        super().__init__(service)


class UpdateAIModelUseCase(BaseUpdateUseCase[AIModelService, AIModel, AIModelUpdate, BaseContextKwargs]):
    def __init__(self, service: Annotated[AIModelService, Depends()]) -> None:
        super().__init__(service)


class DeleteAIModelUseCase(BaseDeleteUseCase[AIModelService, AIModel, BaseContextKwargs]):
    def __init__(self, service: Annotated[AIModelService, Depends()]) -> None:
        super().__init__(service)
