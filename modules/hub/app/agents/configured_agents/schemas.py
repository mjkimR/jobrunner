from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class ConfiguredAgentCreate(BaseModel):
    name: str = Field(description="The name of the configured_agent.")


class ConfiguredAgentUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the configured_agent.")


class ConfiguredAgentRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the configured_agent.")
    model_config = ConfigDict(from_attributes=True)
