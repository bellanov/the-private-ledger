"""Dataclasses Design Patterns.

Demonstrates good design patterns for Python dataclasses (PEP 557):
  1.  Basic Dataclass      — auto __init__, __repr__, __eq__
  2.  Frozen Dataclass      — immutable value objects with hashing
  3.  field() Customisation — default_factory, repr, compare, hash, metadata
  4.  __post_init__         — validation and derived fields
  5.  Inheritance           — extending dataclasses cleanly
  6.  ClassVar & InitVar    — class-level state and init-only parameters
  7.  Utility Functions     — asdict, astuple, fields, replace
  8.  Ordered Dataclass     — sortable instances with order=True
  9.  Slots Dataclass       — memory-efficient with slots=True (Python 3.10+)
  10. Domain Model Example  — combining patterns in a realistic use case
"""

from __future__ import annotations

import uuid
from dataclasses import InitVar, asdict, astuple, dataclass, field, fields, replace
from typing import Any, ClassVar

# ─────────────────────────────────────────────
# PATTERN 1: Basic Dataclass
#
# @dataclass generates __init__, __repr__, and __eq__ automatically from
# the class-level annotations. No boilerplate constructors needed.
# ─────────────────────────────────────────────


@dataclass
class Book:
    """Simple value object representing a book."""

    title: str
    author: str
    pages: int

    def summary(self) -> str:
        return f'"{self.title}" by {self.author} ({self.pages} pages)'


# ─────────────────────────────────────────────
# PATTERN 2: Frozen (Immutable) Dataclass
#
# frozen=True prevents attribute mutation after construction.
# It also synthesises __hash__, making instances usable in sets and
# as dict keys — just like a namedtuple, but with type annotations.
# ─────────────────────────────────────────────


@dataclass(frozen=True)
class Coordinate:
    """Immutable GPS coordinate — hashable and equality-comparable."""

    lat: float
    lon: float

    def distance_to(self, other: Coordinate) -> float:
        """Euclidean approximation (good enough for illustration)."""
        return ((self.lat - other.lat) ** 2 + (self.lon - other.lon) ** 2) ** 0.5


# ─────────────────────────────────────────────
# PATTERN 3: field() Customisation
#
# field() gives fine-grained control over each attribute:
#   default_factory — callable that produces the default (avoids mutable defaults)
#   repr=False      — hide sensitive or verbose fields from __repr__
#   compare=False   — exclude from __eq__ (and __hash__ when frozen=True)
#   metadata        — arbitrary dict attached to the field descriptor
# ─────────────────────────────────────────────


@dataclass
class Employee:
    """Employee record with controlled field behaviour."""

    name: str
    department: str
    # repr=False keeps the salary out of logs / debug output
    salary: float = field(default=0.0, repr=False)
    # Never share a mutable default — use default_factory instead
    tags: list[str] = field(default_factory=list)
    # Auto-generated ID excluded from equality checks
    id: str = field(
        default_factory=lambda: str(uuid.uuid4()),
        compare=False,
        metadata={"description": "Unique employee identifier"},
    )


# ─────────────────────────────────────────────
# PATTERN 4: __post_init__ — Validation and Derived Fields
#
# __post_init__ runs after the generated __init__. Use it to:
#   • validate field values and raise early errors
#   • compute derived attributes (mark them with init=False)
# ─────────────────────────────────────────────


@dataclass
class Rectangle:
    """Rectangle with validated dimensions and a derived area field."""

    width: float
    height: float
    # init=False fields are not accepted as constructor arguments
    area: float = field(init=False, repr=False)
    perimeter: float = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError(
                f"Dimensions must be positive, got {self.width}x{self.height}"
            )
        # Compute derived fields once, immediately after validation
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


# ─────────────────────────────────────────────
# PATTERN 5: Inheritance
#
# Dataclasses compose via normal inheritance. The child's fields come
# after the parent's in __init__. Avoid placing fields with defaults in
# a parent when the child adds required fields — Python disallows this.
# ─────────────────────────────────────────────


@dataclass
class Vehicle:
    """Base vehicle — required fields only, no defaults."""

    make: str
    model: str
    year: int

    def display(self) -> str:
        return f"{self.year} {self.make} {self.model}"


@dataclass
class ElectricVehicle(Vehicle):
    """Extends Vehicle with EV-specific attributes."""

    battery_kwh: float
    range_km: float

    def charge_efficiency(self) -> float:
        """km of range per kWh of battery."""
        return self.range_km / self.battery_kwh


