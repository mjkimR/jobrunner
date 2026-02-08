from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentSkillCreate(BaseModel):
    name: str = Field(description="The name of the agent_skill.")


class AgentSkillUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the agent_skill.")


class AgentSkillRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the agent_skill.")
    model_config = ConfigDict(from_attributes=True)
