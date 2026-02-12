import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagRead, TaskTagUpdate
from httpx import AsyncClient
from tests.utils.assertions import assert_json_contains, assert_status_code


@pytest.mark.e2e
class TestTaskTagsAPI:
    _base_url = "/api/v1/workspaces/{workspace_id}/task_tags"

    @classmethod
    def base_url(cls, workspace_id, task_tag_id=None) -> str:
        url = cls._base_url.format(workspace_id=workspace_id)
        if task_tag_id:
            url += f"/{task_tag_id}"
        return url

    async def test_create_task_tag(
        self,
        client: AsyncClient,
        make_db,
    ):
        # Create a workspace as parent resource
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)

        task_tag_in = TaskTagCreate(name="New Tag", description="A description", color="#FFFFFF")

        response = await client.post(self.base_url(workspace.id), json=task_tag_in.model_dump())

        assert_status_code(response, 201)
        created_task_tag = TaskTagRead.model_validate(response.json())
        assert_json_contains(response, {"name": "New Tag", "description": "A description"})
        assert created_task_tag.name == "New Tag"
        assert created_task_tag.color == "#FFFFFF"

    async def test_create_task_tag_duplicate_name_in_workspace(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        await make_db(
            TaskTagRepository,
            workspace_id=workspace.id,
            name="Existing Tag",
            description="Desc",
            color="#000000",
        )

        task_tag_in = TaskTagCreate(name="Existing Tag", description="Another description", color="#AAAAAA")

        response = await client.post(self.base_url(workspace.id), json=task_tag_in.model_dump())

        assert_status_code(response, 409)  # Conflict

    async def test_get_task_tag(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(
            TaskTagRepository,
            workspace_id=workspace.id,
            name="Get Tag",
            description="To be retrieved",
            color="#FF0000",
        )

        response = await client.get(self.base_url(workspace.id, task_tag.id))

        assert_status_code(response, 200)
        retrieved_task_tag = TaskTagRead.model_validate(response.json())
        assert retrieved_task_tag.id == task_tag.id
        assert retrieved_task_tag.name == "Get Tag"
        assert retrieved_task_tag.description == "To be retrieved"

    async def test_get_multi_task_tags(
        self,
        client: AsyncClient,
        make_db,
        make_db_batch,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)

        await make_db_batch(TaskTagRepository, 5, workspace_id=workspace.id)

        response = await client.get(self.base_url(workspace.id))

        assert_status_code(response, 200)
        assert "items" in response.json()
        assert "total_count" in response.json()
        assert len(response.json()["items"]) == 5
        assert response.json()["total_count"] == 5

    async def test_update_task_tag(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(
            TaskTagRepository,
            workspace_id=workspace.id,
            name="Update Me",
            description="Old description",
            color="#ABCDEF",
        )

        update_data = TaskTagUpdate(description="New description", color="#FEDCBA")
        response = await client.put(
            self.base_url(workspace.id, task_tag.id), json=update_data.model_dump(exclude_unset=True)
        )

        assert_status_code(response, 200)
        updated_task_tag = TaskTagRead.model_validate(response.json())
        assert updated_task_tag.description == "New description"
        assert updated_task_tag.color == "#FEDCBA"
        assert updated_task_tag.name == "Update Me"  # Name should not change if not provided

    async def test_delete_task_tag(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id)

        response = await client.delete(self.base_url(workspace.id, task_tag.id))

        assert_status_code(response, 200)
        response_json = response.json()
        assert "message" in response_json
        assert response_json["identity"] == str(task_tag.id)

        # Verify deletion
        response = await client.get(self.base_url(workspace.id, task_tag.id))
        assert_status_code(response, 404)
