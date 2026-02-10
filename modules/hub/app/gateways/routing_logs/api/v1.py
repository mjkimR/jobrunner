from typing import Annotated
from uuid import UUID

from app.gateways.routing_logs.schemas import RoutingLogCreate, RoutingLogRead, RoutingLogUpdate
from app.gateways.routing_logs.usecases.crud import (
    CreateRoutingLogUseCase,
    DeleteRoutingLogUseCase,
    GetMultiRoutingLogUseCase,
    GetRoutingLogUseCase,
    UpdateRoutingLogUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/routing_logs", tags=["RoutingLog"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=RoutingLogRead)
async def create_routing_log(
    use_case: Annotated[CreateRoutingLogUseCase, Depends()],
    routing_log_in: RoutingLogCreate,
):
    return await use_case.execute(routing_log_in)


@router.get("", response_model=PaginatedList[RoutingLogRead])
async def get_routing_logs(
    use_case: Annotated[GetMultiRoutingLogUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{routing_log_id}", response_model=RoutingLogRead)
async def get_routing_log(
    use_case: Annotated[GetRoutingLogUseCase, Depends()],
    routing_log_id: UUID,
):
    routing_log = await use_case.execute(routing_log_id)
    if not routing_log:
        raise NotFoundException()
    return routing_log


@router.put("/{routing_log_id}", response_model=RoutingLogRead)
async def update_routing_log(
    use_case: Annotated[UpdateRoutingLogUseCase, Depends()],
    routing_log_id: UUID,
    routing_log_in: RoutingLogUpdate,
):
    routing_log = await use_case.execute(routing_log_id, routing_log_in)
    if not routing_log:
        raise NotFoundException()
    return routing_log


@router.delete("/{routing_log_id}", response_model=DeleteResponse)
async def delete_routing_log(
    use_case: Annotated[DeleteRoutingLogUseCase, Depends()],
    routing_log_id: UUID,
):
    return await use_case.execute(routing_log_id)
