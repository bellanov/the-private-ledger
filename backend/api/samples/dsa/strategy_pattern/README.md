# Strategy Pattern

The **Strategy Pattern** defines a family of interchangeable algorithms, encapsulates each one, and makes them swappable at runtime — without changing the client (context) code.

## Structure

```
Context  ──uses──►  «Strategy»
                        ▲
              ┌─────────┼─────────┐
         ConcreteA  ConcreteB  ConcreteC
```

- **Context** — holds a reference to a strategy and delegates work to it
- **Strategy** — the interchangeable behaviour (interface / protocol / callable)
- **Concrete strategies** — the actual implementations

## Three Pythonic Approaches

| Approach | When to use |
|---|---|
| **ABC** (`SortStrategy`) | Explicit contract; strategies may share base-class helpers |
| **Protocol** (`DiscountStrategy`) | Duck typing; no inheritance required — any conforming object works |
| **Callable** (`CompressionFn`) | Stateless, simple algorithms — plain functions are the strategies |

## Key Benefits

- **Open/Closed** — add new strategies without touching the context
- **Runtime swappable** — call `set_strategy()` to change behaviour on the fly
- **Testable** — inject a stub strategy in unit tests instead of the real one
