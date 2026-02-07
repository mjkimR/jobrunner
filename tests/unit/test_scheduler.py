"""Unit tests for RuleExecutor and schedule utilities."""

from datetime import datetime, timezone

import pytest

from app.features.scheduler.executor import RuleExecutor
from app.features.scheduler.schedule import calculate_next_run, is_valid_cron

# ==================== Schedule Calculator Tests ====================


class TestCalculateNextRun:
    """Tests for calculate_next_run function."""

    def test_every_5_minutes(self):
        """Every 5 minutes cron expression."""
        base = datetime(2026, 2, 7, 10, 0, 0, tzinfo=timezone.utc)
        result = calculate_next_run("*/5 * * * *", base)

        assert result > base
        assert result.minute == 5  # Next 5-minute mark
        assert result.tzinfo is not None

    def test_every_hour(self):
        """Every hour at minute 0."""
        base = datetime(2026, 2, 7, 10, 30, 0, tzinfo=timezone.utc)
        result = calculate_next_run("0 * * * *", base)

        assert result.hour == 11
        assert result.minute == 0

    def test_daily_at_noon(self):
        """Every day at noon."""
        base = datetime(2026, 2, 7, 13, 0, 0, tzinfo=timezone.utc)  # After noon
        result = calculate_next_run("0 12 * * *", base)

        assert result.day == 8  # Next day
        assert result.hour == 12
        assert result.minute == 0

    def test_result_is_timezone_aware(self):
        """Result should always have timezone info."""
        base = datetime(2026, 2, 7, 10, 0, 0, tzinfo=timezone.utc)
        result = calculate_next_run("*/5 * * * *", base)

        assert result.tzinfo is not None

    def test_invalid_cron_raises_error(self):
        """Invalid cron expression should raise ValueError."""
        with pytest.raises((ValueError, KeyError)):
            calculate_next_run("invalid cron", datetime.now(timezone.utc))


class TestIsValidCron:
    """Tests for is_valid_cron function."""

    def test_valid_expressions(self):
        """Valid cron expressions."""
        assert is_valid_cron("*/5 * * * *") is True
        assert is_valid_cron("0 12 * * *") is True
        assert is_valid_cron("0 0 1 * *") is True

    def test_invalid_expressions(self):
        """Invalid cron expressions."""
        assert is_valid_cron("not a cron") is False
        assert is_valid_cron("") is False


# ==================== RuleExecutor Tests (with Registry) ====================


class TestRuleExecutorWithRegistry:
    """Tests for RuleExecutor using registry pattern."""

    @pytest.fixture(autouse=True)
    def setup_registry(self):
        """Setup and teardown registry for each test."""
        from scripts.registry import rule_registry

        rule_registry.clear()
        yield
        rule_registry.clear()

    @pytest.fixture
    def executor(self) -> RuleExecutor:
        """Create a RuleExecutor instance."""
        return RuleExecutor()

    @pytest.mark.asyncio
    async def test_execute_registered_rule(self, executor: RuleExecutor):
        """Execute a registered async rule."""
        from scripts.registry import rule

        @rule("test_rule")
        async def test_handler(payload: dict, context=None) -> dict:
            return {"success": True, "message": f"Got: {payload.get('key')}"}

        result = await executor.execute("test_rule", {"key": "value"})

        assert result.success is True
        assert "Got: value" in result.message

    @pytest.mark.asyncio
    async def test_execute_rule_not_found(self, executor: RuleExecutor):
        """Handle missing rule gracefully."""
        result = await executor.execute("nonexistent_rule", {})

        assert result.success is False
        assert result.error is not None
        assert "not found" in result.error.lower()

    @pytest.mark.asyncio
    async def test_execute_rule_with_exception(self, executor: RuleExecutor):
        """Handle rule that raises an exception."""
        from scripts.registry import rule

        @rule("error_rule")
        async def error_handler(payload: dict, context=None) -> dict:
            raise ValueError("Intentional error")

        result = await executor.execute("error_rule", {})

        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_execute_rule_returns_failure(self, executor: RuleExecutor):
        """Rule returns success=False."""
        from scripts.registry import rule

        @rule("fail_rule")
        async def fail_handler(payload: dict, context=None) -> dict:
            return {"success": False, "message": "Validation failed"}

        result = await executor.execute("fail_rule", {})

        assert result.success is False
        assert "Validation failed" in result.message

    @pytest.mark.asyncio
    async def test_path_normalization(self, executor: RuleExecutor):
        """Test script path to rule name normalization."""
        from scripts.registry import rule

        @rule("my_rule")
        async def my_handler(payload: dict, context=None) -> dict:
            return {"success": True}

        # All these should resolve to "my_rule"
        result1 = await executor.execute("my_rule", {})
        result2 = await executor.execute("my_rule/main.py", {})
        result3 = await executor.execute("my_rule.py", {})

        assert result1.success is True
        assert result2.success is True
        assert result3.success is True


