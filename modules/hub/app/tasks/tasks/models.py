"""Task Model for Hub Module.

Task: Task item managed by Host Agent or User.
DB Schema Reference: docs/specification/DB_SCHEMA.md#1.1
"""

import datetime
import uuid
from typing import TYPE_CHECKING

from app.tasks.tasks.enum import TaskComplexity, TaskPriority, TaskQueue, TaskSource, TaskStatus, TaskUrgency
from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.tasks.task_histories.models import TaskHistory
    from app.tasks.task_tags.models import TaskTag


class Task(Base, UUIDMixin, TimestampMixin):
    """Task entity for Host Agent's persistent memory."""

    __tablename__ = "tasks"

    # Basic fields
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Status & routing fields
    status: Mapped[str] = mapped_column(String(50), nullable=False, default=TaskStatus.PENDING.value)
    priority: Mapped[str] = mapped_column(String(20), nullable=False, default=TaskPriority.NORMAL.value)
    urgency: Mapped[str] = mapped_column(String(20), nullable=False, default=TaskUrgency.NORMAL.value)
    complexity: Mapped[str] = mapped_column(String(20), nullable=False, default=TaskComplexity.SIMPLE.value)
    queue: Mapped[str] = mapped_column(String(100), nullable=False, default=TaskQueue.DEFAULT.value)

    # Hierarchy & source
    parent_task_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("tasks.id"), nullable=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False, default=TaskSource.USER.value)
    external_ref: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Timeline
    due_date: Mapped[datetime.datetime | None] = mapped_column(nullable=True)
    completed_at: Mapped[datetime.datetime | None] = mapped_column(nullable=True)

    # Result
    result_summary: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships (use string references to avoid circular imports)
    parent_task: Mapped["Task | None"] = relationship("Task", remote_side="Task.id", back_populates="subtasks")
    subtasks: Mapped[list["Task"]] = relationship("Task", back_populates="parent_task", cascade="all, delete-orphan")
    tags: Mapped[list["TaskTag"]] = relationship(
        "TaskTag",
        secondary="task_tag_associations",
        back_populates="tasks",
    )
    histories: Mapped[list["TaskHistory"]] = relationship(
        "TaskHistory", back_populates="task", cascade="all, delete-orphan"
    )
