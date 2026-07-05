# Logging

Overview of good *logging* design patterns in Python using the built-in `logging` module.

## Patterns Covered

| Pattern | Description |
|---|---|
| **Module-level logger** | Use `logging.getLogger(__name__)` — never call `logging.info()` directly |
| **Centralised configuration** | Configure handlers once at the entry point; libraries only define loggers |
| **Log levels** | Use `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` appropriately |
| **Exception logging** | Use `logger.exception()` inside `except` blocks to capture full tracebacks |
| **Lazy formatting** | Pass `%s` args to the logger — avoid f-strings so formatting is skipped when the level is disabled |
| **Logger hierarchy** | Child loggers (e.g. `myapp.db`) propagate to parents — no extra handlers needed |
| **Contextual logging** | Use `LoggerAdapter` to attach request/user context to every message in a scope |

## Key Rules

- **Never** configure logging in library code (no `basicConfig`, no `addHandler`) — leave that to the application entry point
- **Never** use `print()` for diagnostic output — it bypasses level filtering and is unstructured
- **Always** use a named logger (`getLogger(__name__)`) so output can be filtered and routed per module
- Use `RotatingFileHandler` for file output so logs don't grow unbounded
