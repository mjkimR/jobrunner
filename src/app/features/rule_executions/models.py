import uuid

from datetime import datetime
from enum import StrEnum

from sqlalchemy import DateTime, ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin


class RuleExecutionStatus(StrEnum):
    running = "running"
    success = "success"
    failure = "failure"


class RuleExecution(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "rule_executions"

    rule_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("rules.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    status: Mapped[RuleExecutionStatus] = mapped_column(Text, nullable=False)
    executed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False,
    )

    log_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    artifact_path: Mapped[str | None] = mapped_column(Text, nullable=True)

    rule = relationship("Rule", back_populates="executions")

    __table_args__ = (
        Index("ix_rule_executions_rule_id_executed_at", rule_id, executed_at),
    )
