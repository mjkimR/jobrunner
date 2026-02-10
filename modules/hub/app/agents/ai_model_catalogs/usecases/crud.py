from typing import Annotated, Optional

from app.agents.ai_model_catalogs.models import AIModelCatalog
from app.agents.ai_model_catalogs.schemas import AIModelCatalogCreate
from app.agents.ai_model_catalogs.services import AIModelCatalogContextKwargs, AIModelCatalogService
from app_base.base.usecases.base import BaseUseCase
from app_base.base.usecases.crud import (
    BaseCreateUseCase,
    BaseDeleteUseCase,
    BaseGetMultiUseCase,
    BaseGetUseCase,
)
from app_base.core.database.transaction import AsyncTransaction
from fastapi import Depends


class GetAIModelCatalogUseCase(BaseGetUseCase[AIModelCatalogService, AIModelCatalog, AIModelCatalogContextKwargs]):
    def __init__(self, service: Annotated[AIModelCatalogService, Depends()]) -> None:
        super().__init__(service)


class GetAIModelCatalogLatestUseCase(BaseUseCase):
    def __init__(self, service: Annotated[AIModelCatalogService, Depends()]) -> None:
        self.service = service

    async def execute(self, context: Optional[AIModelCatalogContextKwargs] = None) -> Optional[AIModelCatalog]:
        async with AsyncTransaction() as session:
            return await self.service.get_latest_ai_model(session)


class GetMultiAIModelCatalogUseCase(
    BaseGetMultiUseCase[AIModelCatalogService, AIModelCatalog, AIModelCatalogContextKwargs]
):
    def __init__(self, service: Annotated[AIModelCatalogService, Depends()]) -> None:
        super().__init__(service)


class CreateAIModelCatalogUseCase(
    BaseCreateUseCase[AIModelCatalogService, AIModelCatalog, AIModelCatalogCreate, AIModelCatalogContextKwargs]
):
    def __init__(self, service: Annotated[AIModelCatalogService, Depends()]) -> None:
        super().__init__(service)


class DeleteAIModelCatalogUseCase(
    BaseDeleteUseCase[AIModelCatalogService, AIModelCatalog, AIModelCatalogContextKwargs]
):
    def __init__(self, service: Annotated[AIModelCatalogService, Depends()]) -> None:
        super().__init__(service)
