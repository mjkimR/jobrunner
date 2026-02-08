from app.agents.agent_mcps.models import AgentMCP
from app.agents.agent_mcps.schemas import AgentMCPCreate, AgentMCPUpdate
from app_base.base.repos.base import BaseRepository


class AgentMCPRepository(BaseRepository[AgentMCP, AgentMCPCreate, AgentMCPUpdate]):
    model = AgentMCP
