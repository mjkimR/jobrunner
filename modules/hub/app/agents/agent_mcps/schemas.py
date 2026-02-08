from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentMCPCreate(BaseModel):
    name: str = Field(description="The name of the agent_mcp.")


class AgentMCPUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the agent_mcp.")


class AgentMCPRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the agent_mcp.")
    model_config = ConfigDict(from_attributes=True)
