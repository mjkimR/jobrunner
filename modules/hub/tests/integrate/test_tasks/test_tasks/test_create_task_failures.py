import pytest
from app.tasks.tasks.schemas import TaskCreate
from app.tasks.tasks.services import TaskContextKwargs
from app.tasks.tasks.usecases.crud import CreateTaskUseCase
from app_base.base.exceptions import NotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateTaskFailures:
    async def test_create_task_invalid_workspace(
        self,
        session: AsyncSession,
        make_db,
    ):
        # Use a non-existent workspace ID
        import uuid

        random_workspace_id = uuid.uuid4()

        use_case = resolve_dependency(CreateTaskUseCase)

        task_in = TaskCreate(title="Orphan Task")
        context: TaskContextKwargs = {"parent_id": random_workspace_id}

        # Depending on implementation, this might raise NotFoundException (if workspace check exists)
        # or IntegrityError (DB constraint)
        # The service uses ExistsCheckHooksMixin usually, let's verify if Workspace existence is checked.
        # TaskService has NestedResourceHooksMixin -> repo_workspace.
        # Usually it attempts to validate parent existence if configured.

        # If the parent check is enforced by the service layer:
        with pytest.raises(NotFoundException):
            await use_case.execute(task_in, context=context)
