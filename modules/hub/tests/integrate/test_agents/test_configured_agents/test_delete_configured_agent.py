import pytest
from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.repos import ConfiguredAgentRepository
from app.agents.configured_agents.usecases.crud import DeleteConfiguredAgentUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestDeleteConfiguredAgent:
    async def test_delete_configured_agent_success(self, session: AsyncSession, make_db, inspect_session):
        agent = await make_db(
            ConfiguredAgentRepository,
            name="Delete Agent",
            model_name="gpt-4",
            config={},
        )
        use_case = resolve_dependency(DeleteConfiguredAgentUseCase)

        result = await use_case.execute(agent.id)

        assert str(result.identity) == str(agent.id)

        # Verify in DB
        db_agent = await inspect_session.get(ConfiguredAgent, agent.id)
        assert db_agent is None
