from typing import Annotated

from app.agents.ai_model_groups.models import AIModelGroup
from app.agents.ai_model_groups.repos import AIModelGroupRepository
from app.agents.ai_model_groups.schemas import AIModelGroupCreate, AIModelGroupUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AIModelGroupContextKwargs(BaseContextKwargs):
    pass


class AIModelGroupService(
    BaseCreateServiceMixin[AIModelGroupRepository, AIModelGroup, AIModelGroupCreate, AIModelGroupContextKwargs],
    BaseGetMultiServiceMixin[AIModelGroupRepository, AIModelGroup, AIModelGroupContextKwargs],
    BaseGetServiceMixin[AIModelGroupRepository, AIModelGroup, AIModelGroupContextKwargs],
    BaseUpdateServiceMixin[AIModelGroupRepository, AIModelGroup, AIModelGroupUpdate, AIModelGroupContextKwargs],
    BaseDeleteServiceMixin[AIModelGroupRepository, AIModelGroup, AIModelGroupContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelGroupRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelGroupRepository:
        return self._repo

    @property
    def context_model(self):
        return AIModelGroupContextKwargs
