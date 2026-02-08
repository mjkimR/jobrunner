from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    name: str = Field(description="The name of the task.")


class TaskUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the task.")


class TaskRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the task.")
    model_config = ConfigDict(from_attributes=True)
