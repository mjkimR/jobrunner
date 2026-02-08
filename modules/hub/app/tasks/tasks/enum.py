import enum


class TaskStatus(str, enum.Enum):
    """Task progress status."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    DONE = "done"
    CANCELLED = "cancelled"


class TaskPriority(str, enum.Enum):
    """Priority level."""

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class TaskUrgency(str, enum.Enum):
    """Urgency level (used for routing decisions)."""

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class TaskComplexity(str, enum.Enum):
    """Complexity level (used for routing decisions)."""

    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"


class TaskQueue(str, enum.Enum):
    """Target processing queue (for Dagster sensor polling)."""

    DEFAULT = "default"
    HOST_AGENT = "host-agent"
    LOCAL_AGENT = "local-agent"
    WORKFLOW = "workflow"


class TaskSource(str, enum.Enum):
    """Source of task creation."""

    USER = "user"
    HOST_AGENT = "host_agent"
    GATEWAY = "gateway"
    WORKFLOW = "workflow"
    SYSTEM = "system"
