from app_base.base.models.mixin import Base, TimestampMixin, UUIDMixin
from sqlalchemy.orm import Mapped, mapped_column


class RoutingLog(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "routing_logs"
    name: Mapped[str] = mapped_column()
