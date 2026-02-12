from typing import Annotated

from app.gateways.chat_messages.models import ChatMessage
from app.gateways.chat_messages.repos import ChatMessageRepository
from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageUpdate
from app.gateways.conversations.repos import ConversationRepository
from app_base.base.services.base import (
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app_base.base.services.nested_resource_hook import NestedResourceContextKwargs, NestedResourceHooksMixin
from fastapi import Depends


class ChatMessageContextKwargs(NestedResourceContextKwargs):
    pass


class ChatMessageService(
    NestedResourceHooksMixin,  # Relationship with Conversation
    BaseCreateServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageCreate, ChatMessageContextKwargs],
    BaseGetMultiServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageContextKwargs],
    BaseGetServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageContextKwargs],
    BaseUpdateServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageUpdate, ChatMessageContextKwargs],
    BaseDeleteServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageContextKwargs],
):
    def __init__(
        self,
        repo: Annotated[ChatMessageRepository, Depends()],
        repo_conversation: Annotated[ConversationRepository, Depends()],
    ):
        self._repo = repo
        self._parent_repo = repo_conversation

    @property
    def repo(self) -> ChatMessageRepository:
        return self._repo

    @property
    def parent_repo(self) -> ConversationRepository:
        return self._parent_repo

    @property
    def context_model(self):
        return ChatMessageContextKwargs

    @property
    def fk_name(self) -> str:
        return "conversation_id"
