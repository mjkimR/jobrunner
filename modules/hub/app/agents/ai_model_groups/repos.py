from app.agents.ai_model_groups.models import AIModelGroup
from app.agents.ai_model_groups.schemas import AIModelGroupCreate, AIModelGroupUpdate
from app_base.base.repos.base import BaseRepository


class AIModelGroupRepository(BaseRepository[AIModelGroup, AIModelGroupCreate, AIModelGroupUpdate]):
    model = AIModelGroup