# ==================== Registry Tests ====================


class TestRuleRegistry:
    """Tests for RuleRegistry."""

    @pytest.fixture(autouse=True)
    def setup_registry(self):
        """Setup and teardown registry for each test."""
        from scripts.registry import rule_registry

        rule_registry.clear()
        yield
        rule_registry.clear()

    def test_sync_function_rejected(self):
        """Sync functions should be rejected."""
        from scripts.registry import rule

        with pytest.raises(ValueError, match="async function"):

            @rule("sync_rule")  # type: ignore
            def sync_handler(payload: dict, context=None) -> dict:
                return {"success": True}

    def test_duplicate_registration_rejected(self):
        """Duplicate rule names should be rejected."""
        from scripts.registry import rule

        @rule("duplicate_rule")
        async def first_handler(payload: dict, context=None) -> dict:
            return {"success": True}

        with pytest.raises(ValueError, match="already registered"):

            @rule("duplicate_rule")
            async def second_handler(payload: dict, context=None) -> dict:
                return {"success": True}

    def test_list_rules(self):
        """List all registered rules."""
        from scripts.registry import rule, rule_registry

        @rule("rule1", tags=["a"])
        async def handler1(payload: dict, context=None) -> dict:
            return {"success": True}

        @rule("rule2", tags=["b"])
        async def handler2(payload: dict, context=None) -> dict:
            return {"success": True}

        rules = rule_registry.list_rules()
        assert len(rules) == 2
        assert {r.name for r in rules} == {"rule1", "rule2"}


# ==================== Chain Tests ====================


class TestRuleChain:
    """Tests for chain execution."""

    @pytest.fixture(autouse=True)
    def setup_registry(self):
        """Setup and teardown registry for each test."""
        from scripts.registry import rule_registry

        rule_registry.clear()
        yield
        rule_registry.clear()

    @pytest.mark.asyncio
    async def test_execute_chain_passes_context(self):
        """Chain passes prev_results in context."""
        from scripts.registry import rule

        @rule("step_a")
        async def step_a(payload: dict, context=None) -> dict:
            return {"success": True, "value": 10}

        @rule("step_b")
        async def step_b(payload: dict, context=None) -> dict:
            prev = context.get_prev_result("step_a") if context else None
            value = prev.get("value", 0) if prev else 0
            return {"success": True, "result": value * 2}

        executor = RuleExecutor()
        results = await executor.execute_chain(["step_a", "step_b"], {})

        assert len(results) == 2
        assert results[0].success is True
        assert results[0].data.get("value") == 10
        assert results[1].success is True
        assert results[1].data.get("result") == 20

    @pytest.mark.asyncio
    async def test_chain_stops_on_failure(self):
        """Chain stops when a rule fails."""
        from scripts.registry import rule

        @rule("fail_step")
        async def fail_step(payload: dict, context=None) -> dict:
            return {"success": False, "error": "failed"}

        @rule("never_reached")
        async def never_reached(payload: dict, context=None) -> dict:
            return {"success": True}

        executor = RuleExecutor()
        results = await executor.execute_chain(["fail_step", "never_reached"], {})

        assert len(results) == 1
        assert results[0].success is False


# ==================== Hello World Integration Test ====================


class TestHelloWorldScript:
    """Integration test with actual hello_world script."""

    @pytest.fixture(autouse=True)
    def setup_registry(self):
        """Re-import scripts to register rules after any previous clear."""
        from scripts.registry import rule_registry

        # Clear any previous test registrations
        rule_registry.clear()

        # Re-import hello_world module to register the rule
        # Must clear first, then reload, so decorator can re-register
        import importlib

        import scripts.hello_world.main

        importlib.reload(scripts.hello_world.main)
        yield
        rule_registry.clear()

    @pytest.mark.asyncio
    async def test_hello_world_via_registry(self):
        """Execute hello_world through registry."""
        from scripts.registry import rule_registry

        handler = rule_registry.get("hello_world")
        assert handler is not None, "hello_world not registered"

        # New signature: (payload, context)
        result = await handler({"name": "JobRunner"}, None)
        assert result["success"] is True
        assert "Hello, JobRunner" in result["message"]

    @pytest.mark.asyncio
    async def test_hello_world_via_executor(self):
        """Execute hello_world through RuleExecutor."""
        executor = RuleExecutor()
        result = await executor.execute("hello_world", {"name": "Test"})

        assert result.success is True
        assert "Hello, Test" in result.message
