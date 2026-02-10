"""RoutingLog Model for Hub Module.

RoutingLog: History of routing decisions by the Gateway.
DB Schema Reference: docs/specification/DB_SCHEMA.md#3.3
"""

from typing import TYPE_CHECKING
from uuid import UUID

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.agents.configured_agents.models import ConfiguredAgent
    from app.gateways.chat_messages.models import ChatMessage
    from app.tasks.tasks.models import Task


class RoutingLog(Base, UUIDMixin, TimestampMixin):
    """History of routing decisions by the Gateway."""

    __tablename__ = "routing_logs"

    message_id: Mapped[UUID] = mapped_column(ForeignKey("chat_messages.id", ondelete="CASCADE"), nullable=False)
    routing_result: Mapped[str] = mapped_column(String(50), nullable=False)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    reasoning: Mapped[str | None] = mapped_column(Text, nullable=True)
    target_task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id"), nullable=True)
    target_agent_id: Mapped[UUID | None] = mapped_column(ForeignKey("configured_agents.id"), nullable=True)

    # Relationships
    message: Mapped["ChatMessage"] = relationship("ChatMessage")
    target_task: Mapped["Task"] = relationship("Task")
    target_agent: Mapped["ConfiguredAgent"] = relationship("ConfiguredAgent")
