from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class AgentExecution(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "agent_executions"
    name: Mapped[str] = mapped_column()
