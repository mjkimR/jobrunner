import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.tasks.models import Task
from app.tasks.tasks.repos import TaskRepository
from app.tasks.tasks.services import TaskContextKwargs
from app.tasks.tasks.usecases.crud import DeleteTaskUseCase
from app_base.base.exceptions.basic import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestDeleteTask:
    async def test_delete_task_success(
        self,
        session: AsyncSession,
        inspect_session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task: Task = await make_db(TaskRepository, workspace_id=workspace.id, title="Task to delete")
        delete_use_case = resolve_dependency(DeleteTaskUseCase)

        context: TaskContextKwargs = {"parent_id": workspace.id}

        # Execute delete
        await delete_use_case.execute(task.id, context=context)

        # Verify in DB directly
        db_task = await inspect_session.get(Task, task.id)
        assert db_task is None

    async def test_delete_task_not_found(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        # Random UUID
        import uuid

        random_id = uuid.uuid4()

        delete_use_case = resolve_dependency(DeleteTaskUseCase)
        context: TaskContextKwargs = {"parent_id": workspace.id}

        # Should raise NotFoundException
        with pytest.raises(NotFoundException):
            await delete_use_case.execute(random_id, context=context)
