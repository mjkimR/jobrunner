from typing import Annotated
from uuid import UUID

from app.gateways.conversations.schemas import ConversationCreate, ConversationRead, ConversationUpdate
from app.gateways.conversations.services import ConversationContextKwargs
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

router = APIRouter(prefix="/workspaces/{workspace_id}/conversations", tags=["Conversation"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ConversationRead)
async def create_conversation(
    workspace_id: UUID,
    use_case: Annotated[CreateConversationUseCase, Depends()],
    conversation_in: ConversationCreate,
):
    context: ConversationContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(conversation_in, context=context)


@router.get("", response_model=PaginatedList[ConversationRead])
async def get_conversations(
    workspace_id: UUID,
    use_case: Annotated[GetMultiConversationUseCase, Depends()],
    pagination: PaginationParam,
):
    context: ConversationContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(**pagination, context=context)


@router.get("/{conversation_id}", response_model=ConversationRead)
async def get_conversation(
    workspace_id: UUID,
    use_case: Annotated[GetConversationUseCase, Depends()],
    conversation_id: UUID,
):
    context: ConversationContextKwargs = {"parent_id": workspace_id}
    conversation = await use_case.execute(conversation_id, context=context)
    if not conversation:
        raise NotFoundException()
    return conversation


@router.put("/{conversation_id}", response_model=ConversationRead)
async def update_conversation(
    workspace_id: UUID,
    use_case: Annotated[UpdateConversationUseCase, Depends()],
    conversation_id: UUID,
    conversation_in: ConversationUpdate,
):
    context: ConversationContextKwargs = {"parent_id": workspace_id}
    conversation = await use_case.execute(conversation_id, conversation_in, context=context)
    if not conversation:
        raise NotFoundException()
    return conversation


@router.delete("/{conversation_id}", response_model=DeleteResponse)
async def delete_conversation(
    workspace_id: UUID,
    use_case: Annotated[DeleteConversationUseCase, Depends()],
    conversation_id: UUID,
):
    context: ConversationContextKwargs = {"parent_id": workspace_id}
    return await use_case.execute(conversation_id, context=context)
