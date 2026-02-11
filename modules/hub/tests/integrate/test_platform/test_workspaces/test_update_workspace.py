import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.schemas import WorkspaceUpdate
from app.platform.workspaces.usecases.crud import UpdateWorkspaceUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestUpdateWorkspace:
    async def test_update_workspace_success(self, session: AsyncSession, make_db, inspect_session):
        workspace = await make_db(WorkspaceRepository, name="Old Name", alias="old-alias")

        use_case = resolve_dependency(UpdateWorkspaceUseCase)
        update_data = WorkspaceUpdate(name="New Name", description="Updated description")

        result = await use_case.execute(workspace.id, update_data)

        assert result is not None
        assert result.name == "New Name"
        assert result.alias == "old-alias"  # Should remain unchanged
        assert result.description == "Updated description"

        # Verify in DB using inspect_session to bypass cache
        db_workspace = await inspect_session.get(Workspace, result.id)
        assert db_workspace.name == "New Name"

    async def test_update_workspace_not_found(self, session: AsyncSession):
        use_case = resolve_dependency(UpdateWorkspaceUseCase)
        update_data = WorkspaceUpdate(name="New Name")

        import uuid

        random_id = uuid.uuid4()

        from app_base.base.exceptions.basic import NotFoundException

        with pytest.raises(NotFoundException):
            await use_case.execute(random_id, update_data)
