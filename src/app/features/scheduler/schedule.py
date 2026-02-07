"""Schedule calculation utilities using croniter."""

from datetime import datetime, timezone

from croniter import croniter


def calculate_next_run(
    cron_expression: str, base_time: datetime | None = None
) -> datetime:
    """Calculate the next run time based on cron expression.

    Args:
        cron_expression: Cron expression (e.g., "*/5 * * * *" for every 5 minutes)
        base_time: Base time to calculate from (defaults to current UTC time)

    Returns:
        Next scheduled run time (timezone-aware UTC datetime)

    Raises:
        ValueError: If cron_expression is invalid
    """
    if base_time is None:
        base_time = datetime.now(timezone.utc)

    # Ensure timezone awareness
    if base_time.tzinfo is None:
        base_time = base_time.replace(tzinfo=timezone.utc)

    cron = croniter(cron_expression, base_time)
    next_time: datetime = cron.get_next(datetime)  # type: ignore[assignment]

    # Ensure result is timezone-aware
    if next_time.tzinfo is None:
        next_time = next_time.replace(tzinfo=timezone.utc)

    return next_time


def is_valid_cron(cron_expression: str) -> bool:
    """Check if a cron expression is valid.

    Args:
        cron_expression: Cron expression to validate

    Returns:
        True if valid, False otherwise
    """
    try:
        croniter(cron_expression)
        return True
    except (KeyError, ValueError):
        return False
