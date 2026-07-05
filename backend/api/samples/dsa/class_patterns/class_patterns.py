"""Class Design Patterns.

Demonstrates good design patterns for Python classes:
  1.  Dataclass          — value objects with auto __init__, __repr__, __eq__
  2.  Factory Method     — @classmethod constructors for multiple creation paths
  3.  Singleton          — ensure only one instance is ever created
  4.  Builder            — fluent interface for constructing complex objects
  5.  Mixin              — composing behaviour via multiple inheritance
  6.  Descriptor         — reusable attribute logic via __get__ / __set__
  7.  Context Manager    — resource management via __enter__ / __exit__
  8.  Observer           — notify subscribers when state changes
  9.  Template Method    — skeleton algorithm; subclasses fill in the steps
  10. __slots__          — fixed attribute layout to reduce per-instance memory
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable

# ─────────────────────────────────────────────
# PATTERN 1: Dataclass
#
# Use @dataclass for plain value objects. Python generates __init__,
# __repr__, and __eq__ automatically. Add frozen=True for immutability.
# ─────────────────────────────────────────────


@dataclass(frozen=True)
class Point:
    """Immutable 2-D point — equality and hashing come for free."""

    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


@dataclass
class Order:
    """Mutable order with a default-factory for the line items list."""

    customer: str
    items: list[str] = field(default_factory=list)  # never share a mutable default
    total: float = 0.0

    def add_item(self, name: str, price: float) -> None:
        self.items.append(name)
        self.total += price


# ─────────────────────────────────────────────
# PATTERN 2: Factory Method (@classmethod constructors)
#
# Provide named constructors for each distinct creation path so callers
# don't need to know internal details. Keeps __init__ simple.
# ─────────────────────────────────────────────


class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r, self.g, self.b = r, g, b

    @classmethod
    def from_hex(cls, hex_str: str) -> Color:
        """Create a Color from a '#RRGGBB' hex string."""
        hex_str = hex_str.lstrip("#")
        return cls(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))

    @classmethod
    def from_tuple(cls, rgb: tuple[int, int, int]) -> Color:
        """Create a Color from an (r, g, b) tuple."""
        return cls(*rgb)

    def __repr__(self) -> str:
        return f"Color(r={self.r}, g={self.g}, b={self.b})"


# ─────────────────────────────────────────────
# PATTERN 3: Singleton
#
# Override __new__ so only one instance is ever created. The instance is
# cached on the class itself. Thread-safety is omitted here for clarity;
# add a threading.Lock if needed.
# ─────────────────────────────────────────────


class AppConfig:
    """Application-wide configuration — only one instance should exist."""

    _instance: AppConfig | None = None

    def __new__(cls) -> AppConfig:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
            cls._instance.log_level = "INFO"
        return cls._instance


# ─────────────────────────────────────────────
# PATTERN 4: Builder
#
# Chain setter methods that each return `self` so callers can configure
# an object step-by-step without a huge constructor signature.
# ─────────────────────────────────────────────


class QueryBuilder:
    """Build a SQL SELECT statement fluently."""

    def __init__(self) -> None:
        self._table = ""
        self._columns: list[str] = ["*"]
        self._conditions: list[str] = []
        self._limit: int | None = None

    def from_table(self, table: str) -> QueryBuilder:
        self._table = table
        return self

    def select(self, *columns: str) -> QueryBuilder:
        self._columns = list(columns)
        return self

    def where(self, condition: str) -> QueryBuilder:
        self._conditions.append(condition)
        return self

    def limit(self, n: int) -> QueryBuilder:
        self._limit = n
        return self

    def build(self) -> str:
        cols = ", ".join(self._columns)
        query = f"SELECT {cols} FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit is not None:
            query += f" LIMIT {self._limit}"
        return query


# ─────────────────────────────────────────────
# PATTERN 5: Mixin
#
# Small, focused classes that add a single slice of behaviour.
# Compose them via multiple inheritance — no data, only methods.
# Place mixins before the base class in the MRO.
# ─────────────────────────────────────────────


class ReprMixin:
    """Auto __repr__ that lists all public instance attributes."""

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"


class SerializeMixin:
    """Serialize instance to / from a plain dict."""

    def to_dict(self) -> dict:
        return dict(self.__dict__)

    @classmethod
    def from_dict(cls, data: dict):
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class User(ReprMixin, SerializeMixin):
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


# ─────────────────────────────────────────────
# PATTERN 6: Descriptor
#
# A descriptor lives on the class and intercepts attribute access via
# __get__ / __set__ / __delete__. Unlike @property, a single descriptor
# class can be reused across multiple classes and attributes.
# ─────────────────────────────────────────────


class PositiveFloat:
    """Descriptor that enforces a positive float on any attribute."""

    def __set_name__(self, owner, name: str) -> None:
        self._name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self._name, None)

    def __set__(self, obj, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self._name} must be a positive number, got {value!r}")
        setattr(obj, self._name, float(value))


class Product:
    price = PositiveFloat()
    weight = PositiveFloat()

    def __init__(self, name: str, price: float, weight: float) -> None:
        self.name = name
        self.price = price  # routed through PositiveFloat.__set__
        self.weight = weight

    def __repr__(self) -> str:
        return f"Product({self.name!r}, price={self.price}, weight={self.weight})"


# ─────────────────────────────────────────────
# PATTERN 7: Context Manager
#
# Implement __enter__ and __exit__ to control setup and teardown.
# __exit__ receives exception info — return True to suppress, False to re-raise.
# ─────────────────────────────────────────────


class Timer:
    """Measure elapsed time for a block of code."""

    def __enter__(self) -> Timer:
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args) -> bool:
        self.elapsed = time.perf_counter() - self._start
        return False  # do not suppress exceptions

    def __repr__(self) -> str:
        return f"Timer(elapsed={self.elapsed * 1000:.2f}ms)"


# ─────────────────────────────────────────────
# PATTERN 8: Observer
#
# The subject keeps a list of subscriber callables and calls them all
# when state changes. Decouples producers from consumers.
# ─────────────────────────────────────────────


class EventEmitter:
    """Lightweight observer: subscribe to named events, emit to notify."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, callback: Callable) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


