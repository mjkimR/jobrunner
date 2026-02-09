import uuid
from typing import Annotated

from app.gateways.user_messages.schemas import UserMessageCreate, UserMessageRead, UserMessageUpdate
from app.gateways.user_messages.usecases.crud import (
    CreateUserMessageUseCase,
    DeleteUserMessageUseCase,
    GetMultiUserMessageUseCase,
    GetUserMessageUseCase,
    UpdateUserMessageUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/user_messages", tags=["UserMessage"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserMessageRead)
async def create_user_message(
    use_case: Annotated[CreateUserMessageUseCase, Depends()],
    user_message_in: UserMessageCreate,
):
    return await use_case.execute(user_message_in)


@router.get("", response_model=PaginatedList[UserMessageRead])
async def get_user_messages(
    use_case: Annotated[GetMultiUserMessageUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{user_message_id}", response_model=UserMessageRead)
async def get_user_message(
    use_case: Annotated[GetUserMessageUseCase, Depends()],
    user_message_id: uuid.UUID,
):
    user_message = await use_case.execute(user_message_id)
    if not user_message:
        raise NotFoundException()
    return user_message


@router.put("/{user_message_id}", response_model=UserMessageRead)
async def update_user_message(
    use_case: Annotated[UpdateUserMessageUseCase, Depends()],
    user_message_id: uuid.UUID,
    user_message_in: UserMessageUpdate,
):
    user_message = await use_case.execute(user_message_id, user_message_in)
    if not user_message:
        raise NotFoundException()
    return user_message


@router.delete("/{user_message_id}", response_model=DeleteResponse)
async def delete_user_message(
    use_case: Annotated[DeleteUserMessageUseCase, Depends()],
    user_message_id: uuid.UUID,
):
    return await use_case.execute(user_message_id)
