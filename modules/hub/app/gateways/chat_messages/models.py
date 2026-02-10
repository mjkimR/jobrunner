"""Chat Message Model for Hub Module.

Chat Message: Chat message within a conversation.
DB Schema Reference: docs/specification/DB_SCHEMA.md#3.2
"""

from typing import TYPE_CHECKING
from uuid import UUID

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.agents.agent_executions.models import AgentExecution
    from app.gateways.conversations.models import Conversation


class ChatMessage(Base, UUIDMixin, TimestampMixin):
    """Chat message within a conversation."""

    __tablename__ = "chat_messages"

    conversation_id: Mapped[UUID] = mapped_column(ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_type: Mapped[str] = mapped_column(String(50), nullable=False, default="text")
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, nullable=False, default={})
    agent_execution_id: Mapped[UUID | None] = mapped_column(ForeignKey("agent_executions.id"), nullable=True)

    # Relationships
    conversation: Mapped["Conversation"] = relationship("Conversation", back_populates="messages")
    agent_execution: Mapped["AgentExecution"] = relationship("AgentExecution")
