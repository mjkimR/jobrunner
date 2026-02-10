from typing import Annotated
from uuid import UUID

from app.agents.agent_skills.schemas import AgentSkillCreate, AgentSkillRead, AgentSkillUpdate
from app.agents.agent_skills.usecases.crud import (
    CreateAgentSkillUseCase,
    DeleteAgentSkillUseCase,
    GetAgentSkillUseCase,
    GetMultiAgentSkillUseCase,
    UpdateAgentSkillUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/agent_skills", tags=["AgentSkill"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AgentSkillRead)
async def create_agent_skill(
    use_case: Annotated[CreateAgentSkillUseCase, Depends()],
    agent_skill_in: AgentSkillCreate,
):
    return await use_case.execute(agent_skill_in)


@router.get("", response_model=PaginatedList[AgentSkillRead])
async def get_agent_skills(
    use_case: Annotated[GetMultiAgentSkillUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{agent_skill_id}", response_model=AgentSkillRead)
async def get_agent_skill(
    use_case: Annotated[GetAgentSkillUseCase, Depends()],
    agent_skill_id: UUID,
):
    agent_skill = await use_case.execute(agent_skill_id)
    if not agent_skill:
        raise NotFoundException()
    return agent_skill


@router.put("/{agent_skill_id}", response_model=AgentSkillRead)
async def update_agent_skill(
    use_case: Annotated[UpdateAgentSkillUseCase, Depends()],
    agent_skill_id: UUID,
    agent_skill_in: AgentSkillUpdate,
):
    agent_skill = await use_case.execute(agent_skill_id, agent_skill_in)
    if not agent_skill:
        raise NotFoundException()
    return agent_skill


@router.delete("/{agent_skill_id}", response_model=DeleteResponse)
async def delete_agent_skill(
    use_case: Annotated[DeleteAgentSkillUseCase, Depends()],
    agent_skill_id: UUID,
):
    return await use_case.execute(agent_skill_id)
