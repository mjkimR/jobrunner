import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from httpx import AsyncClient
from tests.utils.assertions import assert_json_contains, assert_status_code


@pytest.mark.e2e
class TestTasksAPI:
    async def test_create_task(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_in = TaskCreate(title="New Task", description="A new task description", tags=["bug", "feature"])

        response = await client.post(f"/api/v1/workspace/{workspace.id}/tasks", json=task_in.model_dump())

        assert_status_code(response, 201)
        created_task = TaskRead.model_validate(response.json())
        assert_json_contains(response, {"title": "New Task", "description": "A new task description"})
        assert len(created_task.tags) == 2
        assert created_task.tags[0].name in ["bug", "feature"]
        assert created_task.tags[1].name in ["bug", "feature"]

    async def test_get_task(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id, title="Get This Task")

        response = await client.get(f"/api/v1/workspace/{workspace.id}/tasks/{task.id}")

        assert_status_code(response, 200)
        retrieved_task = TaskRead.model_validate(response.json())
        assert retrieved_task.id == task.id
        assert retrieved_task.title == "Get This Task"

    async def test_get_task_with_tags(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        tag1: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="backend")
        tag2: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="urgent")

        task: Task = await make_db(TaskRepository, workspace_id=workspace.id, tags=[tag1, tag2])

        response = await client.get(f"/api/v1/workspace/{workspace.id}/tasks/{task.id}")

        assert_status_code(response, 200)
        retrieved_task = TaskRead.model_validate(response.json())
        assert retrieved_task.id == task.id
        assert len(retrieved_task.tags) == 2
        assert {t.name for t in retrieved_task.tags} == {"backend", "urgent"}

    async def test_get_multi_tasks(
        self,
        client: AsyncClient,
        make_db,
        make_db_batch,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        await make_db_batch(TaskRepository, 5, workspace_id=workspace.id)

        response = await client.get(f"/api/v1/workspace/{workspace.id}/tasks")

        assert_status_code(response, 200)
        assert "items" in response.json()
        assert "total_count" in response.json()
        assert len(response.json()["items"]) == 5
        assert response.json()["total_count"] == 5

    async def test_update_task(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(
            TaskRepository,
            workspace_id=workspace.id,
            title="Old Title",
            description="Old description",
        )

        update_data = TaskUpdate(title="New Title", description="New description")
        response = await client.put(
            f"/api/v1/workspace/{workspace.id}/tasks/{task.id}", json=update_data.model_dump(exclude_unset=True)
        )

        assert_status_code(response, 200)
        updated_task = TaskRead.model_validate(response.json())
        assert updated_task.title == "New Title"
        assert updated_task.description == "New description"

    async def test_update_task_with_tags(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        tag1: TaskTag = await make_db(TaskTagRepository, workspace_id=workspace.id, name="initial_tag")
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id, tags=[tag1])

        update_data = TaskUpdate(tags=["new_tag", "another_tag"])
        response = await client.put(
            f"/api/v1/workspace/{workspace.id}/tasks/{task.id}", json=update_data.model_dump(exclude_unset=True)
        )

        assert_status_code(response, 200)
        updated_task = TaskRead.model_validate(response.json())
        assert len(updated_task.tags) == 2
        assert {t.name for t in updated_task.tags} == {"new_tag", "another_tag"}

    async def test_delete_task(
        self,
        client: AsyncClient,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        response = await client.delete(f"/api/v1/workspace/{workspace.id}/tasks/{task.id}")

        assert_status_code(response, 200)
        response_json = response.json()
        assert "message" in response_json
        assert response_json["identity"] == str(task.id)

        # Verify deletion
        response = await client.get(f"/api/v1/workspace/{workspace.id}/tasks/{task.id}")
        assert_status_code(response, 404)
