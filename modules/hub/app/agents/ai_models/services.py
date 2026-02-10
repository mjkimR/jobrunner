from typing import Annotated

from app.agents.ai_models.models import AIModel
from app.agents.ai_models.repos import AIModelRepository
from app.agents.ai_models.schemas import AIModelCreate, AIModelUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AIModelContextKwargs(BaseContextKwargs):
    pass


class AIModelService(
    BaseCreateServiceMixin[AIModelRepository, AIModel, AIModelCreate, AIModelContextKwargs],
    BaseGetMultiServiceMixin[AIModelRepository, AIModel, AIModelContextKwargs],
    BaseGetServiceMixin[AIModelRepository, AIModel, AIModelContextKwargs],
    BaseUpdateServiceMixin[AIModelRepository, AIModel, AIModelUpdate, AIModelContextKwargs],
    BaseDeleteServiceMixin[AIModelRepository, AIModel, AIModelContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelRepository:
        return self._repo

    @property
    def context_model(self):
        return AIModelContextKwargs
