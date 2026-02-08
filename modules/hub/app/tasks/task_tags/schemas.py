from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskTagCreate(BaseModel):
    name: str = Field(description="The name of the task_tag.")


class TaskTagUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the task_tag.")


class TaskTagRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the task_tag.")
    model_config = ConfigDict(from_attributes=True)
