from typing import Annotated

from fastapi import Depends

from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
    BaseUpdateUseCase,
)
from app.features.rule_executions.models import RuleExecution
from app.features.rule_executions.schemas import (
    RuleExecutionCreate,
    RuleExecutionUpdate,
)
from app.features.rule_executions.services import (
    RuleExecutionService,
    BaseContextKwargs,
)


class GetRuleExecutionUseCase(
    BaseGetUseCase[RuleExecutionService, RuleExecution, BaseContextKwargs]
):
    def __init__(self, service: Annotated[RuleExecutionService, Depends()]) -> None:
        super().__init__(service)


class GetMultiRuleExecutionUseCase(
    BaseGetMultiUseCase[RuleExecutionService, RuleExecution, BaseContextKwargs]
):
    def __init__(self, service: Annotated[RuleExecutionService, Depends()]) -> None:
        super().__init__(service)


class CreateRuleExecutionUseCase(
    BaseCreateUseCase[
        RuleExecutionService, RuleExecution, RuleExecutionCreate, BaseContextKwargs
    ]
):
    def __init__(self, service: Annotated[RuleExecutionService, Depends()]) -> None:
        super().__init__(service)


class UpdateRuleExecutionUseCase(
    BaseUpdateUseCase[
        RuleExecutionService, RuleExecution, RuleExecutionUpdate, BaseContextKwargs
    ]
):
    def __init__(self, service: Annotated[RuleExecutionService, Depends()]) -> None:
        super().__init__(service)


class DeleteRuleExecutionUseCase(
    BaseDeleteUseCase[RuleExecutionService, RuleExecution, BaseContextKwargs]
):
    def __init__(self, service: Annotated[RuleExecutionService, Depends()]) -> None:
        super().__init__(service)
