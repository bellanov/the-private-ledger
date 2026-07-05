# Generators

Good design patterns for *generators* in Python — lazy, memory-efficient sequences and pipelines using `yield`.

## Patterns Covered

| # | Pattern | Description |
|---|---|---|
| 1 | **Basic generator function** | `yield` values one at a time — no list ever built in memory |
| 2 | **Generator pipeline** | Chain generators stage-by-stage like Unix pipes — constant memory |
| 3 | **Infinite generator** | Produce values forever; use `itertools.islice()` or `break` to stop |
| 4 | **`send()` / coroutine** | Two-way communication — caller sends values in, generator yields results back |
| 5 | **`try/finally` cleanup** | Guarantee resource release even when iteration is abandoned early |
| 6 | **`yield from` delegation** | Transparently delegate to sub-generators; forwards `send()` and `throw()` |
| 7 | **Generator expression** | Inline lazy generator — use instead of list comprehension when you iterate once |

## Key Rules

- **Never call `list()` on an infinite generator** — use `itertools.islice()` or a bounded loop
- **Prime coroutines** with `next(gen)` before the first `send()`
- **Prefer `yield from`** over manual inner loops when delegating to sub-generators
- **Use generator expressions** inside `sum()`, `any()`, `all()`, `max()`, `min()`, and `next()` to avoid building intermediate lists
- **Use `try/finally`** inside a generator whenever it acquires a resource — cleanup runs even on `GeneratorExit`
