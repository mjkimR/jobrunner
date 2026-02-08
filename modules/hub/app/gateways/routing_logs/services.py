from typing import Annotated

from app.gateways.routing_logs.models import RoutingLog
from app.gateways.routing_logs.repos import RoutingLogRepository
from app.gateways.routing_logs.schemas import RoutingLogCreate, RoutingLogUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class RoutingLogService(
    BaseCreateServiceMixin[RoutingLogRepository, RoutingLog, RoutingLogCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[RoutingLogRepository, RoutingLog, BaseContextKwargs],
    BaseGetServiceMixin[RoutingLogRepository, RoutingLog, BaseContextKwargs],
    BaseUpdateServiceMixin[RoutingLogRepository, RoutingLog, RoutingLogUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[RoutingLogRepository, RoutingLog, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[RoutingLogRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> RoutingLogRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
