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
from app.features.rules.models import Rule
from app.features.rules.repos import RuleRepository
from app.features.rules.schemas import RuleCreate, RuleUpdate


class RuleService(
    BaseCreateServiceMixin[RuleRepository, Rule, RuleCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[RuleRepository, Rule, BaseContextKwargs],
    BaseGetServiceMixin[RuleRepository, Rule, BaseContextKwargs],
    BaseUpdateServiceMixin[RuleRepository, Rule, RuleUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[RuleRepository, Rule, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[RuleRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> RuleRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
