from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentUpdate
from app_base.base.repos.base import BaseRepository


class ConfiguredAgentRepository(BaseRepository[ConfiguredAgent, ConfiguredAgentCreate, ConfiguredAgentUpdate]):
    model = ConfiguredAgent
