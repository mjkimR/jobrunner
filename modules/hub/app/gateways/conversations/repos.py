from app.gateways.conversations.models import Conversation
from app.gateways.conversations.schemas import ConversationCreate, ConversationUpdate
from app_base.base.repos.base import BaseRepository


class ConversationRepository(BaseRepository[Conversation, ConversationCreate, ConversationUpdate]):
    model = Conversation
