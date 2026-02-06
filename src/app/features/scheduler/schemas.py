from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TickRequest(BaseModel):
    now: datetime | None = Field(
        default=None, description="Override current time (timezone-aware)."
    )
    limit: int = Field(
        default=100, ge=1, le=1000, description="Max number of rules to process."
    )


class TickResponse(BaseModel):
    processed: int = Field(description="Number of rules attempted.")
    succeeded: int = Field(description="Number of rules executed successfully.")
    failed: int = Field(description="Number of rules that failed.")

    execution_ids: list[str] = Field(
        default_factory=list, description="Created execution ids."
    )

    model_config = ConfigDict(from_attributes=True)
