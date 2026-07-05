"""Tuples.

Overview of *Tuples* and their usage.

Tuples are immutable sequences, similar to lists but they cannot be modified
after creation.
"""


def demo_tuple_creation() -> tuple:
    """Demonstrate creating tuples."""
    my_list = [1, 2]
    my_tuple = (1, 2)
    other_tuple = 3, 4  # Parentheses are optional

    return my_tuple, other_tuple


def demo_tuple_immutability(my_tuple: tuple) -> str:
    """Demonstrate that tuples cannot be modified."""
    try:
        my_tuple[1] = 3  # type: ignore
    except TypeError:
        return "cannot modify a tuple"


def demo_tuple_multiple_return(x: int, y: int) -> tuple:
    """Demonstrate returning multiple values using tuples."""
    return (x + y), (x * y)


def demo_tuple_unpacking() -> tuple[int, int]:
    """Demonstrate unpacking tuples for multiple assignment."""
    s, p = demo_tuple_multiple_return(5, 10)  # s is 15, p is 50
    return s, p


def demo_tuple_variable_swap() -> tuple[int, int]:
    """Demonstrate swapping variables using tuple assignment."""
    x, y = 1, 2  # now x is 1, y is 2
    x, y = y, x  # Pythonic way to swap variables
    return x, y  # now x is 2, y is 1


def demo_tuple_immutable_operations(my_tuple: tuple) -> tuple:
    """Demonstrate operations that work on tuples (non-modifying)."""
    # These operations work because they don't modify the tuple
    length = len(my_tuple)
    contains_1 = 1 in my_tuple
    combined = my_tuple + (3, 4)
    repeated = my_tuple * 2

    return length, contains_1, combined, repeated


def main() -> None:
    """Demonstrate tuple concepts."""
    # Test tuple creation
    my_tuple, other_tuple = demo_tuple_creation()
    assert my_tuple == (1, 2)
    assert other_tuple == (3, 4)
    print("✓ Tuple creation works correctly")

    # Test immutability
    result = demo_tuple_immutability((1, 2))
    assert result == "cannot modify a tuple"
    print("✓ Tuple immutability works correctly")

    # Test multiple return values
    sum_prod = demo_tuple_multiple_return(2, 3)
    assert sum_prod == (5, 6)
    print("✓ Multiple return values via tuple works correctly")

    # Test unpacking
    s, p = demo_tuple_unpacking()
    assert s == 15
    assert p == 50
    print("✓ Tuple unpacking works correctly")

    # Test variable swapping
    x, y = demo_tuple_variable_swap()
    assert x == 2
    assert y == 1
    print("✓ Variable swapping with tuples works correctly")

    # Test immutable operations
    length, contains_1, combined, repeated = demo_tuple_immutable_operations((1, 2))
    assert length == 2
    assert contains_1 is True
    assert combined == (1, 2, 3, 4)
    assert repeated == (1, 2, 1, 2)
    print("✓ Tuple operations (non-modifying) work correctly")

    print("\nAll tuple concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
