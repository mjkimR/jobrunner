"""Conversation Schemas for Hub Module.

Pydantic schemas for Conversation CRUD operations.
"""

from datetime import datetime
from uuid import UUID

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class ConversationBase(BaseModel):
    """Base schema for Conversation."""

    workspace_id: UUID = Field(..., description="Workspace ID")
    title: str | None = Field(default=None, max_length=255, description="Conversation Title")
    channel: str = Field(default="web", max_length=50, description="Chat Channel")
    status: str = Field(default="active", max_length=50, description="Conversation Status")
    context: dict = Field(default_factory=dict, description="Conversation Context")


class ConversationCreate(ConversationBase):
    """Schema for creating a new Conversation."""

    pass


class ConversationUpdate(BaseModel):
    """Schema for updating Conversation."""

    title: str | None = Field(default=None, max_length=255, description="Conversation Title")
    status: str | None = Field(default=None, max_length=50, description="Conversation Status")
    context: dict | None = Field(default=None, description="Conversation Context")
    ended_at: datetime | None = Field(default=None, description="Ended At")


class ConversationRead(UUIDSchemaMixin, TimestampSchemaMixin, ConversationBase):
    """Schema for reading Conversation data."""

    started_at: datetime = Field(..., description="Started At")
    ended_at: datetime | None = Field(default=None, description="Ended At")

    model_config = ConfigDict(from_attributes=True)
