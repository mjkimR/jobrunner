from app.agents.agent_executions.models import AgentExecution
from app.agents.agent_executions.schemas import AgentExecutionCreate, AgentExecutionUpdate
from app_base.base.repos.base import BaseRepository


class AgentExecutionRepository(BaseRepository[AgentExecution, AgentExecutionCreate, AgentExecutionUpdate]):
    model = AgentExecution
