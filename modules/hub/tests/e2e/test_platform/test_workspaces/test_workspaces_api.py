import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.platform.workspaces.schemas import WorkspaceCreate, WorkspaceRead, WorkspaceUpdate
from httpx import AsyncClient
from tests.utils.assertions import assert_status_code


@pytest.mark.e2e
class TestWorkspacesAPI:
    _base_url = "/api/v1/workspaces"

    @classmethod
    def base_url(cls, workspace_id=None) -> str:
        url = cls._base_url
        if workspace_id:
            url += f"/{workspace_id}"
        return url

    async def test_create_workspace(self, client: AsyncClient):
        workspace_in = WorkspaceCreate(
            name="E2E Workspace",
            alias="e2e-workspace",
            description="Created via E2E test",
        )

        response = await client.post(self.base_url(), json=workspace_in.model_dump())

        assert_status_code(response, 201)
        created_workspace = WorkspaceRead.model_validate(response.json())
        assert created_workspace.name == "E2E Workspace"
        assert created_workspace.alias == "e2e-workspace"
        assert created_workspace.description == "Created via E2E test"
        assert created_workspace.id is not None

    async def test_get_workspace(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(
            WorkspaceRepository, name="Get E2E", alias="get-e2e", description="To be retrieved"
        )

        response = await client.get(self.base_url(workspace.id))

        assert_status_code(response, 200)
        retrieved = WorkspaceRead.model_validate(response.json())
        assert retrieved.id == workspace.id
        assert retrieved.name == "Get E2E"

    async def test_update_workspace(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(WorkspaceRepository, name="Update E2E", alias="update-e2e")

        update_data = WorkspaceUpdate(name="Updated E2E")

        response = await client.put(self.base_url(workspace.id), json=update_data.model_dump(exclude_unset=True))

        assert_status_code(response, 200)
        updated = WorkspaceRead.model_validate(response.json())
        assert updated.name == "Updated E2E"
        assert updated.alias == "update-e2e"

    async def test_delete_workspace(self, client: AsyncClient, make_db):
        workspace: Workspace = await make_db(
            WorkspaceRepository, name="Delete E2E", alias="delete-e2e", is_default=False
        )

        response = await client.delete(self.base_url(workspace.id))

        assert_status_code(response, 200)
        response_json = response.json()
        assert response_json["identity"] == str(workspace.id)

        # Verify 404
        get_response = await client.get(self.base_url(workspace.id))
        assert_status_code(get_response, 404)

    async def test_get_workspaces_list(self, client: AsyncClient, make_db, make_db_batch):
        # Create some workspaces
        await make_db(WorkspaceRepository, name="List 1", alias="list-1")
        await make_db(WorkspaceRepository, name="List 2", alias="list-2")

        # There might be other workspaces from other tests or default one, so we just check if we get list back
        response = await client.get(self.base_url())

        assert_status_code(response, 200)
        data = response.json()
        assert "items" in data
        assert "total_count" in data
        assert len(data["items"]) >= 2
