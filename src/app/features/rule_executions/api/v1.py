import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from app.features.rule_executions.schemas import (
    RuleExecutionCreate,
    RuleExecutionRead,
    RuleExecutionUpdate,
)
from app.features.rule_executions.usecases.crud import (
    CreateRuleExecutionUseCase,
    DeleteRuleExecutionUseCase,
    GetRuleExecutionUseCase,
    GetMultiRuleExecutionUseCase,
    UpdateRuleExecutionUseCase,
)

router = APIRouter(prefix="/rule_executions", tags=["RuleExecutions"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=RuleExecutionRead)
async def create_rule_execution(
    use_case: Annotated[CreateRuleExecutionUseCase, Depends()],
    rule_execution_in: RuleExecutionCreate,
):
    return await use_case.execute(rule_execution_in)


@router.get("", response_model=PaginatedList[RuleExecutionRead])
async def get_rule_executions(
    use_case: Annotated[GetMultiRuleExecutionUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{rule_execution_id}", response_model=RuleExecutionRead)
async def get_rule_execution(
    use_case: Annotated[GetRuleExecutionUseCase, Depends()],
    rule_execution_id: uuid.UUID,
):
    rule_execution = await use_case.execute(rule_execution_id)
    if not rule_execution:
        raise NotFoundException()
    return rule_execution


@router.put("/{rule_execution_id}", response_model=RuleExecutionRead)
async def update_rule_execution(
    use_case: Annotated[UpdateRuleExecutionUseCase, Depends()],
    rule_execution_id: uuid.UUID,
    rule_execution_in: RuleExecutionUpdate,
):
    rule_execution = await use_case.execute(rule_execution_id, rule_execution_in)
    if not rule_execution:
        raise NotFoundException()
    return rule_execution


@router.delete("/{rule_execution_id}", response_model=DeleteResponse)
async def delete_rule_execution(
    use_case: Annotated[DeleteRuleExecutionUseCase, Depends()],
    rule_execution_id: uuid.UUID,
):
    return await use_case.execute(rule_execution_id)
