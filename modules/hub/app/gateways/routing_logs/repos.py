from app.gateways.routing_logs.models import RoutingLog
from app.gateways.routing_logs.schemas import RoutingLogCreate, RoutingLogUpdate
from app_base.base.repos.base import BaseRepository


class RoutingLogRepository(BaseRepository[RoutingLog, RoutingLogCreate, RoutingLogUpdate]):
    model = RoutingLog
