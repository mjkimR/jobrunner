from typing import Annotated

from app.gateways.chat_messages.models import ChatMessage
from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageUpdate
from app.gateways.chat_messages.services import ChatMessageContextKwargs, ChatMessageService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetChatMessageUseCase(BaseGetUseCase[ChatMessageService, ChatMessage, ChatMessageContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class GetMultiChatMessageUseCase(BaseGetMultiUseCase[ChatMessageService, ChatMessage, ChatMessageContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class CreateChatMessageUseCase(
    BaseCreateUseCase[ChatMessageService, ChatMessage, ChatMessageCreate, ChatMessageContextKwargs]
):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class UpdateChatMessageUseCase(
    BaseUpdateUseCase[ChatMessageService, ChatMessage, ChatMessageUpdate, ChatMessageContextKwargs]
):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)


class DeleteChatMessageUseCase(BaseDeleteUseCase[ChatMessageService, ChatMessage, ChatMessageContextKwargs]):
    def __init__(self, service: Annotated[ChatMessageService, Depends()]) -> None:
        super().__init__(service)
