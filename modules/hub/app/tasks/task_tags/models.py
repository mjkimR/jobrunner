"""TaskTag Model for Hub Module.

TaskTag: Tag for classifying tasks.
TaskTagAssociation: M:N Junction Table.
DB Schema Reference: docs/specification/DB_SCHEMA.md#1.2
"""

from typing import TYPE_CHECKING
from uuid import UUID

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.platform.workspaces.models import Workspace
    from app.tasks.tasks.models import Task

# M:N Junction Table for Task-Tag associations
task_tag_associations = Table(
    "task_tag_associations",
    Base.metadata,
    Column("task_id", PG_UUID(as_uuid=True), ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", PG_UUID(as_uuid=True), ForeignKey("task_tags.id"), primary_key=True),
)


class TaskTag(Base, UUIDMixin, TimestampMixin):
    """Tag for classifying tasks."""

    __tablename__ = "task_tags"

    # Foreign keys
    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspaces.id"), nullable=False)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    color: Mapped[str | None] = mapped_column(String(7), nullable=True)  # #RRGGBB

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace")
    tasks: Mapped[list["Task"]] = relationship(
        "Task",
        secondary=task_tag_associations,
        back_populates="tags",
    )
