from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class Conversation(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "conversations"
    name: Mapped[str] = mapped_column()
