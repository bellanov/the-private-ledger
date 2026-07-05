# concurrent.futures

Good design patterns for the `concurrent.futures` module — the standard way to run I/O-bound and CPU-bound work concurrently in Python without managing threads or processes manually.

## When to Use Each Executor

| Executor | Use for | Why |
|---|---|---|
| `ThreadPoolExecutor` | I/O-bound work (HTTP, DB, files) | Threads release the GIL during I/O; low overhead |
| `ProcessPoolExecutor` | CPU-bound work (computation, parsing) | Bypasses the GIL with separate OS processes |

## Patterns Covered

| # | Pattern | Description |
|---|---|---|
| 1 | **`ThreadPoolExecutor`** | Concurrent I/O — fetch multiple URLs at once |
| 2 | **`ProcessPoolExecutor`** | Parallel CPU work — prime checking across cores |
| 3 | **`submit()` vs `map()`** | `submit()` for heterogeneous/dynamic tasks; `map()` for uniform batches |
| 4 | **Callbacks** | `add_done_callback()` for fire-and-forget side effects |
| 5 | **Timeout + `as_completed()`** | Yield results as they arrive; bail out on slow tasks |
| 6 | **Exception handling** | Surface per-task errors without crashing the whole batch |

## Key Rules

- **Always use executors as context managers** (`with ... as executor`) — guarantees `shutdown(wait=True)` on exit
- **Keep worker functions at module level** — lambdas and nested functions cannot be pickled by `ProcessPoolExecutor`
- **Never ignore `future.result()`** — exceptions are stored in the `Future` and only raised when you call `.result()`
- **Use `ThreadPoolExecutor` for I/O, `ProcessPoolExecutor` for CPU** — threading does not help CPU-bound work due to the GIL
- **Use `as_completed()` when order doesn't matter** — it yields the fastest results first; `map()` preserves input order
