import uuid
from typing import Annotated

from app.gateways.conversations.schemas import ConversationCreate, ConversationRead, ConversationUpdate
from app.gateways.conversations.usecases.crud import (
    CreateConversationUseCase,
    DeleteConversationUseCase,
    GetConversationUseCase,
    GetMultiConversationUseCase,
    UpdateConversationUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/conversations", tags=["Conversation"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ConversationRead)
async def create_conversation(
    use_case: Annotated[CreateConversationUseCase, Depends()],
    conversation_in: ConversationCreate,
):
    return await use_case.execute(conversation_in)


@router.get("", response_model=PaginatedList[ConversationRead])
async def get_conversations(
    use_case: Annotated[GetMultiConversationUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{conversation_id}", response_model=ConversationRead)
async def get_conversation(
    use_case: Annotated[GetConversationUseCase, Depends()],
    conversation_id: uuid.UUID,
):
    conversation = await use_case.execute(conversation_id)
    if not conversation:
        raise NotFoundException()
    return conversation


@router.put("/{conversation_id}", response_model=ConversationRead)
async def update_conversation(
    use_case: Annotated[UpdateConversationUseCase, Depends()],
    conversation_id: uuid.UUID,
    conversation_in: ConversationUpdate,
):
    conversation = await use_case.execute(conversation_id, conversation_in)
    if not conversation:
        raise NotFoundException()
    return conversation


@router.delete("/{conversation_id}", response_model=DeleteResponse)
async def delete_conversation(
    use_case: Annotated[DeleteConversationUseCase, Depends()],
    conversation_id: uuid.UUID,
):
    return await use_case.execute(conversation_id)
