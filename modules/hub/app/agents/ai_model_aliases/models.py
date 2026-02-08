from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class AIModelAlias(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ai_model_aliases"
    name: Mapped[str] = mapped_column()
