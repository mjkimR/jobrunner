"""AgentSkill Schemas for Hub Module.

Pydantic schemas for AgentSkill CRUD operations.
"""

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class AgentSkillBase(BaseModel):
    """Base schema for AgentSkill."""

    name: str = Field(..., max_length=100, description="Skill Name")
    description: str | None = Field(default=None, description="Skill Description")
    skill_path: str = Field(..., max_length=500, description="Skill Path (SKILL.md)")
    version: str = Field(default="1.0.0", max_length=20, description="Version")
    is_active: bool = Field(default=True, description="Active status")


class AgentSkillCreate(AgentSkillBase):
    """Schema for creating a new AgentSkill entry."""

    pass


class AgentSkillUpdate(AgentSkillBase):
    """Schema for updating AgentSkill."""

    name: str | None = Field(default=None, max_length=100, description="Skill Name")
    description: str | None = Field(default=None, description="Skill Description")
    skill_path: str | None = Field(default=None, max_length=500, description="Skill Path")
    version: str | None = Field(default=None, max_length=20, description="Version")
    is_active: bool | None = Field(default=None, description="Active status")


class AgentSkillRead(UUIDSchemaMixin, TimestampSchemaMixin, AgentSkillBase):
    """Schema for reading AgentSkill data."""

    model_config = ConfigDict(from_attributes=True)
