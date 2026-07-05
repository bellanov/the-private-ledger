# Class Design Patterns

Good design patterns for Python classes — from value objects to behavioural patterns.

## Patterns Covered

| # | Pattern | When to Use |
|---|---|---|
| 1 | **Dataclass** | Plain value objects — auto `__init__`, `__repr__`, `__eq__`; `frozen=True` for immutability |
| 2 | **Factory Method** | Multiple named constructors via `@classmethod` — keeps `__init__` simple |
| 3 | **Singleton** | Only one instance should ever exist (config, connection pool) |
| 4 | **Builder** | Complex objects with many optional settings — fluent `return self` chaining |
| 5 | **Mixin** | Reusable slices of behaviour composed via multiple inheritance |
| 6 | **Descriptor** | Reusable attribute validation/transformation shareable across many classes |
| 7 | **Context Manager** | Resource management — `__enter__`/`__exit__` guarantee cleanup |
| 8 | **Observer** | Decouple state producers from consumers — register callbacks, emit events |
| 9 | **Template Method** | Fixed algorithm skeleton in the base class; subclasses override the steps |
| 10 | **`__slots__`** | Fixed attribute layout — removes per-instance `__dict__`, saves ~50–200 bytes per object |

## Key Rules

- **Prefer `@dataclass`** over hand-written `__init__`/`__repr__`/`__eq__` for value objects
- **Use `@classmethod` factory methods** instead of overloading `__init__` with optional flags
- **Keep mixins small and stateless** — one responsibility each; always place before the base class in the MRO
- **Use `__slots__`** when creating large numbers of instances (nodes, events, rows)
- **Return `False` from `__exit__`** unless you explicitly want to suppress exceptions
