"""Task Schemas for Hub Module.

Pydantic schemas for Task CRUD operations.
"""

import datetime
import uuid
from typing import Literal

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Schema for creating a new Task."""

    title: str = Field(..., max_length=255, description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: Literal["pending", "in_progress", "review", "done", "cancelled"] = Field(
        default="pending", description="Task status"
    )
    priority: Literal["low", "normal", "high", "critical"] = Field(default="normal", description="Priority level")
    urgency: Literal["low", "normal", "high", "critical"] = Field(
        default="normal", description="Urgency level (for routing)"
    )
    complexity: Literal["simple", "moderate", "complex"] = Field(
        default="simple", description="Complexity level (for routing)"
    )
    queue: str = Field(default="default", max_length=100, description="Target queue")
    parent_task_id: uuid.UUID | None = Field(default=None, description="Parent task ID for subtasks")
    source: Literal["user", "host_agent", "gateway", "workflow", "system"] = Field(
        default="user", description="Task creation source"
    )
    external_ref: str | None = Field(
        default=None, max_length=255, description="External reference (e.g., GitHub Issue URL)"
    )
    due_date: datetime.datetime | None = Field(default=None, description="Due date")
    tag_ids: list[uuid.UUID] | None = Field(default=None, description="Tag IDs to associate")


class TaskUpdate(BaseModel):
    """Schema for updating an existing Task."""

    title: str | None = Field(default=None, max_length=255, description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: Literal["pending", "in_progress", "review", "done", "cancelled"] | None = Field(
        default=None, description="Task status"
    )
    priority: Literal["low", "normal", "high", "critical"] | None = Field(default=None, description="Priority level")
    urgency: Literal["low", "normal", "high", "critical"] | None = Field(default=None, description="Urgency level")
    complexity: Literal["simple", "moderate", "complex"] | None = Field(default=None, description="Complexity level")
    queue: str | None = Field(default=None, max_length=100, description="Target queue")
    parent_task_id: uuid.UUID | None = Field(default=None, description="Parent task ID")
    source: Literal["user", "host_agent", "gateway", "workflow", "system"] | None = Field(
        default=None, description="Task creation source"
    )
    external_ref: str | None = Field(default=None, max_length=255, description="External reference")
    due_date: datetime.datetime | None = Field(default=None, description="Due date")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion time")
    result_summary: str | None = Field(default=None, description="Result summary")
    tag_ids: list[uuid.UUID] | None = Field(default=None, description="Tag IDs to update")


class TaskRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    """Schema for reading Task data."""

    title: str = Field(..., description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: str = Field(..., description="Task status")
    priority: str = Field(..., description="Priority level")
    urgency: str = Field(..., description="Urgency level")
    complexity: str = Field(..., description="Complexity level")
    queue: str = Field(..., description="Target queue")
    parent_task_id: uuid.UUID | None = Field(default=None, description="Parent task ID")
    source: str = Field(..., description="Task creation source")
    external_ref: str | None = Field(default=None, description="External reference")
    due_date: datetime.datetime | None = Field(default=None, description="Due date")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion time")
    result_summary: str | None = Field(default=None, description="Result summary")

    model_config = ConfigDict(from_attributes=True)


class TaskReadWithRelations(TaskRead):
    """Schema for reading Task with related data."""

    subtasks: list[TaskRead] = Field(default_factory=list, description="Subtasks")
    tags: list["TaskTagRead"] = Field(default_factory=list, description="Associated tags")


# Forward reference
from app.tasks.task_tags.schemas import TaskTagRead  # noqa: E402, F401

TaskReadWithRelations.model_rebuild()
