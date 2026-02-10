"""TaskHistory Schemas for Hub Module.

Pydantic schemas for TaskHistory CRUD operations.
"""

import datetime
from typing import Literal
from uuid import UUID

from app_base.base.schemas.mixin import UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class TaskHistoryCreate(BaseModel):
    """Schema for creating a new TaskHistory entry."""

    task_id: UUID = Field(..., description="Associated task ID")
    event_type: Literal["status_change", "assignment", "queue_change", "priority_change"] = Field(
        ..., description="Type of history event"
    )
    previous_value: str | None = Field(default=None, max_length=100, description="Previous value")
    new_value: str = Field(..., max_length=100, description="New value")
    assigned_agent_id: UUID | None = Field(default=None, description="Assigned agent ID (for assignment events)")
    changed_by: str = Field(..., max_length=100, description="Who made the change")
    comment: str | None = Field(default=None, description="Optional comment")


class TaskHistoryUpdate(BaseModel):
    """Schema for updating TaskHistory (limited - history is mostly immutable)."""

    comment: str | None = Field(default=None, description="Update comment only")


class TaskHistoryRead(UUIDSchemaMixin, BaseModel):
    """Schema for reading TaskHistory data."""

    task_id: UUID = Field(..., description="Associated task ID")
    event_type: str = Field(..., description="Type of history event")
    previous_value: str | None = Field(default=None, description="Previous value")
    new_value: str = Field(..., description="New value")
    assigned_agent_id: UUID | None = Field(default=None, description="Assigned agent ID")
    changed_by: str = Field(..., description="Who made the change")
    comment: str | None = Field(default=None, description="Optional comment")
    created_at: datetime.datetime = Field(..., description="Event timestamp")

    model_config = ConfigDict(from_attributes=True)
