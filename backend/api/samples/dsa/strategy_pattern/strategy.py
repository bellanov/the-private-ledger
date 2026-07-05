"""Strategy Pattern.

The Strategy Pattern defines a family of interchangeable algorithms, encapsulates
each one, and makes them swappable at runtime without changing the client code.

Three progressively Pythonic approaches are shown:
  1. ABC-based  — classical OOP, explicit interface contract
  2. Protocol   — structural subtyping (duck typing), no inheritance required
  3. Callable   — plain functions as strategies, most lightweight
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol

# ─────────────────────────────────────────────
# APPROACH 1: ABC-based Strategy
#
# Best when you want an explicit contract enforced at class-definition time
# and need to share helper methods across strategies.
# ─────────────────────────────────────────────


class SortStrategy(ABC):
    """Abstract base for sorting strategies."""

    @abstractmethod
    def sort(self, data: list[int]) -> list[int]: ...


class BubbleSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        result = data[:]
        n = len(result)
        for i in range(n):
            for j in range(n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result


class MergeSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        if len(data) <= 1:
            return data[:]
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        result: list[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]


class Sorter:
    """Context: delegates sorting to whichever strategy is injected."""

    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        """Swap the strategy at runtime."""
        self._strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self._strategy.sort(data)


# ─────────────────────────────────────────────
# APPROACH 2: Protocol-based Strategy
#
# Best when you want duck typing — any object with the right method
# qualifies, without inheriting from a base class.
# ─────────────────────────────────────────────


class DiscountStrategy(Protocol):
    def apply(self, price: float) -> float: ...


class NoDiscount:
    def apply(self, price: float) -> float:
        return price


class PercentageDiscount:
    def __init__(self, percent: float) -> None:
        self._percent = percent

    def apply(self, price: float) -> float:
        return price * (1 - self._percent / 100)


class FlatDiscount:
    def __init__(self, amount: float) -> None:
        self._amount = amount

    def apply(self, price: float) -> float:
        return max(0.0, price - self._amount)


class PriceCalculator:
    """Context: applies whichever discount strategy is set."""

    def __init__(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy) -> None:
        self._strategy = strategy

    def calculate(self, price: float) -> float:
        return self._strategy.apply(price)


# ─────────────────────────────────────────────
# APPROACH 3: Callable Strategy
#
# Best for simple, stateless strategies. A plain function or lambda
# is the strategy — no class boilerplate needed.
# ─────────────────────────────────────────────

from collections.abc import Callable

CompressionFn = Callable[[bytes], bytes]


def gzip_compress(data: bytes) -> bytes:
    import gzip

    return gzip.compress(data)


def zlib_compress(data: bytes) -> bytes:
    import zlib

    return zlib.compress(data)


def no_compress(data: bytes) -> bytes:
    return data


class FileExporter:
    """Context: compresses file content with an injected callable strategy."""

    def __init__(self, compress: CompressionFn = no_compress) -> None:
        self._compress = compress

    def set_strategy(self, compress: CompressionFn) -> None:
        self._compress = compress

    def export(self, content: bytes) -> bytes:
        return self._compress(content)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    data = [5, 3, 8, 1, 9, 2]

    # Approach 1 — ABC
    sorter = Sorter(BubbleSort())
    print("BubbleSort:", sorter.sort(data))

    sorter.set_strategy(MergeSort())  # swap at runtime
    print("MergeSort: ", sorter.sort(data))

    # Approach 2 — Protocol
    calc = PriceCalculator(NoDiscount())
    print(f"\nOriginal price:       ${calc.calculate(100):.2f}")

    calc.set_strategy(PercentageDiscount(20))
    print(f"After 20% discount:   ${calc.calculate(100):.2f}")

    calc.set_strategy(FlatDiscount(15))
    print(f"After $15 flat off:   ${calc.calculate(100):.2f}")

    # Approach 3 — Callable
    payload = b"hello world " * 100
    exporter = FileExporter(no_compress)
    raw = exporter.export(payload)
    print(f"\nNo compression:   {len(raw)} bytes")

    exporter.set_strategy(gzip_compress)
    gz = exporter.export(payload)
    print(f"gzip compression: {len(gz)} bytes")

    exporter.set_strategy(zlib_compress)
    zl = exporter.export(payload)
    print(f"zlib compression: {len(zl)} bytes")


if __name__ == "__main__":
    main()
