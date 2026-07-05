# Dataclasses Design Patterns

Good design patterns for Python **dataclasses** — from simple value objects to full domain models.

## Patterns Covered

| # | Pattern | When to Use |
|---|---|---|
| 1 | **Basic Dataclass** | Any plain object that needs auto `__init__`, `__repr__`, and `__eq__` |
| 2 | **Frozen Dataclass** | Immutable value objects that need hashing (use in sets, dict keys) |
| 3 | **`field()` Customisation** | Fine-grained control over defaults, repr, equality, and metadata |
| 4 | **`__post_init__`** | Validation and derived fields computed once at construction time |
| 5 | **Inheritance** | Extending a base dataclass with additional typed fields |
| 6 | **`ClassVar` & `InitVar`** | Class-level constants and init-only parameters not stored on the instance |
| 7 | **Utility Functions** | `asdict`, `astuple`, `fields`, `replace` — serialisation and cloning |
| 8 | **Ordered Dataclass** | Sortable instances using `order=True` (comparisons based on field order) |
| 9 | **Slots Dataclass** | Memory-efficient instances with `slots=True` — no `__dict__` overhead |
| 10 | **Domain Model Example** | Combining patterns in a realistic e-commerce use case |

## Key Rules

- **Prefer `@dataclass`** over hand-written `__init__` / `__repr__` / `__eq__` for value objects
- **Never use a mutable object as a default** — use `field(default_factory=list)` instead of `= []`
- **Use `frozen=True`** whenever instances should not change after creation; it also enables hashing
- **Use `field(repr=False)`** to hide sensitive or verbose attributes (e.g. passwords, large lists)
- **Use `field(compare=False)`** for identity fields (e.g. UUIDs) that should not affect equality
- **Compute derived fields in `__post_init__`** and mark them `field(init=False)` to keep the constructor clean
- **Prefer `replace(obj, **changes)`** over mutating state — produces a new instance, preserves immutability
- **Use `slots=True`** when creating many thousands of instances (particles, rows, events)
- **Use `order=True`** only when natural ordering by field tuple is meaningful for your domain
- **Call `asdict()`** for JSON-serialisable output; it deep-converts nested dataclasses

## Quick-Reference Cheat Sheet

```python
from dataclasses import dataclass, field, fields, asdict, astuple, replace
from typing import ClassVar

# ── Basic ──────────────────────────────────────────────────
@dataclass
class Point:
    x: float
    y: float

# ── Frozen (immutable, hashable) ───────────────────────────
@dataclass(frozen=True)
class Color:
    r: int; g: int; b: int

# ── field() options ────────────────────────────────────────
@dataclass
class Config:
    name: str
    tags: list[str] = field(default_factory=list)   # mutable default
    secret: str = field(repr=False)                  # hidden from repr
    id: str = field(compare=False)                   # excluded from eq

# ── Derived field + validation ─────────────────────────────
@dataclass
class Circle:
    radius: float
    area: float = field(init=False)

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("radius must be positive")
        self.area = 3.14159 * self.radius ** 2

# ── ClassVar and InitVar ───────────────────────────────────
from dataclasses import InitVar
@dataclass
class Widget:
    DEFAULT_COLOR: ClassVar[str] = "blue"
    size: int
    verbose: InitVar[bool] = False
    label: str = field(init=False)

    def __post_init__(self, verbose: bool):
        self.label = f"widget-{self.size}" + ("-v" if verbose else "")

# ── Utilities ──────────────────────────────────────────────
p = Point(1, 2)
asdict(p)          # {'x': 1, 'y': 2}
astuple(p)         # (1, 2)
fields(p)          # (Field(name='x',...), Field(name='y',...))
replace(p, x=99)   # Point(x=99, y=2)  ← new instance

# ── Ordered ───────────────────────────────────────────────
@dataclass(order=True)
class Version:
    major: int; minor: int; patch: int

# ── Slots (Python 3.10+) ───────────────────────────────────
@dataclass(slots=True)
class Pixel:
    x: int; y: int; r: int; g: int; b: int
```

## Usage

```bash
python3 samples/dsa/dataclasses/dataclasses_patterns.py
```

## When to Use Dataclasses

✅ **Good fit:**
- Value objects and data transfer objects (DTOs)
- Configuration containers
- Domain entities with many fields
- Any class where you'd otherwise write `__init__` / `__repr__` / `__eq__` by hand

⚠️ **Consider alternatives when:**
- You need database ORM mapping → use SQLAlchemy models or Django ORM
- You need schema validation with coercion → consider `pydantic`
- The class is purely behavioural with no data → a plain class is fine

## Python Version Notes

| Feature | Minimum Version |
|---|---|
| `@dataclass` | Python 3.7 |
| `slots=True` parameter | Python 3.10 |
| `kw_only=True` parameter | Python 3.10 |
| `match_args=True` (structural pattern matching) | Python 3.10 |

## Further Reading

- [PEP 557 — Data Classes](https://peps.python.org/pep-0557/)
- [dataclasses — Official Docs](https://docs.python.org/3/library/dataclasses.html)
- [Real Python — Python Data Classes Guide](https://realpython.com/python-data-classes/)
