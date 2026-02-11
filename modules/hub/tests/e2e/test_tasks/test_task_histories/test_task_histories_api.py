import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.repos import TaskHistoryRepository
from app.tasks.task_histories.schemas import TaskHistoryCreate, TaskHistoryRead
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from httpx import AsyncClient
from tests.utils.assertions import assert_json_contains, assert_status_code


@pytest.mark.e2e
class TestTaskHistoriesAPI:
    async def test_create_task_history(
        self,
        client: AsyncClient,
        make_db,
    ):
        # Create a workspace and task as parent resources
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        task_history_in = TaskHistoryCreate(
            task_id=task.id,
            event_type="status_change",
            previous_value="pending",
            new_value="in_progress",
            changed_by="test_user",
            comment="Task started",
        )

        response = await client.post(
            f"/api/v1/workspace/{workspace.id}/task_histories", json=task_history_in.model_dump()
        )

        assert_status_code(response, 201)
        created_task_history = TaskHistoryRead.model_validate(response.json())
        assert_json_contains(response, {"event_type": "status_change", "new_value": "in_progress"})
        assert created_task_history.task_id == task.id
        assert created_task_history.previous_value == "pending"
        assert created_task_history.changed_by == "test_user"

    async def test_get_task_history(
        self,
        client: AsyncClient,
        make_db,
    ):
        # Create a workspace and task
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        # Create a task history entry
        task_history: TaskHistory = await make_db(
            TaskHistoryRepository,
            workspace_id=workspace.id,
            task_id=task.id,
            event_type="assignment",
            new_value="agent_123",
            changed_by="system",
        )

        response = await client.get(f"/api/v1/workspace/{workspace.id}/task_histories/{task_history.id}")

        assert_status_code(response, 200)
        retrieved_task_history = TaskHistoryRead.model_validate(response.json())
        assert retrieved_task_history.id == task_history.id
        assert retrieved_task_history.task_id == task.id
        assert retrieved_task_history.event_type == "assignment"
        assert retrieved_task_history.new_value == "agent_123"

    async def test_get_multi_task_histories(
        self,
        client: AsyncClient,
        make_db,
        make_db_batch,
    ):
        # Create a workspace and task
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        # Create multiple task history entries for the task
        await make_db_batch(
            TaskHistoryRepository,
            5,
            workspace_id=workspace.id,
            task_id=task.id,
        )

        response = await client.get(f"/api/v1/workspace/{workspace.id}/task_histories")

        assert_status_code(response, 200)
        assert "items" in response.json()
        assert "total_count" in response.json()
        assert len(response.json()["items"]) == 5
        assert response.json()["total_count"] == 5

    async def test_update_task_history(
        self,
        client: AsyncClient,
        make_db,
    ):
        # Create a workspace and task
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        # Create a task history entry
        task_history: TaskHistory = await make_db(
            TaskHistoryRepository,
            workspace_id=workspace.id,
            task_id=task.id,
        )

        update_data = {"comment": "Updated comment"}
        response = await client.put(
            f"/api/v1/workspace/{workspace.id}/task_histories/{task_history.id}", json=update_data
        )

        assert_status_code(response, 200)
        updated_task_history = TaskHistoryRead.model_validate(response.json())
        assert updated_task_history.comment == "Updated comment"

    async def test_delete_task_history(
        self,
        client: AsyncClient,
        make_db,
    ):
        # Create a workspace and task
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)

        # Create a task history entry
        task_history: TaskHistory = await make_db(
            TaskHistoryRepository,
            workspace_id=workspace.id,
            task_id=task.id,
        )

        response = await client.delete(f"/api/v1/workspace/{workspace.id}/task_histories/{task_history.id}")

        assert_status_code(response, 200)
        response_json = response.json()
        assert "message" in response_json
        assert response_json["identity"] == str(task_history.id)

        # Verify deletion
        response = await client.get(f"/api/v1/workspace/{workspace.id}/task_histories/{task_history.id}")
        assert_status_code(response, 404)
