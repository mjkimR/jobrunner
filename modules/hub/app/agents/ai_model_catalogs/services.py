from typing import Annotated

from app.agents.ai_model_catalogs.models import AIModelCatalog
from app.agents.ai_model_catalogs.repos import AIModelCatalogRepository
from app.agents.ai_model_catalogs.schemas import AIModelCatalogCreate, AIModelCatalogDbCreate
from app_base.base.services.base import (
    BaseContextKwargs,
    BaseCreateServiceMixin,
    BaseDeleteServiceMixin,
    BaseGetMultiServiceMixin,
    BaseGetServiceMixin,
)
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class AIModelCatalogContextKwargs(BaseContextKwargs):
    pass


class AIModelCatalogService(
    BaseCreateServiceMixin[AIModelCatalogRepository, AIModelCatalog, AIModelCatalogCreate, AIModelCatalogContextKwargs],
    BaseGetMultiServiceMixin[AIModelCatalogRepository, AIModelCatalog, AIModelCatalogContextKwargs],
    BaseGetServiceMixin[AIModelCatalogRepository, AIModelCatalog, AIModelCatalogContextKwargs],
    # BaseUpdateServiceMixin[AIModelRepository, AIModel, AIModelUpdate, AIModelCatalogContextKwargs],
    BaseDeleteServiceMixin[AIModelCatalogRepository, AIModelCatalog, AIModelCatalogContextKwargs],
):
    def __init__(self, repo: Annotated[AIModelCatalogRepository, Depends()]):
        self._repo = repo

    @property
    def repo(self) -> AIModelCatalogRepository:
        return self._repo

    @property
    def context_model(self):
        return AIModelCatalogContextKwargs

    async def get_latest_ai_model(
        self,
        session: AsyncSession,
    ) -> AIModelCatalog | None:
        latest = await self.repo.get_multi(session, order_by=AIModelCatalog.version.desc(), limit=1)
        if not latest.items:
            return None
        return latest.items[0]

    async def create(
        self,
        session: AsyncSession,
        schema: AIModelCatalogCreate,
        context: AIModelCatalogContextKwargs | None = None,
    ) -> AIModelCatalog:
        """Create a new AI Model with an incremented version."""
        # Get the latest version from the database
        latest = await self.get_latest_ai_model(session)
        if latest:
            next_version = latest.version + 1
        else:
            next_version = 1

        # Create DB schema with the injected version
        db_schema = AIModelCatalogDbCreate(
            data=schema.data,
            version=next_version,
        )

        return await self.repo.create(session, db_schema)
