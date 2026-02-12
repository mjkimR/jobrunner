from typing import Annotated

from app.tasks.tasks.enum import TaskComplexity, TaskPriority, TaskStatus, TaskUrgency
from app.tasks.tasks.models import Task
from app_base.base.deps.filters.combine import create_combined_filter_dependency
from app_base.base.deps.filters.prebuilt.filter_string import EnumFilter, StringILikeFilter
from fastapi import Depends

filter_title = StringILikeFilter(Task, "title")
filter_status = EnumFilter(Task, "status", enum_type=TaskStatus)
filter_priority = EnumFilter(Task, "priority", enum_type=TaskPriority)
filter_urgency = EnumFilter(Task, "urgency", enum_type=TaskUrgency)
filter_complexity = EnumFilter(Task, "complexity", enum_type=TaskComplexity)

TaskFilterDepend = Annotated[
    ...,
    Depends(
        create_combined_filter_dependency(
            filter_title, filter_status, filter_priority, filter_urgency, filter_complexity
        )
    ),
]
