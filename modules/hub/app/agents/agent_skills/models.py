"""AgentSkill Model for Hub Module.

AgentSkill: Registry of available agent skills.
DB Schema Reference: docs/specification/DB_SCHEMA.md#2.5
"""

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class AgentSkill(Base, UUIDMixin, TimestampMixin):
    """Registry of available agent skills."""

    __tablename__ = "agent_skills"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    skill_path: Mapped[str] = mapped_column(String(500), nullable=False)
    version: Mapped[str] = mapped_column(String(20), nullable=False, default="1.0.0")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
