import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from app.features.rules.schemas import RuleCreate, RuleRead, RuleUpdate
from app.features.rules.usecases.crud import (
    CreateRuleUseCase,
    DeleteRuleUseCase,
    GetRuleUseCase,
    GetMultiRuleUseCase,
    UpdateRuleUseCase,
)

router = APIRouter(prefix="/rules", tags=["Rules"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=RuleRead)
async def create_rule(
    use_case: Annotated[CreateRuleUseCase, Depends()],
    rule_in: RuleCreate,
):
    return await use_case.execute(rule_in)


@router.get("", response_model=PaginatedList[RuleRead])
async def get_rules(
    use_case: Annotated[GetMultiRuleUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{rule_id}", response_model=RuleRead)
async def get_rule(
    use_case: Annotated[GetRuleUseCase, Depends()],
    rule_id: uuid.UUID,
):
    rule = await use_case.execute(rule_id)
    if not rule:
        raise NotFoundException()
    return rule


@router.put("/{rule_id}", response_model=RuleRead)
async def update_rule(
    use_case: Annotated[UpdateRuleUseCase, Depends()],
    rule_id: uuid.UUID,
    rule_in: RuleUpdate,
):
    rule = await use_case.execute(rule_id, rule_in)
    if not rule:
        raise NotFoundException()
    return rule


@router.delete("/{rule_id}", response_model=DeleteResponse)
async def delete_rule(
    use_case: Annotated[DeleteRuleUseCase, Depends()],
    rule_id: uuid.UUID,
):
    return await use_case.execute(rule_id)
