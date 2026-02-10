"""AgentMCP Model for Hub Module.

AgentMCP: Registry of available MCP servers.
DB Schema Reference: docs/specification/DB_SCHEMA.md#2.6
"""

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class AgentMCP(Base, UUIDMixin, TimestampMixin):
    """Registry of available MCP servers."""

    __tablename__ = "agent_mcps"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    mcp_endpoint: Mapped[str] = mapped_column(String(500), nullable=False)
    version: Mapped[str] = mapped_column(String(20), nullable=False, default="1.0.0")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