class StockTicker(EventEmitter):
    def __init__(self, symbol: str, price: float) -> None:
        super().__init__()
        self.symbol = symbol
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        old = self._price
        self._price = new_price
        self.emit("price_changed", self.symbol, old, new_price)


# ─────────────────────────────────────────────
# PATTERN 9: Template Method
#
# The base class defines the algorithm's skeleton in a final method.
# Abstract "hook" methods are overridden by subclasses to supply details.
# Inversion of control — the base class calls the subclass, not the other way.
# ─────────────────────────────────────────────


class DataExporter(ABC):
    """Template: validate -> transform -> export. Subclasses implement the steps."""

    def run(self, data: list[dict]) -> None:
        """The fixed algorithm skeleton — do not override."""
        self._validate(data)
        transformed = self._transform(data)
        self._export(transformed)

    def _validate(self, data: list[dict]) -> None:
        if not data:
            raise ValueError("Data cannot be empty")

    @abstractmethod
    def _transform(self, data: list[dict]) -> str: ...

    @abstractmethod
    def _export(self, content: str) -> None: ...


class CsvExporter(DataExporter):
    def _transform(self, data: list[dict]) -> str:
        header = ",".join(data[0].keys())
        rows = [",".join(str(v) for v in row.values()) for row in data]
        return "\n".join([header] + rows)

    def _export(self, content: str) -> None:
        print(f"  [CSV]\n{content}")


class JsonExporter(DataExporter):
    def _transform(self, data: list[dict]) -> str:
        import json

        return json.dumps(data, indent=2)

    def _export(self, content: str) -> None:
        print(f"  [JSON]\n{content}")


# ─────────────────────────────────────────────
# PATTERN 10: __slots__
#
# Declaring __slots__ prevents the per-instance __dict__, replacing it with
# a fixed-size C array. Saves ~50-200 bytes per instance — significant when
# creating millions of objects (e.g. nodes in a graph, rows in a table).
# ─────────────────────────────────────────────


class Vector:
    """Memory-efficient 3-D vector using __slots__."""

    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    # 1. Dataclass
    print("=== Dataclass ===")
    p1, p2 = Point(0, 0), Point(3, 4)
    print(f"  {p1} -> {p2}  distance={p1.distance_to(p2)}")
    order = Order("Alice")
    order.add_item("Book", 12.99)
    order.add_item("Pen", 1.49)
    print(f"  {order}")

    # 2. Factory Method
    print("\n=== Factory Method ===")
    c1 = Color.from_hex("#FF8800")
    c2 = Color.from_tuple((0, 128, 255))
    print(f"  {c1}")
    print(f"  {c2}")

    # 3. Singleton
    print("\n=== Singleton ===")
    cfg1 = AppConfig()
    cfg2 = AppConfig()
    cfg1.debug = True
    print(f"  Same instance: {cfg1 is cfg2}")
    print(f"  cfg2.debug (set via cfg1): {cfg2.debug}")

    # 4. Builder
    print("\n=== Builder ===")
    query = (
        QueryBuilder()
        .from_table("users")
        .select("id", "name", "email")
        .where("active = 1")
        .where("age > 18")
        .limit(10)
        .build()
    )
    print(f"  {query}")

    # 5. Mixin
    print("\n=== Mixin ===")
    user = User("Bob", "bob@example.com")
    print(f"  {user}")
    data = user.to_dict()
    restored = User.from_dict(data)
    print(f"  Restored: {restored}")

    # 6. Descriptor
    print("\n=== Descriptor ===")
    product = Product("Widget", price=9.99, weight=0.5)
    print(f"  {product}")
    try:
        product.price = -5
    except ValueError as e:
        print(f"  Caught: {e}")

    # 7. Context Manager
    print("\n=== Context Manager ===")
    with Timer() as t:
        total = sum(i * i for i in range(100_000))
    print(f"  sum={total}  {t}")

    # 8. Observer
    print("\n=== Observer ===")
    ticker = StockTicker("PYTH", 100.0)
    ticker.on("price_changed", lambda sym, old, new: print(f"  {sym}: {old} -> {new}"))
    ticker.price = 105.5
    ticker.price = 98.0

    # 9. Template Method
    print("\n=== Template Method ===")
    records = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]
    CsvExporter().run(records)

    # 10. __slots__
    print("\n=== __slots__ ===")
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"  {v1} + {v2} = {v1 + v2}")
    print(f"  magnitude({v1}) = {v1.magnitude():.4f}")
    try:
        v1.color = "red"  # __slots__ blocks arbitrary attributes
    except AttributeError as e:
        print(f"  Caught: {e}")


if __name__ == "__main__":
    main()
