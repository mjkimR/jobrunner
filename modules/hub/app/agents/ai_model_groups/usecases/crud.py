from typing import Annotated

from app.agents.ai_model_groups.models import AIModelGroup
from app.agents.ai_model_groups.schemas import AIModelGroupCreate, AIModelGroupUpdate
from app.agents.ai_model_groups.services import AIModelGroupContextKwargs, AIModelGroupService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetAIModelGroupUseCase(BaseGetUseCase[AIModelGroupService, AIModelGroup, AIModelGroupContextKwargs]):
    def __init__(self, service: Annotated[AIModelGroupService, Depends()]) -> None:
        super().__init__(service)


class GetMultiAIModelGroupUseCase(BaseGetMultiUseCase[AIModelGroupService, AIModelGroup, AIModelGroupContextKwargs]):
    def __init__(self, service: Annotated[AIModelGroupService, Depends()]) -> None:
        super().__init__(service)


class CreateAIModelGroupUseCase(
    BaseCreateUseCase[AIModelGroupService, AIModelGroup, AIModelGroupCreate, AIModelGroupContextKwargs]
):
    def __init__(self, service: Annotated[AIModelGroupService, Depends()]) -> None:
        super().__init__(service)


class UpdateAIModelGroupUseCase(
    BaseUpdateUseCase[AIModelGroupService, AIModelGroup, AIModelGroupUpdate, AIModelGroupContextKwargs]
):
    def __init__(self, service: Annotated[AIModelGroupService, Depends()]) -> None:
        super().__init__(service)


class DeleteAIModelGroupUseCase(BaseDeleteUseCase[AIModelGroupService, AIModelGroup, AIModelGroupContextKwargs]):
    def __init__(self, service: Annotated[AIModelGroupService, Depends()]) -> None:
        super().__init__(service)
