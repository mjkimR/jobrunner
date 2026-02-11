import pytest
from app.agents.configured_agents.models import ConfiguredAgent
from app.agents.configured_agents.repos import ConfiguredAgentRepository
from app.agents.configured_agents.schemas import ConfiguredAgentCreate, ConfiguredAgentRead, ConfiguredAgentUpdate
from httpx import AsyncClient
from tests.utils.assertions import assert_status_code


@pytest.mark.e2e
class TestConfiguredAgentsAPI:
    async def test_create_configured_agent(self, client: AsyncClient):
        agent_in = ConfiguredAgentCreate(name="E2E Agent", model_name="gpt-4", description="E2E Agent Description")

        response = await client.post("/api/v1/configured_agents", json=agent_in.model_dump())

        assert_status_code(response, 201)
        created = ConfiguredAgentRead.model_validate(response.json())
        assert created.name == "E2E Agent"
        assert created.model_name == "gpt-4"

    async def test_get_configured_agent(self, client: AsyncClient, make_db):
        agent: ConfiguredAgent = await make_db(
            ConfiguredAgentRepository,
            name="Get E2E",
            model_name="gpt-3.5-turbo",
            config={},
        )

        response = await client.get(f"/api/v1/configured_agents/{agent.id}")

        assert_status_code(response, 200)
        retrieved = ConfiguredAgentRead.model_validate(response.json())
        assert retrieved.id == agent.id

    async def test_update_configured_agent(self, client: AsyncClient, make_db):
        agent: ConfiguredAgent = await make_db(
            ConfiguredAgentRepository,
            name="Update E2E",
            model_name="gpt-4",
            config={},
        )

        update_data = ConfiguredAgentUpdate(name="Updated Agent")

        response = await client.put(
            f"/api/v1/configured_agents/{agent.id}", json=update_data.model_dump(exclude_unset=True)
        )

        assert_status_code(response, 200)
        updated = ConfiguredAgentRead.model_validate(response.json())
        assert updated.name == "Updated Agent"
        assert updated.model_name == "gpt-4"

    async def test_delete_configured_agent(self, client: AsyncClient, make_db):
        agent: ConfiguredAgent = await make_db(
            ConfiguredAgentRepository,
            name="Delete E2E",
            model_name="gpt-4",
            config={},
        )

        response = await client.delete(f"/api/v1/configured_agents/{agent.id}")

        assert_status_code(response, 200)

        # Verify 404
        get_response = await client.get(f"/api/v1/configured_agents/{agent.id}")
        assert_status_code(get_response, 404)
