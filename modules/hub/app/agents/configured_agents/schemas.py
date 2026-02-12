"""ConfiguredAgent Schemas for Hub Module.

Pydantic schemas for ConfiguredAgent CRUD operations.
"""

from uuid import UUID

from app.agents.agent_mcps.schemas import AgentMCPRead
from app.agents.agent_skills.schemas import AgentSkillRead
from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field

JsonSerializableType = str | int | float | bool | None | list | dict


class ConfiguredAgentBase(BaseModel):
    """Base schema for ConfiguredAgent."""

    name: str = Field(..., max_length=100, description="Agent Name")
    description: str | None = Field(default=None, description="Agent Description")
    model_name: str = Field(..., max_length=100, description="Model Name (from Catalog)")
    system_prompt: str | None = Field(default=None, description="System Prompt")
    config: dict[str, JsonSerializableType] = Field(default_factory=dict, description="Configuration")
    is_active: bool = Field(default=True, description="Active Status")


class ConfiguredAgentCreate(ConfiguredAgentBase):
    """Schema for creating a new ConfiguredAgent."""

    skill_ids: list[UUID] = Field(default_factory=list, description="List of Skill IDs")
    mcp_ids: list[UUID] = Field(default_factory=list, description="List of MCP IDs")


class ConfiguredAgentUpdate(BaseModel):
    """Schema for updating ConfiguredAgent."""

    name: str | None = Field(default=None, max_length=100, description="Agent Name")
    description: str | None = Field(default=None, description="Agent Description")
    model_name: str | None = Field(default=None, max_length=100, description="Model Name")
    system_prompt: str | None = Field(default=None, description="System Prompt")
    config: dict[str, JsonSerializableType] | None = Field(default=None, description="Configuration")
    is_active: bool | None = Field(default=None, description="Active Status")
    skill_ids: list[UUID] | None = Field(default=None, description="List of Skill IDs")
    mcp_ids: list[UUID] | None = Field(default=None, description="List of MCP IDs")


class ConfiguredAgentRead(UUIDSchemaMixin, TimestampSchemaMixin, ConfiguredAgentBase):
    """Schema for reading ConfiguredAgent data."""

    skills: list[AgentSkillRead] = Field(default_factory=list, description="Linked Skills")
    mcps: list[AgentMCPRead] = Field(default_factory=list, description="Linked MCPs")

    model_config = ConfigDict(from_attributes=True)
