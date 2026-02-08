from typing import Annotated

from app.gateways.conversations.models import Conversation
from app.gateways.conversations.schemas import ConversationCreate, ConversationUpdate
from app.gateways.conversations.services import BaseContextKwargs, ConversationService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetConversationUseCase(BaseGetUseCase[ConversationService, Conversation, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConversationService, Depends()]) -> None:
        super().__init__(service)


class GetMultiConversationUseCase(BaseGetMultiUseCase[ConversationService, Conversation, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConversationService, Depends()]) -> None:
        super().__init__(service)


class CreateConversationUseCase(
    BaseCreateUseCase[ConversationService, Conversation, ConversationCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ConversationService, Depends()]) -> None:
        super().__init__(service)


class UpdateConversationUseCase(
    BaseUpdateUseCase[ConversationService, Conversation, ConversationUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ConversationService, Depends()]) -> None:
        super().__init__(service)


class DeleteConversationUseCase(BaseDeleteUseCase[ConversationService, Conversation, BaseContextKwargs]):
    def __init__(self, service: Annotated[ConversationService, Depends()]) -> None:
        super().__init__(service)
