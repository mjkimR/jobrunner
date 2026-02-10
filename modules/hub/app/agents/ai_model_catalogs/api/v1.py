from typing import Annotated
from uuid import UUID

import yaml
from app.agents.ai_model_catalogs.schemas import AIModelCatalogCreate, AIModelCatalogRead
from app.agents.ai_model_catalogs.usecases.crud import (
    CreateAIModelCatalogUseCase,
    DeleteAIModelCatalogUseCase,
    GetAIModelCatalogLatestUseCase,
    GetAIModelCatalogUseCase,
    GetMultiAIModelCatalogUseCase,
)
from app_base.base.deps.params.page import PaginationParam
from app_base.base.exceptions.basic import BadRequestException, NotFoundException
from app_base.base.schemas.delete_resp import DeleteResponse
from app_base.base.schemas.paginated import PaginatedList
from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/ai_model_catalogs", tags=["AIModelCatalog"], dependencies=[])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AIModelCatalogRead)
async def create_ai_model_catalog(
    use_case: Annotated[CreateAIModelCatalogUseCase, Depends()],
    ai_model_catalog_in: AIModelCatalogCreate,
):
    return await use_case.execute(ai_model_catalog_in)


@router.post("/upload_yaml", status_code=status.HTTP_201_CREATED, response_model=AIModelCatalogRead)
async def upload_yaml_ai_model_catalog(
    use_case: Annotated[CreateAIModelCatalogUseCase, Depends()],
    file: Annotated[UploadFile, File(description="YAML file containing AI Model data")],
):
    file_content = await file.read()
    try:
        ai_model_catalog_in = AIModelCatalogCreate(data=yaml.safe_load(file_content))
    except yaml.YAMLError as e:
        raise BadRequestException(f"Invalid YAML file: {e}") from e
    return await use_case.execute(ai_model_catalog_in)


@router.get("/download_yaml", response_class=StreamingResponse)
async def download_yaml_ai_model_catalog(
    use_case: Annotated[GetAIModelCatalogUseCase, Depends()],
    ai_model_catalog_id: UUID,
):
    ai_model_catalog = await use_case.execute(ai_model_catalog_id)
    if not ai_model_catalog:
        raise NotFoundException()
    return StreamingResponse(yaml.dump(ai_model_catalog.data), media_type="text/yaml")


@router.get("", response_model=PaginatedList[AIModelCatalogRead])
async def get_ai_model_catalogs(
    use_case: Annotated[GetMultiAIModelCatalogUseCase, Depends()],
    pagination: PaginationParam,
):
    return await use_case.execute(**pagination)


@router.get("/{ai_model_catalog_id}", response_model=AIModelCatalogRead)
async def get_ai_model_catalog(
    use_case: Annotated[GetAIModelCatalogUseCase, Depends()],
    ai_model_catalog_id: UUID,
):
    ai_model_catalog = await use_case.execute(ai_model_catalog_id)
    if not ai_model_catalog:
        raise NotFoundException()
    return ai_model_catalog


@router.get("/latest", response_model=AIModelCatalogRead)
async def get_latest_ai_model_catalog(
    use_case: Annotated[GetAIModelCatalogLatestUseCase, Depends()],
):
    ai_model_catalog = await use_case.execute()
    if not ai_model_catalog:
        raise NotFoundException()
    return ai_model_catalog


@router.delete("/{ai_model_catalog_id}", response_model=DeleteResponse)
async def delete_ai_model_catalog(
    use_case: Annotated[DeleteAIModelCatalogUseCase, Depends()],
    ai_model_catalog_id: UUID,
):
    return await use_case.execute(ai_model_catalog_id)
