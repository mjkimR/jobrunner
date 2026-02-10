from app.gateways.chat_messages.models import ChatMessage
from app.gateways.chat_messages.schemas import ChatMessageCreate, ChatMessageUpdate
from app_base.base.repos.base import BaseRepository


class ChatMessageRepository(BaseRepository[ChatMessage, ChatMessageCreate, ChatMessageUpdate]):
    model = ChatMessage
