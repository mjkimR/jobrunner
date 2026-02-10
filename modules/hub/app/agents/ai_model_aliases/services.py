from typing import Annotated

from app.agents.ai_model_aliases.models import AIModelAlias
from app.agents.ai_model_aliases.repos import AIModelAliasRepository
from app.agents.ai_model_aliases.schemas import AIModelAliasCreate, AIModelAliasUpdate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
    BaseUpdateServiceMixin,
)
from fastapi import Depends


class AIModelAliasContextKwargs(BaseContextKwargs):
    pass


class AIModelAliasService(
    BaseCreateServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasCreate, AIModelAliasContextKwargs],
    BaseGetMultiServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasContextKwargs],
    BaseGetServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasContextKwargs],
    BaseUpdateServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasUpdate, AIModelAliasContextKwargs],
    BaseDeleteServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelAliasRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelAliasRepository:
        return self._repo

    @property
    def context_model(self):
        return AIModelAliasContextKwargs
