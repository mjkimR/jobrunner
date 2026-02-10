from typing import Annotated
from uuid import UUID

from app.agents.ai_model_groups.schemas import AIModelGroupCreate, AIModelGroupRead, AIModelGroupUpdate
from app.agents.ai_model_groups.usecases.crud import (
    CreateAIModelGroupUseCase,
    DeleteAIModelGroupUseCase,
    GetAIModelGroupUseCase,
    GetMultiAIModelGroupUseCase,
    UpdateAIModelGroupUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/ai_model_groups", tags=["AIModelGroup"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AIModelGroupRead)
async def create_ai_model_group(
    use_case: Annotated[CreateAIModelGroupUseCase, Depends()],
    ai_model_group_in: AIModelGroupCreate,
):
    return await use_case.execute(ai_model_group_in)


@router.get("", response_model=PaginatedList[AIModelGroupRead])
async def get_ai_model_groups(
    use_case: Annotated[GetMultiAIModelGroupUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{ai_model_group_id}", response_model=AIModelGroupRead)
async def get_ai_model_group(
    use_case: Annotated[GetAIModelGroupUseCase, Depends()],
    ai_model_group_id: UUID,
):
    ai_model_group = await use_case.execute(ai_model_group_id)
    if not ai_model_group:
        raise NotFoundException()
    return ai_model_group


@router.put("/{ai_model_group_id}", response_model=AIModelGroupRead)
async def update_ai_model_group(
    use_case: Annotated[UpdateAIModelGroupUseCase, Depends()],
    ai_model_group_id: UUID,
    ai_model_group_in: AIModelGroupUpdate,
):
    ai_model_group = await use_case.execute(ai_model_group_id, ai_model_group_in)
    if not ai_model_group:
        raise NotFoundException()
    return ai_model_group


@router.delete("/{ai_model_group_id}", response_model=DeleteResponse)
async def delete_ai_model_group(
    use_case: Annotated[DeleteAIModelGroupUseCase, Depends()],
    ai_model_group_id: UUID,
):
    return await use_case.execute(ai_model_group_id)
