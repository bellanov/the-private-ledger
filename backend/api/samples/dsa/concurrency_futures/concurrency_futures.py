"""concurrent.futures Design Patterns.

Demonstrates good design patterns for the `concurrent.futures` module:
  1. ThreadPoolExecutor  — I/O-bound work (network, file, DB calls)
  2. ProcessPoolExecutor — CPU-bound work (computation, image processing)
  3. map() vs submit()   — when to use each
  4. Future callbacks    — fire-and-forget with add_done_callback()
  5. Timeout handling    — preventing hangs with as_completed() + timeout
  6. Exception handling  — surfacing errors from worker threads/processes
  7. Executor as context manager — guaranteed shutdown / resource cleanup
"""

from __future__ import annotations

import math
import os
import time
from concurrent.futures import (
    Future,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)

# ─────────────────────────────────────────────
# Worker functions
#
# Keep worker functions at module level (not lambdas / nested functions)
# so they can be pickled by ProcessPoolExecutor on all platforms.
# ─────────────────────────────────────────────


def fetch_url(url: str) -> tuple[str, int]:
    """Simulate an I/O-bound HTTP request."""
    time.sleep(0.05)  # stand-in for real network latency
    return url, 200


def is_prime(n: int) -> bool:
    """CPU-bound primality check."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def risky_task(value: int) -> int:
    """Worker that raises for negative inputs."""
    if value < 0:
        raise ValueError(f"Negative input not allowed: {value}")
    time.sleep(0.01)
    return value * value


# ─────────────────────────────────────────────
# PATTERN 1: ThreadPoolExecutor for I/O-bound work
#
# Threads share memory and switch during I/O waits, so they are ideal when
# the bottleneck is waiting — not computing. The GIL is released during I/O.
# ─────────────────────────────────────────────


def fetch_all_urls(urls: list[str]) -> list[tuple[str, int]]:
    """Fetch multiple URLs concurrently and return results in input order."""
    # Use executor as a context manager — guarantees shutdown(wait=True) on exit
    with ThreadPoolExecutor(max_workers=8) as executor:
        # map() preserves order and blocks until all futures complete
        results = list(executor.map(fetch_url, urls))
    return results


# ─────────────────────────────────────────────
# PATTERN 2: ProcessPoolExecutor for CPU-bound work
#
# Each worker runs in a separate OS process, bypassing the GIL.
# Use when work is compute-heavy and can run independently.
# max_workers defaults to os.cpu_count() — override for memory-heavy tasks.
# ─────────────────────────────────────────────


def find_primes(candidates: list[int]) -> list[int]:
    """Find all primes in candidates using multiple CPU cores."""
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        flags = list(executor.map(is_prime, candidates))
    return [n for n, prime in zip(candidates, flags) if prime]


# ─────────────────────────────────────────────
# PATTERN 3: submit() for heterogeneous or dynamic work
#
# Use submit() instead of map() when:
#   - tasks have different functions or argument shapes
#   - you need the Future object (for callbacks, cancellation, timeout)
#   - you want results as-they-complete rather than in submission order
# ─────────────────────────────────────────────


def submit_mixed_work(values: list[int]) -> dict[int, int]:
    """Submit tasks individually; collect results mapped back to inputs."""
    results: dict[int, int] = {}
    with ThreadPoolExecutor() as executor:
        future_to_value: dict[Future, int] = {
            executor.submit(risky_task, v): v for v in values if v >= 0
        }
        for future in as_completed(future_to_value):
            original = future_to_value[future]
            results[original] = future.result()
    return results


# ─────────────────────────────────────────────
# PATTERN 4: Callbacks — fire-and-forget side effects
#
# add_done_callback(fn) registers a function called when the future finishes
# (success or exception). Runs in the thread that completed the future, so
# keep callbacks short and thread-safe.
# ─────────────────────────────────────────────


def on_done(future: Future) -> None:
    """Callback: log the result or error when a future completes."""
    exc = future.exception()
    if exc:
        print(f"  [callback] Task failed: {exc}")
    else:
        print(f"  [callback] Task succeeded: {future.result()}")


def submit_with_callbacks(values: list[int]) -> None:
    """Submit tasks and attach a logging callback to each."""
    with ThreadPoolExecutor() as executor:
        for v in values:
            future = executor.submit(risky_task, v)
            future.add_done_callback(on_done)
    # Executor waits for all futures before exiting the with block


# ─────────────────────────────────────────────
# PATTERN 5: Timeout + as_completed()
#
# as_completed() yields futures in completion order — fastest results first.
# Pass timeout= to avoid hanging forever on a slow or stuck worker.
# ─────────────────────────────────────────────


def fetch_with_timeout(urls: list[str], timeout: float = 5.0) -> None:
    """Process URL results as they arrive; skip any that exceed the timeout."""
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        try:
            for future in as_completed(future_to_url, timeout=timeout):
                url = future_to_url[future]
                url_result, status = future.result()
                print(f"  {status} {url_result} {url}")
        except TimeoutError:
            print("  [timeout] Some tasks did not finish in time")


# ─────────────────────────────────────────────
# PATTERN 6: Exception handling
#
# Exceptions raised in worker functions are stored in the Future and
# re-raised when you call future.result(). Always handle them explicitly —
# never silently swallow a future's result without checking for errors.
# ─────────────────────────────────────────────


def safe_submit(values: list[int]) -> None:
    """Submit tasks and handle per-task exceptions without crashing the batch."""
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(risky_task, v): v for v in values}
        for future in as_completed(futures):
            v = futures[future]
            try:
                print(f"  risky_task({v:>3}) = {future.result()}")
            except ValueError as exc:
                print(f"  risky_task({v:>3}) failed: {exc}")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    urls = [f"https://example.com/page/{i}" for i in range(6)]
    candidates = list(range(2, 50))

    print("=== Pattern 1: ThreadPoolExecutor (I/O-bound) ===")
    results = fetch_all_urls(urls)
    for url, status in results:
        print(f"  {status} {url}")

    print("\n=== Pattern 2: ProcessPoolExecutor (CPU-bound) ===")
    primes = find_primes(candidates)
    print(f"  Primes up to 50: {primes}")

    print("\n=== Pattern 3: submit() with as_completed() ===")
    squared = submit_mixed_work([1, 2, 3, 4, 5])
    for k, v in sorted(squared.items()):
        print(f"  {k}^2 = {v}")

    print("\n=== Pattern 4: Callbacks ===")
    submit_with_callbacks([3, -1, 5])

    print("\n=== Pattern 5: Timeout + as_completed() ===")
    fetch_with_timeout(urls[:4], timeout=5.0)

    print("\n=== Pattern 6: Per-task Exception Handling ===")
    safe_submit([4, -2, 7, -5, 9])


if __name__ == "__main__":
    main()
