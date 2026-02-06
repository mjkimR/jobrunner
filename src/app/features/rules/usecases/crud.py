from typing import Annotated

from fastapi import Depends

from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from app.features.rules.models import Rule
from app.features.rules.schemas import RuleCreate, RuleUpdate
from app.features.rules.services import RuleService, BaseContextKwargs


class GetRuleUseCase(BaseGetUseCase[RuleService, Rule, BaseContextKwargs]):
    def __init__(self, service: Annotated[RuleService, Depends()]) -> None:
        super().__init__(service)


class GetMultiRuleUseCase(BaseGetMultiUseCase[RuleService, Rule, BaseContextKwargs]):
    def __init__(self, service: Annotated[RuleService, Depends()]) -> None:
        super().__init__(service)


class CreateRuleUseCase(
    BaseCreateUseCase[RuleService, Rule, RuleCreate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[RuleService, Depends()]) -> None:
        super().__init__(service)


class UpdateRuleUseCase(
    BaseUpdateUseCase[RuleService, Rule, RuleUpdate, BaseContextKwargs]
):
    def __init__(self, service: Annotated[RuleService, Depends()]) -> None:
        super().__init__(service)


class DeleteRuleUseCase(BaseDeleteUseCase[RuleService, Rule, BaseContextKwargs]):
    def __init__(self, service: Annotated[RuleService, Depends()]) -> None:
        super().__init__(service)
