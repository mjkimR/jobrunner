"""TaskHistory Model for Hub Module.

TaskHistory: History of task status changes and assignments.
DB Schema Reference: docs/specification/DB_SCHEMA.md#1.3
"""

import datetime
import enum
from typing import TYPE_CHECKING, Optional
from uuid import UUID

from app_base.base.models.mixin import Base, UUIDMixin
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.agents.configured_agents.models import ConfiguredAgent
    from app.platform.workspaces.models import Workspace
    from app.tasks.tasks.models import Task


class TaskHistoryEventType(str, enum.Enum):
    """History event type."""

    STATUS_CHANGE = "status_change"
    ASSIGNMENT = "assignment"
    QUEUE_CHANGE = "queue_change"
    PRIORITY_CHANGE = "priority_change"


class TaskHistory(Base, UUIDMixin):
    """History record for Task status changes and assignments."""

    __tablename__ = "task_history"

    # Foreign keys
    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspaces.id"), nullable=False)
    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"), nullable=False)
    assigned_agent_id: Mapped[UUID | None] = mapped_column(ForeignKey("configured_agents.id"), nullable=True)

    # Event details
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    previous_value: Mapped[str | None] = mapped_column(String(100), nullable=True)
    new_value: Mapped[str] = mapped_column(String(100), nullable=False)
    changed_by: Mapped[str] = mapped_column(String(100), nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamp (only created_at, history is immutable)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace")
    task: Mapped["Task"] = relationship("Task", back_populates="histories")
    assigned_agent: Mapped[Optional["ConfiguredAgent"]] = relationship("ConfiguredAgent")
