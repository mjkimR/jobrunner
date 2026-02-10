from typing import Annotated
from uuid import UUID

from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentRead, ConfiguredAgentUpdate
from app.agents.configured_agents.usecases.crud import (
    CreateConfiguredAgentUseCase,
    DeleteConfiguredAgentUseCase,
    GetConfiguredAgentUseCase,
    GetMultiConfiguredAgentUseCase,
    UpdateConfiguredAgentUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/configured_agents", tags=["ConfiguredAgent"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ConfiguredAgentRead)
async def create_configured_agent(
    use_case: Annotated[CreateConfiguredAgentUseCase, Depends()],
    configured_agent_in: ConfiguredAgentCreate,
):
    return await use_case.execute(configured_agent_in)


@router.get("", response_model=PaginatedList[ConfiguredAgentRead])
async def get_configured_agents(
    use_case: Annotated[GetMultiConfiguredAgentUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{configured_agent_id}", response_model=ConfiguredAgentRead)
async def get_configured_agent(
    use_case: Annotated[GetConfiguredAgentUseCase, Depends()],
    configured_agent_id: UUID,
):
    configured_agent = await use_case.execute(configured_agent_id)
    if not configured_agent:
        raise NotFoundException()
    return configured_agent


@router.put("/{configured_agent_id}", response_model=ConfiguredAgentRead)
async def update_configured_agent(
    use_case: Annotated[UpdateConfiguredAgentUseCase, Depends()],
    configured_agent_id: UUID,
    configured_agent_in: ConfiguredAgentUpdate,
):
    configured_agent = await use_case.execute(configured_agent_id, configured_agent_in)
    if not configured_agent:
        raise NotFoundException()
    return configured_agent


@router.delete("/{configured_agent_id}", response_model=DeleteResponse)
async def delete_configured_agent(
    use_case: Annotated[DeleteConfiguredAgentUseCase, Depends()],
    configured_agent_id: UUID,
):
    return await use_case.execute(configured_agent_id)
