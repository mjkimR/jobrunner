import pytest
from app.agents.configured_agents.repos import ConfiguredAgentRepository
from app.agents.configured_agents.usecases.crud import GetConfiguredAgentUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetConfiguredAgent:
    async def test_get_configured_agent_by_id(self, session: AsyncSession, make_db):
        agent = await make_db(ConfiguredAgentRepository, name="Get Agent", model_name="gpt-3.5-turbo")

        use_case = resolve_dependency(GetConfiguredAgentUseCase)

        result = await use_case.execute(agent.id)

        assert result is not None
        assert result.id == agent.id
        assert result.name == "Get Agent"

    async def test_get_configured_agent_not_found(self, session: AsyncSession):
        use_case = resolve_dependency(GetConfiguredAgentUseCase)

        import uuid

        random_id = uuid.uuid4()

        result = await use_case.execute(random_id)

        assert result is None
