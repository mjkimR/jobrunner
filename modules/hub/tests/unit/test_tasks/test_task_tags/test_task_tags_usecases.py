from unittest.mock import AsyncMock, MagicMock

import pytest
from app.tasks.task_tags.schemas import TaskTagCreate, TaskTagRead
from app.tasks.task_tags.services import TaskTagService
from app.tasks.task_tags.usecases.crud import CreateTaskTagUseCase


@pytest.fixture
def mock_task_tag_service():
    """Fixture to provide a mocked TaskTagService."""
    service = AsyncMock(spec=TaskTagService)
    # Configure mock behavior as needed for specific test cases
    service.create.return_value = MagicMock(spec=TaskTagRead)
    return service


@pytest.mark.unit
class TestCreateTaskTagUseCase:
    async def test_create_task_tag_success(self, mock_task_tag_service):
        # Given
        use_case = CreateTaskTagUseCase(service=mock_task_tag_service)
        session = AsyncMock()  # Mock session, as it's passed to _execute
        workspace_id = "123e4567-e89b-12d3-a456-426614174000"

        task_tag_in = TaskTagCreate(name="Unit Test Tag", description="Created via unit test", color="#111222")
        context = {"parent_id": workspace_id}

        # Simulate the return value of service.create
        mock_task_tag_service.create.return_value = TaskTagRead(
            id="123e4567-e89b-12d3-a456-426614174001",
            name="Unit Test Tag",
            description="Created via unit test",
            color="#111222",
            created_at="2024-01-01T00:00:00Z",
            updated_at="2024-01-01T00:00:00Z",
        )

        # When
        result = await use_case._execute(session, task_tag_in, context=context)

        # Then
        mock_task_tag_service.create.assert_called_once_with(session, task_tag_in, context=context)
        assert result.name == "Unit Test Tag"
        assert result.description == "Created via unit test"
        assert result.color == "#111222"
