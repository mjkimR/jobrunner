from typing import Annotated

from app.gateways.routing_logs.models import RoutingLog
from app.gateways.routing_logs.schemas import RoutingLogCreate, RoutingLogUpdate
from app.gateways.routing_logs.services import BaseContextKwargs, RoutingLogService
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from fastapi import Depends


class GetRoutingLogUseCase(BaseGetUseCase[RoutingLogService, RoutingLog, BaseContextKwargs]):
    def __init__(self, service: Annotated[RoutingLogService, Depends()]) -> None:
        super().__init__(service)


class GetMultiRoutingLogUseCase(BaseGetMultiUseCase[RoutingLogService, RoutingLog, BaseContextKwargs]):
    def __init__(self, service: Annotated[RoutingLogService, Depends()]) -> None:
        super().__init__(service)


class CreateRoutingLogUseCase(BaseCreateUseCase[RoutingLogService, RoutingLog, RoutingLogCreate, BaseContextKwargs]):
    def __init__(self, service: Annotated[RoutingLogService, Depends()]) -> None:
        super().__init__(service)


class UpdateRoutingLogUseCase(BaseUpdateUseCase[RoutingLogService, RoutingLog, RoutingLogUpdate, BaseContextKwargs]):
    def __init__(self, service: Annotated[RoutingLogService, Depends()]) -> None:
        super().__init__(service)


class DeleteRoutingLogUseCase(BaseDeleteUseCase[RoutingLogService, RoutingLog, BaseContextKwargs]):
    def __init__(self, service: Annotated[RoutingLogService, Depends()]) -> None:
        super().__init__(service)
