from app.agents.agent_skills.models import AgentSkill
from app_base.base.deps.filters.prebuilt.filter_uuid import UUIDAnyFilter

filter_ids = UUIDAnyFilter(AgentSkill, "id")
