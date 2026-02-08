"""TaskTag Model for Hub Module.

TaskTag: Tag for classifying tasks.
TaskTagAssociation: M:N Junction Table.
DB Schema Reference: docs/specification/DB_SCHEMA.md#1.2
"""

import datetime
from typing import TYPE_CHECKING

from app_base.base.models.mixin import Base, UUIDMixin
from sqlalchemy import Column, DateTime, ForeignKey, String, Table, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.tasks.tasks.models import Task

# M:N Junction Table for Task-Tag associations
task_tag_associations = Table(
    "task_tag_associations",
    Base.metadata,
    Column("task_id", UUID(as_uuid=True), ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", UUID(as_uuid=True), ForeignKey("task_tags.id"), primary_key=True),
)


class TaskTag(Base, UUIDMixin):
    """Tag for classifying tasks."""

    __tablename__ = "task_tags"

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    color: Mapped[str | None] = mapped_column(String(7), nullable=True)  # #RRGGBB
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships (use string references to avoid circular imports)
    tasks: Mapped[list["Task"]] = relationship(
        "Task",
        secondary=task_tag_associations,
        back_populates="tags",
    )
