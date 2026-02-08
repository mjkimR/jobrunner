from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class UserMessage(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "user_messages"
    name: Mapped[str] = mapped_column()
