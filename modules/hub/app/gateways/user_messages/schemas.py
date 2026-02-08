from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class UserMessageCreate(BaseModel):
    name: str = Field(description="The name of the user_message.")


class UserMessageUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the user_message.")


class UserMessageRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the user_message.")
    model_config = ConfigDict(from_attributes=True)
