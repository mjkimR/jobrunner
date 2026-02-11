from uuid import UUID

import pytest
from app.platform.workspaces.models import Workspace
from app.tasks.task_histories.models import TaskHistory
from app.tasks.task_histories.schemas import TaskHistoryCreate
from app.tasks.task_histories.services import TaskHistoryService
from app.tasks.task_histories.usecases.crud import CreateTaskHistoryUseCase
from app.tasks.tasks.models import Task
from app.tasks.tasks.schemas import TaskCreate
from app_base.base.exceptions.basic import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestTaskHistoriesIntegration:
    async def test_create_task_history_via_use_case(
        self,
        session: AsyncSession,
        make_db,
    ):
        # Create a workspace and task as parent resources
        workspace: Workspace = await make_db(Workspace)
        task_create_data = TaskCreate(title="Integration Task", tags=[])
        task: Task = await make_db(Task, workspace_id=workspace.id, **task_create_data.model_dump(exclude={"tags"}))
        use_case = resolve_dependency(CreateTaskHistoryUseCase)

        task_history_in = TaskHistoryCreate(
            task_id=task.id,
            event_type="status_change",
            previous_value="pending",
            new_value="in_progress",
            changed_by="integration_test_user",
            comment="Task started during integration test",
        )

        context = {"parent_id": workspace.id}
        created_task_history = await use_case._execute(session, task_history_in, context=context)

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

    async def test_get_task_history_via_service(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(Workspace)
        task_create_data = TaskCreate(title="Integration Get Task", tags=[])
        task: Task = await make_db(Task, workspace_id=workspace.id, **task_create_data.model_dump(exclude={"tags"}))

        task_history: TaskHistory = await make_db(
            TaskHistory,
            workspace_id=workspace.id,
            task_id=task.id,
            event_type="assignment",
            new_value="agent_456",
            changed_by="system_integration",
        )

        service = resolve_dependency(TaskHistoryService)

        context = {"parent_id": workspace.id}
        retrieved_task_history = await service.get(session, task_history.id, context=context)

        assert retrieved_task_history is not None
        assert retrieved_task_history.id == task_history.id
        assert retrieved_task_history.event_type == "assignment"

        # Test non-existent
        with pytest.raises(NotFoundException):  # Assuming service.get raises NotFoundException for non-existent
            await service.get(session, UUID("00000000-0000-0000-0000-000000000000"), context=context)
