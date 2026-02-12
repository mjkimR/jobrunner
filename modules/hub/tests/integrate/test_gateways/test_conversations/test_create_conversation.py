import pytest
from app.gateways.conversations.models import Conversation
from app.gateways.conversations.schemas import ConversationCreate
from app.gateways.conversations.usecases.crud import CreateConversationUseCase
from app.platform.workspaces.repos import WorkspaceRepository
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateConversation:
    async def test_create_conversation_success(self, session: AsyncSession, make_db):
        workspace = await make_db(WorkspaceRepository, is_default=False)

        use_case = resolve_dependency(CreateConversationUseCase)

        conversation_in = ConversationCreate(
            workspace_id=workspace.id, title="Integration Conversation", channel="web", status="active"
        )

        result = await use_case.execute(conversation_in, {"parent_id": workspace.id})

        assert result.title == "Integration Conversation"
        assert result.workspace_id == workspace.id
        assert result.id is not None

        # Verify in DB
        db_conversation = await session.get(Conversation, result.id)
        assert db_conversation is not None
        assert db_conversation.title == "Integration Conversation"
