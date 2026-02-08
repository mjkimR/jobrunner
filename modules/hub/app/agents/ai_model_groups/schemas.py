from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AIModelGroupCreate(BaseModel):
    name: str = Field(description="The name of the ai_model_group.")


class AIModelGroupUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the ai_model_group.")


class AIModelGroupRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the ai_model_group.")
    model_config = ConfigDict(from_attributes=True)
