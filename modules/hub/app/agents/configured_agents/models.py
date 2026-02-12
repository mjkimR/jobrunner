"""ConfiguredAgent Model for Hub Module.

ConfiguredAgent: Hub-defined Agent configuration (Model + Skills + MCPs).
DB Schema Reference: docs/specification/DB_SCHEMA.md#2.2
"""

from typing import TYPE_CHECKING

from app.common.database import JSON_VARIANT
from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.agents.agent_mcps.models import AgentMCP
    from app.agents.agent_skills.models import AgentSkill


class ConfiguredAgentSkill(Base):
    """Association table for ConfiguredAgent and AgentSkill."""

    __tablename__ = "configured_agent_skills"

    agent_id: Mapped[str] = mapped_column(ForeignKey("configured_agents.id", ondelete="CASCADE"), primary_key=True)
    skill_id: Mapped[str] = mapped_column(ForeignKey("agent_skills.id", ondelete="CASCADE"), primary_key=True)


class ConfiguredAgentMCP(Base):
    """Association table for ConfiguredAgent and AgentMCP."""

    __tablename__ = "configured_agent_mcps"

    agent_id: Mapped[str] = mapped_column(ForeignKey("configured_agents.id", ondelete="CASCADE"), primary_key=True)
    mcp_id: Mapped[str] = mapped_column(ForeignKey("agent_mcps.id", ondelete="CASCADE"), primary_key=True)


class ConfiguredAgent(Base, UUIDMixin, TimestampMixin):
    """Hub-defined Agent configuration."""

    __tablename__ = "configured_agents"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    model_name: Mapped[str] = mapped_column(String(100), nullable=False)
    system_prompt: Mapped[str | None] = mapped_column(Text, nullable=True)
    config: Mapped[dict] = mapped_column(JSON_VARIANT, nullable=False, default={})
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Relationships
    skills: Mapped[list["AgentSkill"]] = relationship(
        "AgentSkill",
        secondary="configured_agent_skills",
        backref="configured_agents",
        lazy="selectin",
    )
    mcps: Mapped[list["AgentMCP"]] = relationship(
        "AgentMCP",
        secondary="configured_agent_mcps",
        backref="configured_agents",
        lazy="selectin",
    )
