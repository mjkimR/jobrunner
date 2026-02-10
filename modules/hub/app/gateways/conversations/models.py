"""Conversation Model for Hub Module.

Conversation: Chat session managed per Workspace.
DB Schema Reference: docs/specification/DB_SCHEMA.md#3.1
"""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.gateways.chat_messages.models import ChatMessage
    from app.platform.workspaces.models import Workspace


class Conversation(Base, UUIDMixin, TimestampMixin):
    """Chat session managed per Workspace."""

    __tablename__ = "conversations"

    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspaces.id"), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    channel: Mapped[str] = mapped_column(String(50), nullable=False, default="web")
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="active")
    context: Mapped[dict] = mapped_column(JSONB, nullable=False, default={})
    started_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    ended_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace")
    messages: Mapped[list["ChatMessage"]] = relationship(
        "ChatMessage", back_populates="conversation", cascade="all, delete-orphan"
    )
