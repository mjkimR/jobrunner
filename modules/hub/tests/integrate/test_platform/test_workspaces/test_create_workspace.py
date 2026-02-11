import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.schemas import WorkspaceCreate
from app.platform.workspaces.usecases.crud import CreateWorkspaceUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateWorkspace:
    async def test_create_workspace_success(self, session: AsyncSession):
        use_case = resolve_dependency(CreateWorkspaceUseCase)

        workspace_in = WorkspaceCreate(
            name="Integration Test Workspace",
            alias="integration-test-workspace",
            description="Created via integration test",
        )

        result = await use_case.execute(workspace_in)

        assert result.name == "Integration Test Workspace"
        assert result.alias == "integration-test-workspace"
        assert result.description == "Created via integration test"
        assert result.id is not None

        # Verify in DB
        db_workspace = await session.get(Workspace, result.id)
        assert db_workspace is not None
        assert db_workspace.name == "Integration Test Workspace"

    async def test_create_workspace_duplicate_alias(self, session: AsyncSession, make_db):
        # Create existing workspace
        await make_db(WorkspaceRepository, alias="duplicate-alias", name="Original Workspace")

        use_case = resolve_dependency(CreateWorkspaceUseCase)
        workspace_in = WorkspaceCreate(
            name="New Workspace",
            alias="duplicate-alias",
        )

        from app_base.base.exceptions.basic import BadRequestException

        with pytest.raises(BadRequestException):
            await use_case.execute(workspace_in)

    async def test_create_workspace_duplicate_name(self, session: AsyncSession, make_db):
        # Create existing workspace
        await make_db(WorkspaceRepository, alias="unique-alias", name="Duplicate Name")

        use_case = resolve_dependency(CreateWorkspaceUseCase)
        workspace_in = WorkspaceCreate(
            name="Duplicate Name",
            alias="new-alias",
        )

        from app_base.base.exceptions.basic import BadRequestException

        with pytest.raises(BadRequestException):
            await use_case.execute(workspace_in)
