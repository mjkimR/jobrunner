import pytest
from app.gateways.conversations.models import Conversation
from app.gateways.conversations.repos import ConversationRepository
from app.gateways.conversations.schemas import ConversationCreate, ConversationRead, ConversationUpdate
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from httpx import AsyncClient
from tests.utils.assertions import assert_status_code


@pytest.mark.e2e
class TestConversationsAPI:
    async def test_create_conversation(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)

        conversation_in = ConversationCreate(
            workspace_id=workspace.id, title="E2E Conversation", channel="slack", status="active"
        )

        response = await client.post("/api/v1/conversations", json=conversation_in.model_dump(mode="json"))

        assert_status_code(response, 201)
        created = ConversationRead.model_validate(response.json())
        assert created.title == "E2E Conversation"
        assert created.workspace_id == workspace.id

    async def test_get_conversation(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        conversation: Conversation = await make_db(
            ConversationRepository,
            workspace_id=workspace.id,
            title="Get E2E",
            context={},
        )

        response = await client.get(f"/api/v1/conversations/{conversation.id}")

        assert_status_code(response, 200)
        retrieved = ConversationRead.model_validate(response.json())
        assert retrieved.id == conversation.id

    async def test_update_conversation(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        conversation: Conversation = await make_db(
            ConversationRepository,
            workspace_id=workspace.id,
            title="Update E2E",
            context={},
        )

        update_data = ConversationUpdate(title="Updated E2E", status="closed")

        response = await client.put(
            f"/api/v1/conversations/{conversation.id}", json=update_data.model_dump(exclude_unset=True)
        )

        assert_status_code(response, 200)
        updated = ConversationRead.model_validate(response.json())
        assert updated.title == "Updated E2E"
        assert updated.status == "closed"

    async def test_delete_conversation(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        conversation: Conversation = await make_db(
            ConversationRepository,
            workspace_id=workspace.id,
            title="Delete E2E",
            context={},
        )

        response = await client.delete(f"/api/v1/conversations/{conversation.id}")

        assert_status_code(response, 200)

        # Verify 404
        get_response = await client.get(f"/api/v1/conversations/{conversation.id}")
        assert_status_code(get_response, 404)
