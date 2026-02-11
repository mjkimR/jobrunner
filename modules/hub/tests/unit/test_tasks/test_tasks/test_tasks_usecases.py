from unittest.mock import AsyncMock, MagicMock
from uuid import UUID

import pytest
from app.tasks.task_tags.schemas import TaskTagRead
from app.tasks.task_tags.services import TaskTagService
from app.tasks.tasks.schemas import TaskCreate, TaskDbCreate, TaskRead
from app.tasks.tasks.services import TaskService
from app.tasks.tasks.usecases.crud import CreateTaskUseCase


@pytest.fixture
def mock_task_service():
    """Fixture to provide a mocked TaskService."""
    service = AsyncMock(spec=TaskService)
    service.create.return_value = MagicMock(spec=TaskRead)
    return service


@pytest.fixture
def mock_task_tag_service():
    """Fixture to provide a mocked TaskTagService."""
    service = AsyncMock(spec=TaskTagService)
    # Simulate get_or_create_tags returning a list of TaskTagRead
    tag1 = TaskTagRead(
        id=UUID("123e4567-e89b-12d3-a456-4266141740a1"),
        name="tag1",
        created_at="2024-01-01T00:00:00Z",
        updated_at="2024-01-01T00:00:00Z",
    )
    tag2 = TaskTagRead(
        id=UUID("123e4567-e89b-12d3-a456-4266141740a2"),
        name="tag2",
        created_at="2024-01-01T00:00:00Z",
        updated_at="2024-01-01T00:00:00Z",
    )
    service.get_or_create_tags.return_value = [tag1, tag2]
    return service


@pytest.mark.unit
class TestCreateTaskUseCase:
    async def test_create_task_success(self, mock_task_service, mock_task_tag_service):
        # Given
        use_case = CreateTaskUseCase(service=mock_task_service, tag_service=mock_task_tag_service)
        session = AsyncMock()  # Mock session
        workspace_id = UUID("123e4567-e89b-12d3-a456-426614174000")

        task_in = TaskCreate(
            title="Unit Test Task",
            description="Created via unit test",
            tags=["tag1", "tag2"],
        )
        context = {"parent_id": workspace_id}

        # Simulate the return value of service.create
        mock_task_service.create.return_value = TaskRead(
            id=UUID("123e4567-e89b-12d3-a456-4266141740b0"),
            title="Unit Test Task",
            description="Created via unit test",
            status="pending",
            priority="normal",
            urgency="normal",
            complexity="simple",
            queue="default",
            source="user",
            tags=mock_task_tag_service.get_or_create_tags.return_value,  # Use the mocked tags
            created_at="2024-01-01T00:00:00Z",
            updated_at="2024-01-01T00:00:00Z",
        )

        # When
        result = await use_case._execute(session, task_in, context=context)

        # Then
        mock_task_tag_service.get_or_create_tags.assert_called_once_with(session, ["tag1", "tag2"])
        expected_db_create_data = TaskDbCreate.model_validate(task_in.model_dump(exclude={"tags"}))
        mock_task_service.create.assert_called_once()
        # Check arguments passed to mock_task_service.create
        call_args, call_kwargs = mock_task_service.create.call_args
        assert call_args[0] == session
        assert call_args[1] == expected_db_create_data
        assert call_kwargs["context"] == context
        assert len(call_kwargs["tags"]) == 2
        assert {t.name for t in call_kwargs["tags"]} == {"tag1", "tag2"}

        assert result.title == "Unit Test Task"
        assert result.description == "Created via unit test"
        assert len(result.tags) == 2
        assert {t.name for t in result.tags} == {"tag1", "tag2"}
