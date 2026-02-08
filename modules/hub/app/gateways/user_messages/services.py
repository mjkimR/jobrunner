from typing import Annotated

from app.gateways.user_messages.models import UserMessage
from app.gateways.user_messages.repos import UserMessageRepository
from app.gateways.user_messages.schemas import UserMessageCreate, UserMessageUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class UserMessageService(
    BaseCreateServiceMixin[UserMessageRepository, UserMessage, UserMessageCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[UserMessageRepository, UserMessage, BaseContextKwargs],
    BaseGetServiceMixin[UserMessageRepository, UserMessage, BaseContextKwargs],
    BaseUpdateServiceMixin[UserMessageRepository, UserMessage, UserMessageUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[UserMessageRepository, UserMessage, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[UserMessageRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> UserMessageRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
