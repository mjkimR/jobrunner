import pytest
from app.gateways.conversations.repos import ConversationRepository
from app.gateways.conversations.usecases.crud import GetConversationUseCase
from app.platform.workspaces.repos import WorkspaceRepository
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetConversation:
    async def test_get_conversation_by_id(self, session: AsyncSession, make_db):
        workspace = await make_db(WorkspaceRepository, is_default=False)
        conversation = await make_db(
            ConversationRepository,
            workspace_id=workspace.id,
            title="Get Conversation",
            context={},
        )

        use_case = resolve_dependency(GetConversationUseCase)

        result = await use_case.execute(conversation.id, {"parent_id": workspace.id})

        assert result is not None
        assert result.id == conversation.id
        assert result.title == "Get Conversation"

    async def test_get_conversation_not_found(self, session: AsyncSession):
        use_case = resolve_dependency(GetConversationUseCase)

        import uuid

        random_id = uuid.uuid4()

        result = await use_case.execute(random_id, {"parent_id": uuid.uuid4()})

        assert result is None
