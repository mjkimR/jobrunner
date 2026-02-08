from typing import Annotated

from app.gateways.user_messages.models import UserMessage
from app.gateways.user_messages.schemas import UserMessageCreate, UserMessageUpdate
from app.gateways.user_messages.services import BaseContextKwargs, UserMessageService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetUserMessageUseCase(BaseGetUseCase[UserMessageService, UserMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[UserMessageService, Depends()]) -> None:
        super().__init__(service)


class GetMultiUserMessageUseCase(BaseGetMultiUseCase[UserMessageService, UserMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[UserMessageService, Depends()]) -> None:
        super().__init__(service)


class CreateUserMessageUseCase(
    BaseCreateUseCase[UserMessageService, UserMessage, UserMessageCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[UserMessageService, Depends()]) -> None:
        super().__init__(service)


class UpdateUserMessageUseCase(
    BaseUpdateUseCase[UserMessageService, UserMessage, UserMessageUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[UserMessageService, Depends()]) -> None:
        super().__init__(service)


class DeleteUserMessageUseCase(BaseDeleteUseCase[UserMessageService, UserMessage, BaseContextKwargs]):
    def __init__(self, service: Annotated[UserMessageService, Depends()]) -> None:
        super().__init__(service)
