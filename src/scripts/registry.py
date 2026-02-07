"""Rule script registry with decorator pattern.

Provides a declarative way to register rule scripts using decorators,
similar to FastAPI's router pattern.

Usage:
    from scripts.registry import rule_registry, rule, ExecutionContext

    @rule()
    async def hello_world(payload: dict, context: ExecutionContext | None = None) -> dict:
        name = payload.get("name", "World")
        return {"success": True, "message": f"Hello, {name}!"}

    # Get registered rule
    handler = rule_registry.get("hello_world")
    result = await handler({"name": "Test"})
"""

import asyncio
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Awaitable, Callable
from uuid import UUID


@dataclass
class ExecutionContext:
    """Context passed to rule handlers during execution.

    Contains execution metadata and results from previous steps in a chain.
    """

    execution_id: UUID
    rule_name: str
    started_at: datetime

    # Chain execution data
    chain_position: int = 0  # 0 = first in chain or standalone
    prev_results: dict[str, dict[str, Any]] = field(default_factory=dict)

    # Optional metadata
    metadata: dict[str, Any] = field(default_factory=dict)

    def get_prev_result(self, rule_name: str) -> dict[str, Any] | None:
        """Get result from a previous rule in the chain."""
        return self.prev_results.get(rule_name)


# Type alias for async rule handler (with optional context)
RuleHandler = Callable[
    [dict[str, Any], ExecutionContext | None],
    Awaitable[dict[str, Any]],
]


@dataclass
class RuleDefinition:
    """Metadata for a registered rule."""

    name: str
    handler: RuleHandler
    description: str = ""
    tags: list[str] = field(default_factory=list)
    chain_next: str | None = None  # Next rule to execute on success


class RuleRegistry:
    """Registry for rule handlers.

    Provides decorator-based registration and lookup of async rule handlers.
    Follows a singleton-like pattern for global registration.
    """

    def __init__(self):
        self._rules: dict[str, RuleDefinition] = {}

    def rule(
        self,
        name: str | None = None,
        *,
        description: str = "",
        tags: list[str] | None = None,
        chain_next: str | None = None,
    ) -> Callable[[RuleHandler], RuleHandler]:
        """Decorator to register an async rule handler.

        Args:
            name: Unique identifier for the rule. Defaults to func.__name__.
            description: Optional description. Defaults to func.__doc__.
            tags: Optional list of tags for categorization.
            chain_next: Next rule to execute on success (basic chain).

        Returns:
            Decorator function

        Raises:
            ValueError: If name is already registered or handler is not async

        Example:
            @registry.rule()  # Uses function name as rule name
            async def check_stock(payload: dict, context=None) -> dict:
                ...

            @registry.rule(chain_next="process_data")
            async def fetch_data(payload: dict, context=None) -> dict:
                ...
        """

        def decorator(func: RuleHandler) -> RuleHandler:
            # Use function name as default
            rule_name = name or func.__name__

            # Validate async function
            if not asyncio.iscoroutinefunction(func):
                raise ValueError(
                    f"Rule handler '{rule_name}' must be an async function (async def). "
                    f"Got: {type(func).__name__}"
                )

            # Check for duplicate registration
            if rule_name in self._rules:
                raise ValueError(
                    f"Rule '{rule_name}' is already registered. "
                    f"Existing: {self._rules[rule_name].handler.__module__}.{self._rules[rule_name].handler.__name__}"
                )

            # Register the rule
            self._rules[rule_name] = RuleDefinition(
                name=rule_name,
                handler=func,
                description=description or func.__doc__ or "",
                tags=tags or [],
                chain_next=chain_next,
            )

            return func

        return decorator

    def get(self, name: str) -> RuleHandler | None:
        """Get a registered rule handler by name."""
        definition = self._rules.get(name)
        return definition.handler if definition else None

    def get_definition(self, name: str) -> RuleDefinition | None:
        """Get full rule definition including metadata."""
        return self._rules.get(name)

    def list_rules(self) -> list[RuleDefinition]:
        """List all registered rules."""
        return list(self._rules.values())

    def has(self, name: str) -> bool:
        """Check if a rule is registered."""
        return name in self._rules

    def clear(self):
        """Clear all registered rules. Useful for testing."""
        self._rules.clear()


# Global registry instance
rule_registry = RuleRegistry()


# Convenience decorator using global registry
def rule(
    name: str | None = None,
    *,
    description: str = "",
    tags: list[str] | None = None,
    chain_next: str | None = None,
) -> Callable[[RuleHandler], RuleHandler]:
    """Decorator to register an async rule handler to the global registry.

    Args:
        name: Rule name. Defaults to function name (func.__name__).
        description: Description. Defaults to docstring (func.__doc__).
        tags: Optional categorization tags.
        chain_next: Next rule to trigger on success.

    Example:
        @rule()  # name='hello_world', description from docstring
        async def hello_world(payload: dict, context=None) -> dict:
            return {"success": True, "message": "Hello!"}

        @rule(chain_next="send_notification")
        async def fetch_data(payload: dict, context=None) -> dict:
            ...
    """
    return rule_registry.rule(
        name, description=description, tags=tags, chain_next=chain_next
    )
