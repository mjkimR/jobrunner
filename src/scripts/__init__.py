"""JobRunner Rule Scripts Package.

This package contains rule scripts that can be executed by the scheduler.

Auto-discovery:
    Import this module to register all rule scripts to the global registry.

Usage:
    # In your app startup or tick usecase
    import scripts  # Registers all rules

    from scripts.registry import rule_registry
    handler = rule_registry.get("hello_world")
"""

# Import registry for external access
# Auto-register all rule modules
# Add imports here as you create new rules
from scripts.hello_world import main as _hello_world  # noqa: F401
from scripts.registry import (
    ExecutionContext,
    RuleDefinition,
    RuleRegistry,
    rule,
    rule_registry,
)

__all__ = [
    "rule_registry",
    "rule",
    "RuleRegistry",
    "RuleDefinition",
    "ExecutionContext",
]