# ─────────────────────────────────────────────
# PATTERN 6: ClassVar & InitVar
#
# ClassVar — a class-level attribute, invisible to __init__ and __repr__.
# InitVar  — accepted by __init__ but NOT stored as an instance attribute.
#            Pass it to __post_init__ for setup-time computation.
# ─────────────────────────────────────────────


@dataclass
class ServerConfig:
    """Configuration object with class-level defaults and setup logic."""

    # ClassVar: shared across all instances, not touched by dataclass machinery
    DEFAULT_PORT: ClassVar[int] = 8080
    MAX_CONNECTIONS: ClassVar[int] = 100

    host: str
    port: int = field(default_factory=lambda: ServerConfig.DEFAULT_PORT)
    # InitVar: used only during initialisation, not stored
    debug_mode: InitVar[bool] = False
    # Derived from InitVar in __post_init__
    log_level: str = field(init=False)

    def __post_init__(self, debug_mode: bool) -> None:
        self.log_level = "DEBUG" if debug_mode else "INFO"


# ─────────────────────────────────────────────
# PATTERN 7: Utility Functions
#
# The dataclasses module ships four handy utilities:
#   asdict()   — deep-convert to a plain dict (great for JSON serialisation)
#   astuple()  — deep-convert to a plain tuple
#   fields()   — return a tuple of Field descriptors for introspection
#   replace()  — return a shallow copy with selected fields overridden
# ─────────────────────────────────────────────


@dataclass
class Address:
    street: str
    city: str
    country: str
    postcode: str


@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    address: Address

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


# ─────────────────────────────────────────────
# PATTERN 8: Ordered Dataclass
#
# order=True synthesises __lt__, __le__, __gt__, __ge__ based on the
# tuple of all fields declared in order. Useful for sorting, heaps, etc.
# Set eq=False together with order=True if you supply your own __eq__.
# ─────────────────────────────────────────────


