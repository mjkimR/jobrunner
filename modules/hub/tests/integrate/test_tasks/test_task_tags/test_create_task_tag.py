import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.schemas import TaskTagCreate
from app.tasks.task_tags.services import TaskTagContextKwargs
from app.tasks.task_tags.usecases.crud import CreateTaskTagUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestCreateTaskTag:
    async def test_create_task_tag_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        use_case = resolve_dependency(CreateTaskTagUseCase)

        task_tag_in = TaskTagCreate(name="Integration Tag", description="Created via integration test", color="#AABBCC")
        context: TaskTagContextKwargs = {"parent_id": workspace.id}

        # Using public API .execute()
        created_task_tag = await use_case.execute(task_tag_in, context=context)

        assert created_task_tag.name == "Integration Tag"
        assert created_task_tag.description == "Created via integration test"
        assert created_task_tag.color == "#AABBCC"

        # Verify in DB
        db_task_tag = await session.get(TaskTag, created_task_tag.id)
        assert db_task_tag is not None
        assert db_task_tag.name == "Integration Tag"
        assert db_task_tag.workspace_id == workspace.id

    async def test_create_duplicate_task_tag_fails(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        use_case = resolve_dependency(CreateTaskTagUseCase)

        # Create first tag
        task_tag_in = TaskTagCreate(name="Duplicate Tag", color="#111111")
        context: TaskTagContextKwargs = {"parent_id": workspace.id}
        await use_case.execute(task_tag_in, context=context)

        # Attempt to create duplicate
        with (
            pytest.raises(Exception) as excinfo
        ):  # Catch generic exception first to see what it is, then refine if needed. AppBase usually raises specialized exceptions.
            await use_case.execute(task_tag_in, context=context)

        assert "TaskTag with this name already exists" in str(excinfo.value)
