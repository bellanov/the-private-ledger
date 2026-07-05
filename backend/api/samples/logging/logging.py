"""Logging Patterns.

Demonstrates good design patterns for logging in Python using the standard
`logging` module, including module-level loggers, handlers, formatters,
log levels, exception capture, and rotating file output.
"""

import logging
import logging.handlers
import sys
from pathlib import Path

# ─────────────────────────────────────────────
# PATTERN 1: Module-level logger
#
# Always use a named logger scoped to the module.
# Never call logging.info() / logging.debug() directly — that writes
# to the root logger and makes it hard to control output per-module.
# ─────────────────────────────────────────────

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# PATTERN 2: Centralised logging configuration
#
# Configure logging once at application entry point, not in library code.
# Libraries should only define loggers — never call basicConfig() or
# add handlers — so that callers stay in control.
# ─────────────────────────────────────────────

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def configure_logging(level: int = logging.DEBUG, log_file: Path | None = None) -> None:
    """Configure root logger with console and optional rotating file handler."""
    root = logging.getLogger()
    root.setLevel(level)

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console handler — INFO and above to stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

    # File handler — all levels, rotates at 1 MB, keeps 3 backups
    if log_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=1_000_000,
            backupCount=3,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)


# ─────────────────────────────────────────────
# PATTERN 3: Log levels — use the right one
# ─────────────────────────────────────────────


def demonstrate_log_levels() -> None:
    """Show each log level and when to use it."""
    logger.debug("DEBUG: fine-grained detail useful during development")
    logger.info("INFO: confirmation that things are working as expected")
    logger.warning("WARNING: something unexpected, but the app continues")
    logger.error("ERROR: a serious problem — a feature failed")
    logger.critical("CRITICAL: the app may not be able to continue")


# ─────────────────────────────────────────────
# PATTERN 4: Exception logging
#
# Use logger.exception() inside except blocks.
# It automatically includes the full stack trace
# without needing to pass exc_info=True manually.
# ─────────────────────────────────────────────


def divide(a: float, b: float) -> float | None:
    """Return a / b, logging any error."""
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Division failed: b=%s", b)
        return None


# ─────────────────────────────────────────────
# PATTERN 5: Lazy string formatting
#
# Pass args to the logger — do NOT use f-strings.
# The logger skips string interpolation entirely when the level
# is disabled, saving CPU on hot code paths.
# ─────────────────────────────────────────────


def process_items(items: list[str]) -> None:
    for item in items:
        logger.debug(
            "Processing item: %s", item
        )  # ✅ lazy — only formatted if DEBUG enabled
        # logger.debug(f"Processing item: {item}")  # ❌ always formats the string


# ─────────────────────────────────────────────
# PATTERN 6: Child loggers and logger hierarchy
#
# Loggers follow a dotted-name hierarchy. A child logger
# propagates records up to its parent by default, so you only
# need handlers on the root (or a shared ancestor).
# ─────────────────────────────────────────────


def demonstrate_hierarchy() -> None:
    """Show how parent/child loggers share configuration."""
    parent_logger = logging.getLogger("myapp")
    child_logger = logging.getLogger("myapp.database")  # child of myapp
    sibling_logger = logging.getLogger("myapp.cache")  # sibling

    parent_logger.info("myapp logger")
    child_logger.info("myapp.database logger — propagates to myapp then root")
    sibling_logger.warning("myapp.cache logger — also propagates up")


# ─────────────────────────────────────────────
# PATTERN 7: Contextual logging with LoggerAdapter
#
# Add consistent context (e.g. request_id, user_id) to every message
# in a given scope without threading it through every function call.
# ─────────────────────────────────────────────


class RequestAdapter(logging.LoggerAdapter):
    """Prepend request context to every log message."""

    def process(self, msg: str, kwargs: dict) -> tuple[str, dict]:
        ctx = self.extra.get("request_id", "?")
        return f"[req={ctx}] {msg}", kwargs


def handle_request(request_id: str) -> None:
    """Simulate handling a web request with contextual logging."""
    req_logger = RequestAdapter(logger, {"request_id": request_id})
    req_logger.info("Request received")
    req_logger.debug("Validating payload")
    req_logger.info("Request complete")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    configure_logging(level=logging.DEBUG, log_file=Path("app.log"))

    logger.info("=== Log Levels ===")
    demonstrate_log_levels()

    logger.info("=== Exception Logging ===")
    result = divide(10, 2)
    logger.info("10 / 2 = %s", result)
    divide(10, 0)  # triggers exception log

    logger.info("=== Lazy Formatting ===")
    process_items(["alpha", "beta", "gamma"])

    logger.info("=== Logger Hierarchy ===")
    demonstrate_hierarchy()

    logger.info("=== Contextual Logging ===")
    handle_request("abc-123")
    handle_request("xyz-789")


if __name__ == "__main__":
    main()
