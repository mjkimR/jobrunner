import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.usecases.crud import DeleteWorkspaceUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestDeleteWorkspace:
    async def test_delete_workspace_success(self, session: AsyncSession, make_db, inspect_session):
        workspace = await make_db(WorkspaceRepository, is_default=False)

        use_case = resolve_dependency(DeleteWorkspaceUseCase)

        result = await use_case.execute(workspace.id)

        assert result.identity == workspace.id

        # Verify in DB using inspect_session to bypass cache
        db_workspace = await inspect_session.get(Workspace, workspace.id)
        assert db_workspace is None
