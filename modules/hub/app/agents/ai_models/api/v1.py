import uuid
from typing import Annotated

from app.agents.ai_models.schemas import AIModelCreate, AIModelRead, AIModelUpdate
from app.agents.ai_models.usecases.crud import (
    CreateAIModelUseCase,
    DeleteAIModelUseCase,
    GetAIModelUseCase,
    GetMultiAIModelUseCase,
    UpdateAIModelUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/ai_models", tags=["AIModel"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AIModelRead)
async def create_ai_model(
    use_case: Annotated[CreateAIModelUseCase, Depends()],
    ai_model_in: AIModelCreate,
):
    return await use_case.execute(ai_model_in)


@router.get("", response_model=PaginatedList[AIModelRead])
async def get_ai_models(
    use_case: Annotated[GetMultiAIModelUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{ai_model_id}", response_model=AIModelRead)
async def get_ai_model(
    use_case: Annotated[GetAIModelUseCase, Depends()],
    ai_model_id: uuid.UUID,
):
    ai_model = await use_case.execute(ai_model_id)
    if not ai_model:
        raise NotFoundException()
    return ai_model


@router.put("/{ai_model_id}", response_model=AIModelRead)
async def update_ai_model(
    use_case: Annotated[UpdateAIModelUseCase, Depends()],
    ai_model_id: uuid.UUID,
    ai_model_in: AIModelUpdate,
):
    ai_model = await use_case.execute(ai_model_id, ai_model_in)
    if not ai_model:
        raise NotFoundException()
    return ai_model


@router.delete("/{ai_model_id}", response_model=DeleteResponse)
async def delete_ai_model(
    use_case: Annotated[DeleteAIModelUseCase, Depends()],
    ai_model_id: uuid.UUID,
):
    return await use_case.execute(ai_model_id)
