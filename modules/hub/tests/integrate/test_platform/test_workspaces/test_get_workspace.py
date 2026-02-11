import pytest
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.usecases.crud import GetWorkspaceUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetWorkspace:
    async def test_get_workspace_by_id(self, session: AsyncSession, make_db):
        workspace = await make_db(WorkspaceRepository, name="Get Test Workspace", alias="get-test")

        use_case = resolve_dependency(GetWorkspaceUseCase)

        result = await use_case.execute(workspace.id)

        assert result is not None
        assert result.id == workspace.id
        assert result.name == "Get Test Workspace"

    async def test_get_workspace_not_found(self, session: AsyncSession):
        use_case = resolve_dependency(GetWorkspaceUseCase)

        import uuid

        random_id = uuid.uuid4()

        result = await use_case.execute(random_id)

        assert result is None
