"""Iterables & Generators.

Overview of *Iterables & Generators* and their usage.

Generators provide a way to create memory-efficient iterables that generate
values on demand.
"""

from typing import Generator


def generate_range(n: int) -> Generator[int, None, None]:
    """Generate integers from 0 to n-1.

    This is a generator function that yields values lazily.
    """
    i = 0
    while i < n:
        yield i  # every call to yield produces a value of the generator
        i += 1


def natural_numbers() -> Generator[int, None, None]:
    """Generate natural numbers: 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1


def demo_generator_comprehension():
    """Create a generator using a generator comprehension."""
    # Note: this uses parentheses, not square brackets (unlike list comprehension)
    evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
    return evens_below_20


def demo_generator_pipeline() -> Generator:
    """Demonstrate a generator pipeline for lazy evaluation."""
    # None of these computations *does* anything until we iterate
    data = natural_numbers()
    evens = (x for x in data if x % 2 == 0)
    even_squares = (x**2 for x in evens)
    even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

    return even_squares_ending_in_six


def demo_generator_once_iteration() -> list:
    """Demonstrate that generators can only be iterated once."""
    gen = generate_range(3)

    # First iteration
    first = list(gen)

    # Second iteration on same generator returns empty
    second = list(gen)

    return first, second


def main() -> None:
    """Demonstrate iterator and generator concepts."""
    # Test basic generator
    print("✓ Testing basic generator...")
    result = []
    for i in generate_range(5):
        result.append(i)
    assert result == [0, 1, 2, 3, 4]
    print("✓ Basic generator works correctly")

    # Test generator comprehension
    print("✓ Testing generator comprehension...")
    evens = demo_generator_comprehension()
    result = list(evens)
    assert result == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print("✓ Generator comprehension works correctly")

    # Test generator pipeline with first 5 matching values
    print("✓ Testing generator pipeline...")
    pipeline = demo_generator_pipeline()
    # Get first few values that end in 6 (16, 36, 196, 256, ...)
    result = []
    for _ in range(3):
        try:
            result.append(next(pipeline))
        except StopIteration:
            break
    assert result == [16, 36, 196]
    print("✓ Generator pipeline works correctly")

    # Test that generators can only iterate once
    print("✓ Testing single iteration of generators...")
    first, second = demo_generator_once_iteration()
    assert first == [0, 1, 2]
    assert second == []  # Empty on second iteration
    print("✓ Generators can only be iterated once")

    # Test generator vs list memory efficiency
    print("✓ Testing memory efficiency...")
    # This creates a generator (lazy) - minimal memory
    gen = generate_range(1000000)
    # This creates a list (eager) - significant memory
    lst = list(range(1000000))

    # Both work the same way, but generator is more efficient
    gen_first = next(generate_range(1000000))
    lst_first = lst[0]
    assert gen_first == lst_first == 0
    print("✓ Generators are memory efficient")

    print("\nAll generator concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
