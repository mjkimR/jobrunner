"""Task Schemas for Hub Module.

Pydantic schemas for Task CRUD operations.
"""

import datetime
from uuid import UUID

from app.tasks.task_tags.schemas import TaskTagRead
from app.tasks.tasks.enum import (
    TaskComplexity,
    TaskPriority,
    TaskQueue,
    TaskSource,
    TaskStatus,
    TaskUrgency,
)
from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskDbCreate(BaseModel):
    """Schema for creating a new Task in the database."""

    title: str = Field(..., max_length=255, description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Task status")
    priority: TaskPriority = Field(default=TaskPriority.NORMAL, description="Priority level")
    urgency: TaskUrgency = Field(default=TaskUrgency.NORMAL, description="Urgency level (for routing)")
    complexity: TaskComplexity = Field(default=TaskComplexity.SIMPLE, description="Complexity level (for routing)")
    queue: TaskQueue = Field(default=TaskQueue.DEFAULT, description="Target queue")
    parent_task_id: UUID | None = Field(default=None, description="Parent task ID for subtasks")
    source: TaskSource = Field(default=TaskSource.USER, description="Task creation source")
    external_ref: str | None = Field(
        default=None, max_length=255, description="External reference (e.g., GitHub Issue URL)"
    )
    due_date: datetime.datetime | None = Field(default=None, description="Due date")


class TaskCreate(TaskDbCreate):
    """Schema for creating a new Task."""

    tags: list[str] = Field(default_factory=list, description="List of tag names")


class TaskDbUpdate(BaseModel):
    """Schema for updating an existing Task in the database."""

    title: str | None = Field(default=None, max_length=255, description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: TaskStatus | None = Field(default=None, description="Task status")
    priority: TaskPriority | None = Field(default=None, description="Priority level")
    urgency: TaskUrgency | None = Field(default=None, description="Urgency level")
    complexity: TaskComplexity | None = Field(default=None, description="Complexity level")
    queue: TaskQueue | None = Field(default=None, description="Target queue")
    parent_task_id: UUID | None = Field(default=None, description="Parent task ID")
    source: TaskSource | None = Field(default=None, description="Task creation source")
    external_ref: str | None = Field(default=None, max_length=255, description="External reference")
    due_date: datetime.datetime | None = Field(default=None, description="Due date")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion time")
    result_summary: str | None = Field(default=None, description="Result summary")


class TaskUpdate(TaskDbUpdate):
    """Schema for updating an existing Task."""

    tags: list[str] | None = Field(default=None, description="List of tag names")


class TaskRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    """Schema for reading Task data."""

    title: str = Field(..., description="Task title")
    description: str | None = Field(default=None, description="Task description")
    status: TaskStatus = Field(..., description="Task status")
    priority: TaskPriority = Field(..., description="Priority level")
    urgency: TaskUrgency = Field(..., description="Urgency level")
    complexity: TaskComplexity = Field(..., description="Complexity level")
    queue: TaskQueue = Field(..., description="Target queue")
    parent_task_id: UUID | None = Field(default=None, description="Parent task ID")
    source: TaskSource = Field(..., description="Task creation source")
    external_ref: str | None = Field(default=None, description="External reference")
    due_date: datetime.datetime | None = Field(default=None, description="Due date")
    completed_at: datetime.datetime | None = Field(default=None, description="Completion time")
    result_summary: str | None = Field(default=None, description="Result summary")
    tags: list[TaskTagRead] = Field(default_factory=list, description="Associated tags")

    model_config = ConfigDict(from_attributes=True)


class TaskReadWithRelations(TaskRead):
    """Schema for reading Task with related data."""

    subtasks: list[TaskRead] = Field(default_factory=list, description="Subtasks")
