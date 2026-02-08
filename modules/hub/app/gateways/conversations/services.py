from typing import Annotated

from app.gateways.conversations.models import Conversation
from app.gateways.conversations.repos import ConversationRepository
from app.gateways.conversations.schemas import ConversationCreate, ConversationUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class ConversationService(
    BaseCreateServiceMixin[ConversationRepository, Conversation, ConversationCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[ConversationRepository, Conversation, BaseContextKwargs],
    BaseGetServiceMixin[ConversationRepository, Conversation, BaseContextKwargs],
    BaseUpdateServiceMixin[ConversationRepository, Conversation, ConversationUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[ConversationRepository, Conversation, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[ConversationRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> ConversationRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
