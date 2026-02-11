import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.schemas import TaskHistoryCreate
from app.tasks.task_histories.services import TaskHistoryContextKwargs
from app.tasks.task_histories.usecases.crud import CreateTaskHistoryUseCase
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateTaskHistory:
    async def test_create_task_history_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        # Create a workspace and task as parent resources
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id)
        use_case = resolve_dependency(CreateTaskHistoryUseCase)

        task_history_in = TaskHistoryCreate(
            task_id=task.id,
            event_type="status_change",
            previous_value="pending",
            new_value="in_progress",
            changed_by="integration_test_user",
            comment="Task started during integration test",
        )

        context: TaskHistoryContextKwargs = {"parent_id": workspace.id}

        # Using public API .execute()
        created_task_history = await use_case.execute(task_history_in, context=context)

        assert created_task_history.task_id == task.id
        assert created_task_history.event_type == "status_change"
        assert created_task_history.new_value == "in_progress"
        assert created_task_history.changed_by == "integration_test_user"

        # Verify in DB
        db_task_history = await session.get(TaskHistory, created_task_history.id)
        assert db_task_history is not None
        assert db_task_history.task_id == task.id
        assert db_task_history.workspace_id == workspace.id
        assert db_task_history.comment == "Task started during integration test"
