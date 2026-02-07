"""Callback system for rule execution results.

Provides handlers for on_success/on_failure callbacks defined in Rule model.

Architecture (2-tier):
    Tier 1 (Atoms): Low-level reusable functions (not AI-exposed)
        - send_telegram_message()
        - write_log()
        - store_artifact()

    Tier 2 (Handlers): Composable callback handlers (AI-exposed/orchestrated)
        - telegram_callback()
        - log_callback()
        - chain_callback()
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from app_base.core.log import logger

# ==============================================================================
# Tier 1: Atomic Functions (Low-level, reusable, NOT AI-exposed)
# ==============================================================================


async def send_telegram_message(
    chat_id: str,
    message: str,
    *,
    parse_mode: str = "Markdown",
    bot_token: str | None = None,
) -> bool:
    """Send a message via Telegram bot.

    This is a Tier 1 atomic function - reusable but not directly AI-exposed.

    Args:
        chat_id: Telegram chat ID to send to
        message: Message content
        parse_mode: Markdown or HTML
        bot_token: Bot token (uses env var if not provided)

    Returns:
        True if sent successfully
    """
    # TODO: Implement actual Telegram API call
    # For now, just log
    logger.info(f"[Telegram] Would send to {chat_id}: {message[:50]}...")
    return True


async def write_log(
    level: str,
    message: str,
    *,
    context: dict[str, Any] | None = None,
) -> bool:
    """Write a structured log entry.

    Args:
        level: Log level (info, warning, error)
        message: Log message
        context: Additional context data

    Returns:
        True if logged successfully
    """
    log_func = getattr(logger, level.lower(), logger.info)
    log_func(message, **context or {})
    return True


# ==============================================================================
# Tier 2: Callback Handlers (Composable, AI-orchestrated)
# ==============================================================================


@dataclass
class CallbackContext:
    """Context passed to callback handlers."""

    rule_name: str
    rule_id: str
    execution_id: str
    success: bool
    message: str
    data: dict[str, Any]
    payload: dict[str, Any]  # Original rule payload


class CallbackHandler(ABC):
    """Base class for callback handlers."""

    @abstractmethod
    async def execute(self, context: CallbackContext) -> bool:
        """Execute the callback.

        Returns:
            True if callback executed successfully
        """
        pass


class LogCallbackHandler(CallbackHandler):
    """Simple logging callback handler."""

    def __init__(self, level: str = "info"):
        self.level = level

    async def execute(self, context: CallbackContext) -> bool:
        status = "SUCCESS" if context.success else "FAILURE"
        message = (
            f"[{status}] Rule '{context.rule_name}' "
            f"(execution: {context.execution_id}): {context.message}"
        )
        return await write_log(
            level=self.level,
            message=message,
            context={"rule_id": context.rule_id, "data": context.data},
        )


class TelegramCallbackHandler(CallbackHandler):
    """Telegram notification callback handler."""

    def __init__(self, chat_id: str, template: str | None = None):
        self.chat_id = chat_id
        self.template = template or "📋 *{rule_name}*\n{status_emoji} {message}"

    async def execute(self, context: CallbackContext) -> bool:
        status_emoji = "✅" if context.success else "❌"
        message = self.template.format(
            rule_name=context.rule_name,
            status_emoji=status_emoji,
            message=context.message,
            **context.data,
        )
        return await send_telegram_message(
            chat_id=self.chat_id,
            message=message,
        )


class ChainCallbackHandler(CallbackHandler):
    """Chain multiple callback handlers together."""

    def __init__(self, handlers: list[CallbackHandler]):
        self.handlers = handlers

    async def execute(self, context: CallbackContext) -> bool:
        all_success = True
        for handler in self.handlers:
            try:
                result = await handler.execute(context)
                all_success = all_success and result
            except Exception as e:
                logger.error(f"Callback handler failed: {e}")
                all_success = False
        return all_success


# ==============================================================================
# Callback Factory (creates handlers from config)
# ==============================================================================


def create_callback_handler(config: dict[str, Any] | None) -> CallbackHandler | None:
    """Create a callback handler from configuration.

    Args:
        config: Callback configuration from Rule.on_success or Rule.on_failure
            Example:
            {
                "type": "telegram",
                "config": {"chat_id": "123456", "template": "..."}
            }

            {
                "type": "chain",
                "config": {"handlers": [
                    {"type": "log", "config": {"level": "info"}},
                    {"type": "telegram", "config": {"chat_id": "123"}}
                ]}
            }

    Returns:
        Configured CallbackHandler or None if config is invalid
    """
    if not config:
        return None

    callback_type = config.get("type")
    callback_config = config.get("config", {})

    if callback_type == "log":
        return LogCallbackHandler(level=callback_config.get("level", "info"))

    elif callback_type == "telegram":
        chat_id = callback_config.get("chat_id")
        if not chat_id:
            logger.warning("Telegram callback missing chat_id")
            return None
        return TelegramCallbackHandler(
            chat_id=chat_id,
            template=callback_config.get("template"),
        )

    elif callback_type == "chain":
        handlers_config = callback_config.get("handlers", [])
        handlers = []
        for h_config in handlers_config:
            handler = create_callback_handler(h_config)
            if handler:
                handlers.append(handler)
        return ChainCallbackHandler(handlers) if handlers else None

    else:
        logger.warning(f"Unknown callback type: {callback_type}")
        return None


# ==============================================================================
# Callback Registry (for Tier 2 handlers)
# ==============================================================================


_callback_types: dict[str, type[CallbackHandler]] = {
    "log": LogCallbackHandler,
    "telegram": TelegramCallbackHandler,
    "chain": ChainCallbackHandler,
}


def register_callback_type(name: str, handler_class: type[CallbackHandler]):
    """Register a custom callback type."""
    _callback_types[name] = handler_class


def list_callback_types() -> list[str]:
    """List available callback types."""
    return list(_callback_types.keys())
