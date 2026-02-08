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


class AIModelService(
    BaseCreateServiceMixin[AIModelRepository, AIModel, AIModelCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[AIModelRepository, AIModel, BaseContextKwargs],
    BaseGetServiceMixin[AIModelRepository, AIModel, BaseContextKwargs],
    BaseUpdateServiceMixin[AIModelRepository, AIModel, AIModelUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[AIModelRepository, AIModel, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
