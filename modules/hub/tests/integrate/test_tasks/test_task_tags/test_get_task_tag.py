import pytest
from app.platform.workspaces.models import Workspace
from app.platform.workspaces.repos import WorkspaceRepository
from app.tasks.task_tags.models import TaskTag
from app.tasks.task_tags.repos import TaskTagRepository
from app.tasks.task_tags.services import TaskTagService
from sqlalchemy.ext.asyncio import AsyncSession
from tests.utils.fastapi import resolve_dependency


@pytest.mark.integrate
class TestGetTaskTag:
    async def test_get_task_tag_success(
        self,
        session: AsyncSession,
        make_db,
    ):
        workspace: Workspace = await make_db(WorkspaceRepository, is_default=False)
        task_tag: TaskTag = await make_db(
            TaskTagRepository,
            workspace_id=workspace.id,
            name="Get Integration Tag",
            description="To be fetched",
            color="#CCDDEE",
        )

        service = resolve_dependency(TaskTagService)
        # Service can be used directly for simple GET operations
        retrieved_task_tag = await service.get(session, task_tag.id, context={"parent_id": workspace.id})

        assert retrieved_task_tag is not None
        assert retrieved_task_tag.id == task_tag.id
        assert retrieved_task_tag.name == "Get Integration Tag"
