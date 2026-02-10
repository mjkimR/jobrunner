from typing import Annotated

from app.gateways.chat_messages.models import ChatMessage
from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageUpdate
from app.gateways.chat_messages.services import BaseContextKwargs, ChatMessageService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetChatMessageUseCase(BaseGetUseCase[ChatMessageService, ChatMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class GetMultiChatMessageUseCase(BaseGetMultiUseCase[ChatMessageService, ChatMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class CreateChatMessageUseCase(
    BaseCreateUseCase[ChatMessageService, ChatMessage, ChatMessageCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class UpdateChatMessageUseCase(
    BaseUpdateUseCase[ChatMessageService, ChatMessage, ChatMessageUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class DeleteChatMessageUseCase(BaseDeleteUseCase[ChatMessageService, ChatMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)
