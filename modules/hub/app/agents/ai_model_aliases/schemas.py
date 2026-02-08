from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AIModelAliasCreate(BaseModel):
    name: str = Field(description="The name of the ai_model_alias.")


class AIModelAliasUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the ai_model_alias.")


class AIModelAliasRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the ai_model_alias.")
    model_config = ConfigDict(from_attributes=True)
