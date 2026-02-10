from app.agents.ai_model_catalogs.models import AIModelCatalog
from app.agents.ai_model_catalogs.schemas import AIModelCatalogDbCreate, AIModelCatalogDbUpdate
from app_base.base.repos.base import BaseRepository


class AIModelCatalogRepository(BaseRepository[AIModelCatalog, AIModelCatalogDbCreate, AIModelCatalogDbUpdate]):
    model = AIModelCatalog
