from typing import Annotated

from fastapi import Depends

from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from app.features.rule_executions.models import RuleExecution
from app.features.rule_executions.repos import RuleExecutionRepository
from app.features.rule_executions.schemas import (
    RuleExecutionCreate,
    RuleExecutionUpdate,
)


class RuleExecutionService(
    BaseCreateServiceMixin[
        RuleExecutionRepository, RuleExecution, RuleExecutionCreate, BaseContextKwargs
    ],
    BaseGetMultiServiceMixin[RuleExecutionRepository, RuleExecution, BaseContextKwargs],
    BaseGetServiceMixin[RuleExecutionRepository, RuleExecution, BaseContextKwargs],
    BaseUpdateServiceMixin[
        RuleExecutionRepository, RuleExecution, RuleExecutionUpdate, BaseContextKwargs
    ],
    BaseDeleteServiceMixin[RuleExecutionRepository, RuleExecution, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[RuleExecutionRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> RuleExecutionRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
