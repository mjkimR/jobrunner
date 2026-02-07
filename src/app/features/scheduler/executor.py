"""Rule script executor with registry support and chain execution.

Supports:
1. Registry-based: Looks up handlers from RuleRegistry (preferred)
2. File-based: Dynamically loads scripts from filesystem (legacy fallback)
3. Chain execution: Executes a sequence of rules with context passing
"""

import importlib.util
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import UUID, uuid4

from app_base.core.log import logger


@dataclass
class ExecutionResult:
    """Result of a rule script execution."""

    success: bool
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


@dataclass
class RuleExecutor:
    """Executor that runs rule scripts.

    Supports both registry-based and file-based execution modes.
    Registry-based is preferred for production use.
    """

    scripts_base_path: Path | None = None

    def __post_init__(self):
        if isinstance(self.scripts_base_path, str):
            self.scripts_base_path = Path(self.scripts_base_path)

    async def execute(
        self,
        script_path: str,
        payload: dict[str, Any],
        context: "ExecutionContext | None" = None,
    ) -> ExecutionResult:
        """Execute a rule script.

        First attempts registry lookup, then falls back to file-based loading.

        Args:
            script_path: Rule name (for registry) or relative path to script
                         (e.g., "hello_world" or "hello_world/main.py")
            payload: Data to pass to the handler
            context: Execution context with chain data

        Returns:
            ExecutionResult with success status and any returned data
        """
        # Import registry here to avoid circular imports
        from scripts.registry import ExecutionContext, rule_registry

        # Normalize script_path to rule name
        rule_name = self._extract_rule_name(script_path)

        # Try registry first
        handler = rule_registry.get(rule_name)
        if handler:
            # Create context if not provided
            if context is None:
                context = ExecutionContext(
                    execution_id=uuid4(),
                    rule_name=rule_name,
                    started_at=datetime.now(timezone.utc),
                )
            return await self._execute_handler(rule_name, handler, payload, context)

        # Fallback: try to load and register from file
        if self.scripts_base_path:
            return await self._execute_from_file(script_path, payload, context)

        error_msg = f"Rule '{rule_name}' not found in registry"
        logger.error(error_msg)
        return ExecutionResult(success=False, error=error_msg)

    async def execute_chain(
        self,
        rules: list[str],
        initial_payload: dict[str, Any],
        execution_id: UUID | None = None,
    ) -> list[ExecutionResult]:
        """Execute a chain of rules sequentially, passing context between them.

        Args:
            rules: List of rule names to execute in order
            initial_payload: Payload for the first rule
            execution_id: Optional shared execution ID for the chain

        Returns:
            List of ExecutionResults, one per rule
        """
        from scripts.registry import ExecutionContext

        results: list[ExecutionResult] = []
        prev_results: dict[str, dict[str, Any]] = {}
        execution_id = execution_id or uuid4()
        started_at = datetime.now(timezone.utc)

        for i, rule_name in enumerate(rules):
            # Build context with previous results
            context = ExecutionContext(
                execution_id=execution_id,
                rule_name=rule_name,
                started_at=started_at,
                chain_position=i,
                prev_results=prev_results.copy(),
            )

            # Use initial payload or empty dict
            payload = initial_payload if i == 0 else {}

            result = await self.execute(rule_name, payload, context)
            results.append(result)

            # Store result for next step
            prev_results[rule_name] = {
                "success": result.success,
                "message": result.message,
                **result.data,
            }

            # Stop chain on failure
            if not result.success:
                logger.warning(f"Chain stopped at '{rule_name}': {result.error}")
                break

        return results

    def _extract_rule_name(self, script_path: str) -> str:
        """Extract rule name from script path.

        Examples:
            "hello_world" -> "hello_world"
            "hello_world/main.py" -> "hello_world"
            "stock/check_price.py" -> "stock/check_price"
        """
        # Remove .py extension
        if script_path.endswith(".py"):
            script_path = script_path[:-3]

        # Remove /main suffix (convention for directory-based scripts)
        if script_path.endswith("/main"):
            script_path = script_path[:-5]

        return script_path

    async def _execute_handler(
        self,
        rule_name: str,
        handler,
        payload: dict[str, Any],
        context: "ExecutionContext",
    ) -> ExecutionResult:
        """Execute a registered handler."""
        try:
            logger.info(f"Executing rule: {rule_name}")
            result = await handler(payload, context)

            # Validate result format
            if not isinstance(result, dict):
                error_msg = f"Rule returned non-dict result: {type(result)}"
                logger.error(error_msg)
                return ExecutionResult(success=False, error=error_msg)

            success = result.get("success", False)
            message = result.get("message", "")
            data = {k: v for k, v in result.items() if k not in ("success", "message")}

            logger.info(f"Rule completed: {rule_name}, success={success}")
            return ExecutionResult(success=success, message=message, data=data)

        except Exception as e:
            error_msg = f"Rule execution failed: {e}"
            logger.exception(error_msg)
            return ExecutionResult(success=False, error=error_msg)

    async def _execute_from_file(
        self,
        script_path: str,
        payload: dict[str, Any],
        context: "ExecutionContext | None",
    ) -> ExecutionResult:
        """Fallback: Load and execute from filesystem.

        This also registers the script to the registry for future calls.
        """
        from scripts.registry import ExecutionContext

        if self.scripts_base_path is None:
            return ExecutionResult(
                success=False, error="scripts_base_path not configured"
            )

        full_path = self.scripts_base_path / script_path

        if not full_path.exists():
            error_msg = f"Script not found: {full_path}"
            logger.error(error_msg)
            return ExecutionResult(success=False, error=error_msg)

        if not full_path.suffix == ".py":
            error_msg = f"Invalid script extension (must be .py): {full_path}"
            logger.error(error_msg)
            return ExecutionResult(success=False, error=error_msg)

        try:
            # Load the module (this triggers @rule decorator registration)
            self._load_module(full_path)

            # Now try registry again
            from scripts.registry import rule_registry

            rule_name = self._extract_rule_name(script_path)
            handler = rule_registry.get(rule_name)

            if handler:
                if context is None:
                    context = ExecutionContext(
                        execution_id=uuid4(),
                        rule_name=rule_name,
                        started_at=datetime.now(timezone.utc),
                    )
                return await self._execute_handler(rule_name, handler, payload, context)

            # If still not found, the script doesn't use @rule decorator
            error_msg = (
                f"Script '{script_path}' loaded but no @rule decorator found. "
                f"Please use @rule('{rule_name}') decorator."
            )
            logger.error(error_msg)
            return ExecutionResult(success=False, error=error_msg)

        except Exception as e:
            error_msg = f"Script loading failed: {e}"
            logger.exception(error_msg)
            return ExecutionResult(success=False, error=error_msg)

    def _load_module(self, path: Path):
        """Dynamically load a Python module from path."""
        module_name = f"rule_script_{path.stem}_{id(path)}"

        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load module spec from {path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        return module


# Re-export ExecutionContext for convenience
from scripts.registry import ExecutionContext  # noqa: E402

__all__ = ["RuleExecutor", "ExecutionResult", "ExecutionContext"]
