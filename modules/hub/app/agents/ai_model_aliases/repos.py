from app.agents.ai_model_aliases.models import AIModelAlias
from app.agents.ai_model_aliases.schemas import AIModelAliasCreate, AIModelAliasUpdate
from app_base.base.repos.base import BaseRepository


class AIModelAliasRepository(BaseRepository[AIModelAlias, AIModelAliasCreate, AIModelAliasUpdate]):
    model = AIModelAlias
