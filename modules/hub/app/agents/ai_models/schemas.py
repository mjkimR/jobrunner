from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AIModelCreate(BaseModel):
    name: str = Field(description="The name of the ai_model.")


class AIModelUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the ai_model.")


class AIModelRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the ai_model.")
    model_config = ConfigDict(from_attributes=True)
