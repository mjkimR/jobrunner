"""AI Model Catalog Schemas for Hub Module.

Pydantic schemas for AIModelCatalog CRUD operations.
"""

from typing import Any

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AIModelCatalogCreate(BaseModel):
    """Schema for creating a new AI Model (External)."""

    data: dict[str, Any] = Field(..., description="YAML catalog data as JSON")


class AIModelCatalogDbCreate(AIModelCatalogCreate):
    """Schema for creating a new AI Model in the database (Internal)."""

    version: int = Field(..., description="Catalog version")


class AIModelCatalogUpdate(BaseModel):
    """Schema for updating an existing AI Model (External)."""

    data: dict[str, Any] | None = Field(default=None, description="YAML catalog data as JSON")


class AIModelCatalogDbUpdate(AIModelCatalogUpdate):
    """Schema for updating an existing AI Model in the database (Internal)."""

    version: int | None = Field(default=None, description="Catalog version")


class AIModelCatalogRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    """Schema for reading AI Model data."""

    version: int = Field(..., description="Catalog version")
    data: dict[str, Any] = Field(..., description="YAML catalog data as JSON")

    model_config = ConfigDict(from_attributes=True)
