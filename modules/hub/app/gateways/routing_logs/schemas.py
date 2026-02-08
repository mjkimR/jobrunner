from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class RoutingLogCreate(BaseModel):
    name: str = Field(description="The name of the routing_log.")


class RoutingLogUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the routing_log.")


class RoutingLogRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the routing_log.")
    model_config = ConfigDict(from_attributes=True)
