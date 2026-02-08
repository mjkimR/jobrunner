from app_base.base.schemas.mixin import TimestampSchemaMixin, UUIDSchemaMixin
from pydantic import BaseModel, ConfigDict, Field


class ConversationCreate(BaseModel):
    name: str = Field(description="The name of the conversation.")


class ConversationUpdate(BaseModel):
    name: str | None = Field(default=None, description="The name of the conversation.")


class ConversationRead(UUIDSchemaMixin, TimestampSchemaMixin, BaseModel):
    name: str = Field(..., description="The name of the conversation.")
    model_config = ConfigDict(from_attributes=True)
