import enum


class AgentType(str, enum.Enum):
    """Agent type enum."""

    CONFIGURED = "configured"
    GRAPH = "graph"


class AgentExecutionType(str, enum.Enum):
    """Agent Execution type enum."""

    TASK_PROCESSING = "task_processing"
    ROUTING_DECISION = "routing_decision"
    CHAT_RESPONSE = "chat_response"
    WORKFLOW_STEP = "workflow_step"


class AgentExecutionStatus(str, enum.Enum):
    """Agent Execution status enum."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMEOUT = "timeout"
