from app.agents.agent_mcps.models import AgentMCP
from app_base.base.deps.filters.prebuilt.filter_uuid import UUIDAnyFilter

filter_ids = UUIDAnyFilter(AgentMCP, "id")
