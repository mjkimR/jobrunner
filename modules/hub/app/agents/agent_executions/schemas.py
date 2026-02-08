from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentExecutionCreate(BaseModel):
    name: str = Field(description="The name of the agent_execution.")


class AgentExecutionUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the agent_execution.")


class AgentExecutionRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the agent_execution.")
    model_config = ConfigDict(from_attributes=True)
