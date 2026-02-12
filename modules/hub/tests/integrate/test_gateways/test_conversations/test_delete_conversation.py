import pytest
from app.gateways.conversations.models import Conversation
from app.gateways.conversations.repos import ConversationRepository
from app.gateways.conversations.usecases.crud import DeleteConversationUseCase
from app.platform.workspaces.repos import WorkspaceRepository
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestDeleteConversation:
    async def test_delete_conversation_success(self, session: AsyncSession, make_db, inspect_session):
        workspace = await make_db(WorkspaceRepository, is_default=False)
        conversation = await make_db(
            ConversationRepository,
            workspace_id=workspace.id,
            title="Delete Conversation",
            context={},
        )

        use_case = resolve_dependency(DeleteConversationUseCase)

        result = await use_case.execute(conversation.id, {"parent_id": workspace.id})

        assert str(result.identity) == str(conversation.id)

        # Verify in DB
        db_conversation = await inspect_session.get(Conversation, conversation.id)
        assert db_conversation is None
