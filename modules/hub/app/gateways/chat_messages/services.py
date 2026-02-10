from typing import Annotated

from app.gateways.chat_messages.models import ChatMessage
from app.gateways.chat_messages.repos import ChatMessageRepository
from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class ChatMessageService(
    BaseCreateServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[ChatMessageRepository, ChatMessage, BaseContextKwargs],
    BaseGetServiceMixin[ChatMessageRepository, ChatMessage, BaseContextKwargs],
    BaseUpdateServiceMixin[ChatMessageRepository, ChatMessage, ChatMessageUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[ChatMessageRepository, ChatMessage, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[ChatMessageRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> ChatMessageRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
