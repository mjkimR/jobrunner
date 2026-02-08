"""TaskTag Schemas for Hub Module.

Pydantic schemas for TaskTag CRUD operations.
"""

import datetime

from app_base.base.schemas.mixin import UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskTagCreate(BaseModel):
    """Schema for creating a new TaskTag."""

    name: str = Field(..., max_length=100, description="Tag name (unique)")
    description: str | None = Field(default=None, max_length=255, description="Tag description")
    color: str | None = Field(
        default=None,
        max_length=7,
        pattern=r"^#[0-9A-Fa-f]{6}$",
        description="Hex color code (#RRGGBB)",
    )


class TaskTagUpdate(BaseModel):
    """Schema for updating an existing TaskTag."""

    name: str | None = Field(default=None, max_length=100, description="Tag name (unique)")
    description: str | None = Field(default=None, max_length=255, description="Tag description")
    color: str | None = Field(
        default=None,
        max_length=7,
        pattern=r"^#[0-9A-Fa-f]{6}$",
        description="Hex color code (#RRGGBB)",
    )


class TaskTagRead(UUIDSchemaMixin, BaseModel):
    """Schema for reading TaskTag data."""

    name: str = Field(..., description="Tag name")
    description: str | None = Field(default=None, description="Tag description")
    color: str | None = Field(default=None, description="Hex color code")
    created_at: datetime.datetime = Field(..., description="Creation timestamp")

    model_config = ConfigDict(from_attributes=True)
