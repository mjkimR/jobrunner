"""RoutingLog Schemas for Hub Module.

Pydantic schemas for RoutingLog CRUD operations.
"""

from uuid import UUID

from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class RoutingLogBase(BaseModel):
    """Base schema for RoutingLog."""

    message_id: UUID = Field(..., description="Message ID")
    routing_result: str = Field(..., max_length=50, description="Routing Result")
    confidence: float | None = Field(default=None, description="Confidence Score")
    reasoning: str | None = Field(default=None, description="Routing Reasoning")
    target_task_id: UUID | None = Field(default=None, description="Target Task ID")
    target_agent_id: UUID | None = Field(default=None, description="Target Agent ID")


class RoutingLogCreate(RoutingLogBase):
    """Schema for creating a new RoutingLog."""

    pass


class RoutingLogRead(UUIDSchemaMixin, TimestampSchemaMixin, RoutingLogBase):
    """Schema for reading RoutingLog data."""

    model_config = ConfigDict(from_attributes=True)
