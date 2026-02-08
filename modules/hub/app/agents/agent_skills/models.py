from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class AgentSkill(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "agent_skills"
    name: Mapped[str] = mapped_column()
