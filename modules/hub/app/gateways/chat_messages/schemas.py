"""Chat Message Schemas for Hub Module.

Pydantic schemas for Chat Message CRUD operations.
"""

from uuid import UUID

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class ChatMessageBase(BaseModel):
    """Base schema for Chat Message."""

    conversation_id: UUID = Field(..., description="Conversation ID")
    role: str = Field(..., max_length=20, description="Role (user, assistant, system)")
    content: str = Field(..., description="Message Content")
    content_type: str = Field(default="text", max_length=50, description="Content Type")
    metadata_: dict = Field(default_factory=dict, alias="metadata", description="Metadata")
    agent_execution_id: UUID | None = Field(default=None, description="Agent Execution ID (if applicable)")


class ChatMessageCreate(ChatMessageBase):
    """Schema for creating a new Chat Message."""

    pass


class ChatMessageUpdate(BaseModel):
    """Schema for updating Chat Message."""

    content: str | None = Field(default=None, description="Message Content")
    metadata_: dict | None = Field(default=None, alias="metadata", description="Metadata")


class ChatMessageRead(UUIDSchemaMixin, TimestampSchemaMixin, ChatMessageBase):
    """Schema for reading Chat Message data."""

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
