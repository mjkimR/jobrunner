from typing import Any

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class WorkspaceCreate(BaseModel):
    name: str = Field(max_length=100, description="The name of the workspace.")
    alias: str = Field(
        max_length=100,
        description="The alias (api-friendly identifier) of the workspace.",
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )
    description: str | None = Field(default=None, description="A description of the workspace.")
    meta: dict[str, Any] = Field(default_factory=dict, description="JSONB settings for the workspace.")
    is_active: bool = Field(default=True, description="Whether the workspace is active.")
    is_default: bool = Field(default=False, description="Whether the workspace is the default workspace.")


class WorkspaceUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=100, description="The name of the workspace.")
    alias: str | None = Field(
        default=None,
        max_length=100,
        description="The alias (api-friendly identifier) of the workspace.",
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )
    description: str | None = Field(default=None, description="A description of the workspace.")
    meta: dict[str, Any] | None = Field(default=None, description="JSONB settings for the workspace.")
    is_active: bool | None = Field(default=None, description="Whether the workspace is active.")
    is_default: bool | None = Field(default=None, description="Whether the workspace is the default workspace.")


class WorkspaceRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(max_length=100, description="The name of the workspace.")
    alias: str = Field(max_length=100, description="The alias (api-friendly identifier) of the workspace.")
    description: str | None = Field(default=None, description="A description of the workspace.")
    meta: dict[str, Any] = Field(description="JSONB settings for the workspace.")
    is_active: bool = Field(description="Whether the workspace is active.")
    is_default: bool = Field(description="Whether the workspace is the default workspace.")

    model_config = ConfigDict(from_attributes=True)
