from app.agents.ai_models.models import AIModel
from app.agents.ai_models.schemas import AIModelCreate, AIModelUpdate
from app_base.base.repos.base import BaseRepository


class AIModelRepository(BaseRepository[AIModel, AIModelCreate, AIModelUpdate]):
    model = AIModel
