from typing import Annotated
from uuid import UUID

from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageRead, ChatMessageUpdate
from app.gateways.chat_messages.services import ChatMessageContextKwargs
from app.gateways.chat_messages.usecases.crud import (
    CreateChatMessageUseCase,
    DeleteChatMessageUseCase,
    GetChatMessageUseCase,
    GetMultiChatMessageUseCase,
    UpdateChatMessageUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(
    prefix="/workspaces/{workspace_id}/conversations/{conversation_id}/chat_messages",
    tags=["ChatMessage"],
    dependencies=[],
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ChatMessageRead)
async def create_chat_message(
    conversation_id: UUID,
    use_case: Annotated[CreateChatMessageUseCase, Depends()],
    chat_message_in: ChatMessageCreate,
):
    context: ChatMessageContextKwargs = {"parent_id": conversation_id}
    return await use_case.execute(chat_message_in, context=context)


@router.get("", response_model=PaginatedList[ChatMessageRead])
async def get_chat_messages(
    conversation_id: UUID,
    use_case: Annotated[GetMultiChatMessageUseCase, Depends()],
    pagination: PaginationParam,
):
    context: ChatMessageContextKwargs = {"parent_id": conversation_id}
    return await use_case.execute(**pagination, context=context)


@router.get("/{chat_message_id}", response_model=ChatMessageRead)
async def get_chat_message(
    conversation_id: UUID,
    use_case: Annotated[GetChatMessageUseCase, Depends()],
    chat_message_id: UUID,
):
    context: ChatMessageContextKwargs = {"parent_id": conversation_id}
    chat_message = await use_case.execute(chat_message_id, context=context)
    if not chat_message:
        raise NotFoundException()
    return chat_message


@router.put("/{chat_message_id}", response_model=ChatMessageRead)
async def update_chat_message(
    conversation_id: UUID,
    use_case: Annotated[UpdateChatMessageUseCase, Depends()],
    chat_message_id: UUID,
    chat_message_in: ChatMessageUpdate,
):
    context: ChatMessageContextKwargs = {"parent_id": conversation_id}
    chat_message = await use_case.execute(chat_message_id, chat_message_in, context=context)
    if not chat_message:
        raise NotFoundException()
    return chat_message


@router.delete("/{chat_message_id}", response_model=DeleteResponse)
async def delete_chat_message(
    conversation_id: UUID,
    use_case: Annotated[DeleteChatMessageUseCase, Depends()],
    chat_message_id: UUID,
):
    context: ChatMessageContextKwargs = {"parent_id": conversation_id}
    return await use_case.execute(chat_message_id, context=context)
