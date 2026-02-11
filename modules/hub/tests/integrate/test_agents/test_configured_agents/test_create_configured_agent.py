import pytest
from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.schemas import ConfiguredAgentCreate
from app.agents.configured_agents.usecases.crud import CreateConfiguredAgentUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateConfiguredAgent:
    async def test_create_configured_agent_success(self, session: AsyncSession):
        use_case = resolve_dependency(CreateConfiguredAgentUseCase)

        agent_in = ConfiguredAgentCreate(
            name="Integration Agent", model_name="gpt-4", description="Integration test agent"
        )

        result = await use_case.execute(agent_in)

        assert result.name == "Integration Agent"
        assert result.model_name == "gpt-4"
        assert result.id is not None

        # Verify in DB
        db_agent = await session.get(ConfiguredAgent, result.id)
        assert db_agent is not None
        assert db_agent.name == "Integration Agent"
