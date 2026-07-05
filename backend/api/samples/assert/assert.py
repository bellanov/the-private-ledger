"""assert.

Overview of *assert* and its usage.

Assertions are a way to write automated tests to verify that your code is
working correctly.
"""


def smallest_item(xs: list) -> int:
    """Return the smallest item in a list.

    This function demonstrates the use of assertions to validate inputs.
    """
    assert xs, "empty list has no smallest item"
    return min(xs)


def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y


def divide(x: int, y: int) -> float:
    """Divide two numbers.

    This function demonstrates assertions for output validation.
    """
    assert y != 0, "cannot divide by zero"
    return x / y


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def is_sorted(xs: list) -> bool:
    """Check if a list is sorted in ascending order."""
    return all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1))


def main() -> None:
    """Demonstrate assert concepts."""
    # Test basic assertions
    assert 1 + 1 == 2
    assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"
    print("✓ Basic assertions work correctly")

    # Test assertions on function outputs
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("✓ Function output assertions work correctly")

    # Test smallest_item function
    assert smallest_item([10, 20, 5, 40]) == 5
    assert smallest_item([1, 0, -1, 2]) == -1
    assert smallest_item([42]) == 42
    print("✓ smallest_item function works correctly")

    # Test divide with assertion
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    print("✓ Divide function with assertions works correctly")

    # Test that divide raises AssertionError for division by zero
    try:
        divide(10, 0)
        assert False, "should have raised AssertionError"
    except AssertionError as e:
        assert "cannot divide by zero" in str(e)
    print("✓ Division by zero assertion works correctly")

    # Test that smallest_item raises AssertionError for empty list
    try:
        smallest_item([])
        assert False, "should have raised AssertionError"
    except AssertionError as e:
        assert "empty list" in str(e)
    print("✓ Empty list assertion works correctly")

    # Test multiple assertions on same function
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(0) is True
    print("✓ Multiple assertions on helper functions work correctly")

    # Test sorting assertion
    assert is_sorted([1, 2, 3, 4, 5]) is True
    assert is_sorted([1, 3, 2, 4]) is False
    assert is_sorted([]) is True  # Empty list is sorted
    assert is_sorted([1]) is True  # Single element is sorted
    print("✓ Sorting assertions work correctly")

    print("\nAll assert concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