@dataclass(order=True)
class SemanticVersion:
    """Semantic version number — naturally sortable (major, minor, patch)."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"v{self.major}.{self.minor}.{self.patch}"

    @classmethod
    def from_string(cls, version: str) -> SemanticVersion:
        """Parse 'major.minor.patch' or 'vX.Y.Z' into a SemanticVersion."""
        parts = version.lstrip("v").split(".")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))


# ─────────────────────────────────────────────
# PATTERN 9: Slots Dataclass (Python 3.10+)
#
# slots=True replaces the per-instance __dict__ with a fixed-size C array.
# Benefits: ~50–200 bytes saved per instance, faster attribute access.
# Best for classes instantiated in large numbers (particles, rows, nodes).
# ─────────────────────────────────────────────


@dataclass(slots=True)
class Particle:
    """Memory-efficient 3-D particle — no __dict__ overhead."""

    x: float
    y: float
    z: float
    mass: float

    def kinetic_energy(self, velocity: float) -> float:
        return 0.5 * self.mass * velocity**2


# ─────────────────────────────────────────────
# PATTERN 10: Domain Model Example
#
# Combines multiple patterns in a realistic e-commerce use case:
#   • Frozen Money value object (immutable, hashable)
#   • Order with validation, derived totals, and replace() for state changes
#   • Serialisation via asdict()
# ─────────────────────────────────────────────


@dataclass(frozen=True)
class Money:
    """Immutable monetary amount with currency."""

    amount: float
    currency: str = "USD"

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"


@dataclass
class LineItem:
    """A single line in an order."""

    product_name: str
    unit_price: Money
    quantity: int = 1
    subtotal: Money = field(init=False)

    def __post_init__(self) -> None:
        if self.quantity < 1:
            raise ValueError("Quantity must be at least 1")
        self.subtotal = Money(
            self.unit_price.amount * self.quantity, self.unit_price.currency
        )


@dataclass
class Order:
    """An e-commerce order demonstrating combined dataclass patterns."""

    order_id: str = field(
        default_factory=lambda: str(uuid.uuid4())[:8], compare=False
    )  # shortened for readability; use full UUID in production
    customer_name: str = ""
    items: list[LineItem] = field(default_factory=list)
    status: str = field(default="pending", compare=False)
    total: Money = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._recalculate_total()

    def _recalculate_total(self) -> None:
        if not self.items:
            self.total = Money(0.0)
            return
        currency = self.items[0].unit_price.currency
        self.total = Money(sum(item.subtotal.amount for item in self.items), currency)

    def add_item(self, item: LineItem) -> Order:
        """Return a new Order with the item appended (immutable update pattern).

        replace() triggers __post_init__ on the new instance, which
        recalculates the total automatically.
        """
        new_items = self.items + [item]
        return replace(self, items=new_items)

    def confirm(self) -> Order:
        """Return a confirmed copy of this order."""
        return replace(self, status="confirmed")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    # 1. Basic Dataclass
    print("=== Basic Dataclass ===")
    book = Book("Clean Code", "Robert C. Martin", 431)
    print(f"  {book}")
    print(f"  {book.summary()}")
    book2 = Book("Clean Code", "Robert C. Martin", 431)
    print(f"  Equal books: {book == book2}")

    # 2. Frozen Dataclass
    print("\n=== Frozen Dataclass ===")
    home = Coordinate(51.5074, -0.1278)
    office = Coordinate(51.5155, -0.0922)
    print(f"  Home: {home}")
    print(f"  Distance: {home.distance_to(office):.4f}")
    visited = {home, office}  # hashable because frozen=True
    print(f"  Unique locations: {len(visited)}")
    try:
        home.lat = 0.0  # type: ignore[misc]
    except Exception as e:
        print(f"  Caught mutation attempt: {e}")

    # 3. field() Customisation
    print("\n=== field() Customisation ===")
    emp = Employee("Alice", "Engineering", salary=95_000, tags=["python", "ml"])
    print(f"  repr (salary hidden by repr=False): {emp}")  # salary excluded from output
    print(f"  Tags: {emp.tags}")

    # 4. __post_init__
    print("\n=== __post_init__ ===")
    rect = Rectangle(5.0, 3.0)
    print(f"  {rect}  area={rect.area}  perimeter={rect.perimeter}")
    try:
        Rectangle(-1.0, 3.0)
    except ValueError as e:
        print(f"  Caught: {e}")

    # 5. Inheritance
    print("\n=== Inheritance ===")
    car = Vehicle("Toyota", "Camry", 2023)
    ev = ElectricVehicle("Tesla", "Model 3", 2024, battery_kwh=75.0, range_km=560.0)
    print(f"  {car.display()}")
    print(f"  {ev.display()}  efficiency={ev.charge_efficiency():.1f} km/kWh")

    # 6. ClassVar & InitVar
    print("\n=== ClassVar & InitVar ===")
    prod_cfg = ServerConfig("prod.example.com")
    dev_cfg = ServerConfig("localhost", debug_mode=True)
    print(
        f"  prod: host={prod_cfg.host}  port={prod_cfg.port}  log_level={prod_cfg.log_level}"
    )
    print(
        f"  dev:  host={dev_cfg.host}  port={dev_cfg.port}  log_level={dev_cfg.log_level}"
    )
    print(f"  Shared default port: {ServerConfig.DEFAULT_PORT}")

    # 7. Utility Functions
    print("\n=== Utility Functions (asdict / astuple / fields / replace) ===")
    addr = Address("10 Downing St", "London", "UK", "SW1A 2AA")
    contact = Contact("Jane", "Smith", "jane@example.com", addr)

    d = asdict(contact)
    print(f"  asdict: {d['first_name']} lives at {d['address']['city']}")

    t = astuple(contact)
    print(f"  astuple first element: {t[0]}")

    field_names = [f.name for f in fields(contact)]
    print(f"  fields: {field_names}")

    updated = replace(contact, email="jane.smith@example.com")
    print(f"  replace email: {updated.email}")

    # 8. Ordered Dataclass
    print("\n=== Ordered Dataclass ===")
    versions = [
        SemanticVersion.from_string("2.1.0"),
        SemanticVersion.from_string("1.9.3"),
        SemanticVersion.from_string("2.0.1"),
        SemanticVersion.from_string("1.9.10"),
    ]
    print(f"  Sorted: {[str(v) for v in sorted(versions)]}")
    print(f"  Latest: {max(versions)}")

    # 9. Slots Dataclass
    print("\n=== Slots Dataclass ===")
    p = Particle(1.0, 2.0, 3.0, mass=9.11e-31)
    print(f"  {p}")
    print(f"  KE at 1e6 m/s: {p.kinetic_energy(1e6):.3e} J")
    try:
        p.charge = 1.6e-19  # type: ignore[attr-defined]
    except AttributeError as e:
        print(f"  Caught: {e}")

    # 10. Domain Model Example
    print("\n=== Domain Model Example ===")
    order = Order(customer_name="Bob")
    order = order.add_item(LineItem("Python Book", Money(39.99), quantity=2))
    order = order.add_item(LineItem("Mechanical Keyboard", Money(129.00)))
    order = order.confirm()
    print(f"  Order #{order.order_id} — status: {order.status}")
    print(f"  Total: {order.total}")
    print(f"  Items: {len(order.items)}")
    data = order.to_dict()
    print(f"  Serialised keys: {list(data.keys())}")


if __name__ == "__main__":
    main()
