import uuid
from typing import Annotated

from app.agents.agent_mcps.schemas import AgentMCPCreate, AgentMCPRead, AgentMCPUpdate
from app.agents.agent_mcps.usecases.crud import (
    CreateAgentMCPUseCase,
    DeleteAgentMCPUseCase,
    GetAgentMCPUseCase,
    GetMultiAgentMCPUseCase,
    UpdateAgentMCPUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/agent_mcps", tags=["AgentMCP"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AgentMCPRead)
async def create_agent_mcp(
    use_case: Annotated[CreateAgentMCPUseCase, Depends()],
    agent_mcp_in: AgentMCPCreate,
):
    return await use_case.execute(agent_mcp_in)


@router.get("", response_model=PaginatedList[AgentMCPRead])
async def get_agent_mcps(
    use_case: Annotated[GetMultiAgentMCPUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{agent_mcp_id}", response_model=AgentMCPRead)
async def get_agent_mcp(
    use_case: Annotated[GetAgentMCPUseCase, Depends()],
    agent_mcp_id: uuid.UUID,
):
    agent_mcp = await use_case.execute(agent_mcp_id)
    if not agent_mcp:
        raise NotFoundException()
    return agent_mcp


@router.put("/{agent_mcp_id}", response_model=AgentMCPRead)
async def update_agent_mcp(
    use_case: Annotated[UpdateAgentMCPUseCase, Depends()],
    agent_mcp_id: uuid.UUID,
    agent_mcp_in: AgentMCPUpdate,
):
    agent_mcp = await use_case.execute(agent_mcp_id, agent_mcp_in)
    if not agent_mcp:
        raise NotFoundException()
    return agent_mcp


@router.delete("/{agent_mcp_id}", response_model=DeleteResponse)
async def delete_agent_mcp(
    use_case: Annotated[DeleteAgentMCPUseCase, Depends()],
    agent_mcp_id: uuid.UUID,
):
    return await use_case.execute(agent_mcp_id)
