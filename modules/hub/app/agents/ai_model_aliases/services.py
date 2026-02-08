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


class AIModelAliasService(
    BaseCreateServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasCreate, BaseContextKwargs],
    BaseGetMultiServiceMixin[AIModelAliasRepository, AIModelAlias, BaseContextKwargs],
    BaseGetServiceMixin[AIModelAliasRepository, AIModelAlias, BaseContextKwargs],
    BaseUpdateServiceMixin[AIModelAliasRepository, AIModelAlias, AIModelAliasUpdate, BaseContextKwargs],
    BaseDeleteServiceMixin[AIModelAliasRepository, AIModelAlias, BaseContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelAliasRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelAliasRepository:
        return self._repo

    @property
    def context_model(self):
        return BaseContextKwargs
