import uuid
from typing import Annotated

from app.agents.ai_model_aliases.schemas import AIModelAliasCreate, AIModelAliasRead, AIModelAliasUpdate
from app.agents.ai_model_aliases.usecases.crud import (
    CreateAIModelAliasUseCase,
    DeleteAIModelAliasUseCase,
    GetAIModelAliasUseCase,
    GetMultiAIModelAliasUseCase,
    UpdateAIModelAliasUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/ai_model_aliases", tags=["AIModelAliass"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AIModelAliasRead)
async def create_ai_model_alias(
    use_case: Annotated[CreateAIModelAliasUseCase, Depends()],
    ai_model_alias_in: AIModelAliasCreate,
):
    return await use_case.execute(ai_model_alias_in)


@router.get("", response_model=PaginatedList[AIModelAliasRead])
async def get_ai_model_aliases(
    use_case: Annotated[GetMultiAIModelAliasUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{ai_model_alias_id}", response_model=AIModelAliasRead)
async def get_ai_model_alias(
    use_case: Annotated[GetAIModelAliasUseCase, Depends()],
    ai_model_alias_id: uuid.UUID,
):
    ai_model_alias = await use_case.execute(ai_model_alias_id)
    if not ai_model_alias:
        raise NotFoundException()
    return ai_model_alias


@router.put("/{ai_model_alias_id}", response_model=AIModelAliasRead)
async def update_ai_model_alias(
    use_case: Annotated[UpdateAIModelAliasUseCase, Depends()],
    ai_model_alias_id: uuid.UUID,
    ai_model_alias_in: AIModelAliasUpdate,
):
    ai_model_alias = await use_case.execute(ai_model_alias_id, ai_model_alias_in)
    if not ai_model_alias:
        raise NotFoundException()
    return ai_model_alias


@router.delete("/{ai_model_alias_id}", response_model=DeleteResponse)
async def delete_ai_model_alias(
    use_case: Annotated[DeleteAIModelAliasUseCase, Depends()],
    ai_model_alias_id: uuid.UUID,
):
    return await use_case.execute(ai_model_alias_id)
