"""Generator Design Patterns.

Demonstrates good design patterns for generators in Python:
  1. Basic generator function   — lazy sequence production with yield
  2. Generator pipeline         — chaining generators to process data in stages
  3. Infinite generator         — safe, memory-free infinite sequences
  4. Generator with send()      — two-way communication / coroutine-style
  5. Context-managed generator  — resource cleanup with try/finally + yield
  6. yield from delegation      — composing generators without manual loops
  7. Generator expression       — inline, memory-efficient alternative to list comprehension
"""

from __future__ import annotations

import itertools
from collections.abc import Generator, Iterable, Iterator
from contextlib import contextmanager
from typing import TypeVar

T = TypeVar("T")


# ─────────────────────────────────────────────
# PATTERN 1: Basic Generator Function
#
# Use `yield` to produce values one at a time.
# The function body is paused between yields — no list is ever built.
# Ideal for large or expensive sequences.
# ─────────────────────────────────────────────


def read_chunks(text: str, size: int = 4) -> Iterator[str]:
    """Yield successive chunks of a string without loading all chunks at once."""
    for start in range(0, len(text), size):
        yield text[start: start + size]


# ─────────────────────────────────────────────
# PATTERN 2: Generator Pipeline
#
# Chain generators together so each stage only pulls the data it needs.
# This is the generator equivalent of Unix pipes — constant memory regardless
# of input size because no stage materialises the full sequence.
# ─────────────────────────────────────────────


def parse_lines(lines: Iterable[str]) -> Iterator[str]:
    """Strip whitespace and drop blank lines."""
    for line in lines:
        stripped = line.strip()
        if stripped:
            yield stripped


def to_uppercase(lines: Iterable[str]) -> Iterator[str]:
    """Uppercase each line."""
    for line in lines:
        yield line.upper()


def filter_short(lines: Iterable[str], min_len: int = 5) -> Iterator[str]:
    """Drop lines shorter than min_len characters."""
    for line in lines:
        if len(line) >= min_len:
            yield line


def build_pipeline(raw_lines: list[str]) -> Iterator[str]:
    """Compose the three stages into a lazy pipeline."""
    stage1 = parse_lines(raw_lines)
    stage2 = to_uppercase(stage1)
    stage3 = filter_short(stage2)
    return stage3


# ─────────────────────────────────────────────
# PATTERN 3: Infinite Generator
#
# Generators can produce values forever — the caller controls when to stop
# using itertools.islice(), a loop break, or next() with a default.
# Never call list() on an infinite generator.
# ─────────────────────────────────────────────


def fibonacci() -> Iterator[int]:
    """Yield Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def counter(start: int = 0, step: int = 1) -> Iterator[int]:
    """Yield an endless arithmetic sequence."""
    n = start
    while True:
        yield n
        n += step


# ─────────────────────────────────────────────
# PATTERN 4: Two-way Communication with send()
#
# Generators are not just producers — callers can send values back in via
# generator.send(value). The sent value becomes the result of the `yield`
# expression inside the generator. Useful for accumulators and stateful
# coroutines without threads.
# ─────────────────────────────────────────────


def running_average() -> Generator[float, float, None]:
    """
    Coroutine that maintains a running average.

    Usage:
        gen = running_average()
        next(gen)           # prime the coroutine
        avg = gen.send(10)  # send a value, receive current average
    """
    total = 0.0
    count = 0
    average = 0.0
    while True:
        value = yield average  # yield current avg, receive next value
        total += value
        count += 1
        average = total / count


# ─────────────────────────────────────────────
# PATTERN 5: Resource Cleanup with try/finally
#
# Placing resource acquisition before `yield` and cleanup in `finally`
# guarantees the resource is released even if the caller stops iterating
# early (e.g. by breaking out of a for loop or if an exception is raised).
# ─────────────────────────────────────────────


def managed_lines(path: str) -> Iterator[str]:
    """Yield lines from a file, closing it even if iteration is abandoned."""
    f = open(path, encoding="utf-8")
    try:
        for line in f:
            yield line.rstrip("\n")
    finally:
        f.close()  # always runs, even on break or exception


# contextmanager uses the same pattern under the hood:
@contextmanager
def timer(label: str):
    """Context manager implemented as a generator."""
    import time

    start = time.perf_counter()
    try:
        yield  # execution of `with` block happens here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed * 1000:.2f} ms")


# ─────────────────────────────────────────────
# PATTERN 6: yield from — Delegating to Sub-generators
#
# `yield from iterable` transparently delegates iteration to another
# generator (or any iterable). It also forwards send() and throw() calls,
# making it essential for composing generators cleanly.
# ─────────────────────────────────────────────


def flatten(nested: Iterable) -> Iterator:
    """Recursively flatten arbitrarily nested iterables (not strings/bytes)."""
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)  # delegate to recursive call
        else:
            yield item


def chain_sources(*sources: Iterable[T]) -> Iterator[T]:
    """Yield from multiple sources in sequence (like itertools.chain)."""
    for source in sources:
        yield from source


# ─────────────────────────────────────────────
# PATTERN 7: Generator Expression
#
# An inline generator — same lazy semantics as a generator function,
# zero boilerplate. Use instead of a list comprehension when you only
# need to iterate once and don't need random access.
# ─────────────────────────────────────────────


def sum_of_squares(n: int) -> int:
    # Generator expression inside sum() — no intermediate list created
    return sum(x * x for x in range(n))


def first_match(items: Iterable[str], prefix: str) -> str | None:
    # next() + generator expression = efficient first-match search
    return next((s for s in items if s.startswith(prefix)), None)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    # Pattern 1 — chunked reading
    print("=== Chunks ===")
    for chunk in read_chunks("Hello, World!", size=4):
        print(repr(chunk), end="  ")
    print()

    # Pattern 2 — pipeline
    print("\n=== Pipeline ===")
    raw = ["  hello  ", "hi", "  WORLD  ", "", "  python  "]
    for line in build_pipeline(raw):
        print(line)

    # Pattern 3 — infinite generator + islice
    print("\n=== Fibonacci (first 10) ===")
    print(list(itertools.islice(fibonacci(), 10)))

    print("\n=== Counter (5..15, step 2) ===")
    print(list(itertools.islice(counter(5, 2), 6)))

    # Pattern 4 — send()
    print("\n=== Running Average ===")
    gen = running_average()
    next(gen)  # prime the coroutine
    for value in [10, 20, 30, 40]:
        avg = gen.send(value)
        print(f"  sent {value:>3} -> running avg = {avg:.1f}")

    # Pattern 6 — yield from
    print("\n=== Flatten ===")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(list(flatten(nested)))

    print("\n=== Chain Sources ===")
    print(list(chain_sources([1, 2], [3, 4], [5])))

    # Pattern 7 — generator expression
    print("\n=== Sum of Squares (n=6) ===")
    print(sum_of_squares(6))  # 0+1+4+9+16+25 = 55

    print("\n=== First Match ===")
    words = ["apple", "avocado", "banana", "apricot"]
    print(first_match(words, "ap"))  # apple — stops after first hit

    # Pattern 5 — timer context manager
    print()
    with timer("sum_of_squares(10_000)"):
        _ = sum_of_squares(10_000)


if __name__ == "__main__":
    main()
