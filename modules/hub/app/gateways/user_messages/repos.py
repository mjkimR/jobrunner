from app.gateways.user_messages.models import UserMessage
from app.gateways.user_messages.schemas import UserMessageCreate, UserMessageUpdate
from app_base.base.repos.base import BaseRepository


class UserMessageRepository(BaseRepository[UserMessage, UserMessageCreate, UserMessageUpdate]):
    model = UserMessage
