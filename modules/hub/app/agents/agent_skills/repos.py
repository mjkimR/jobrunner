from app.agents.agent_skills.models import AgentSkill
from app.agents.agent_skills.schemas import AgentSkillCreate, AgentSkillUpdate
from app_base.base.repos.base import BaseRepository


class AgentSkillRepository(BaseRepository[AgentSkill, AgentSkillCreate, AgentSkillUpdate]):
    model = AgentSkill
