from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskHistoryCreate(BaseModel):
    name: str = Field(description="The name of the task_history.")


class TaskHistoryUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the task_history.")


class TaskHistoryRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the task_history.")
    model_config = ConfigDict(from_attributes=True)
