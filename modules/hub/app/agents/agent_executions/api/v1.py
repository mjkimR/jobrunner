import uuid
from typing import Annotated

from app.agents.agent_executions.schemas import AgentExecutionCreate, AgentExecutionRead, AgentExecutionUpdate
from app.agents.agent_executions.usecases.crud import (
    CreateAgentExecutionUseCase,
    DeleteAgentExecutionUseCase,
    GetAgentExecutionUseCase,
    GetMultiAgentExecutionUseCase,
    UpdateAgentExecutionUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/agent_executions", tags=["AgentExecution"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AgentExecutionRead)
async def create_agent_execution(
    use_case: Annotated[CreateAgentExecutionUseCase, Depends()],
    agent_execution_in: AgentExecutionCreate,
):
    return await use_case.execute(agent_execution_in)


@router.get("", response_model=PaginatedList[AgentExecutionRead])
async def get_agent_executions(
    use_case: Annotated[GetMultiAgentExecutionUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{agent_execution_id}", response_model=AgentExecutionRead)
async def get_agent_execution(
    use_case: Annotated[GetAgentExecutionUseCase, Depends()],
    agent_execution_id: uuid.UUID,
):
    agent_execution = await use_case.execute(agent_execution_id)
    if not agent_execution:
        raise NotFoundException()
    return agent_execution


@router.put("/{agent_execution_id}", response_model=AgentExecutionRead)
async def update_agent_execution(
    use_case: Annotated[UpdateAgentExecutionUseCase, Depends()],
    agent_execution_id: uuid.UUID,
    agent_execution_in: AgentExecutionUpdate,
):
    agent_execution = await use_case.execute(agent_execution_id, agent_execution_in)
    if not agent_execution:
        raise NotFoundException()
    return agent_execution


@router.delete("/{agent_execution_id}", response_model=DeleteResponse)
async def delete_agent_execution(
    use_case: Annotated[DeleteAgentExecutionUseCase, Depends()],
    agent_execution_id: uuid.UUID,
):
    return await use_case.execute(agent_execution_id)
