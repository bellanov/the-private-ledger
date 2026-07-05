"""Type Annotations.

Overview of *Type Annotations* in Python.

Type annotations provide documentation and enable type checking tools to catch
potential errors before runtime.
"""

from typing import Callable, Dict, List, Optional, Union


def add_untyped(a, b):
    """Add two values without type annotations.

    This works for numbers, lists, strings, etc.
    """
    return a + b


def add_typed(a: int, b: int) -> int:
    """Add two integers with type annotations.

    Type annotations document the expected types but don't enforce them at runtime.
    """
    return a + b


def process_list(items: List[int]) -> int:
    """Process a list of integers and return the sum."""
    return sum(items)


def create_mapping(keys: List[str], values: List[int]) -> Dict[str, int]:
    """Create a dictionary from keys and values."""
    return dict(zip(keys, values))


def find_first_positive(numbers: List[int]) -> Optional[int]:
    """Find the first positive number, or None if not found.

    Optional indicates the return value can be either int or None.
    """
    for num in numbers:
        if num > 0:
            return num
    return None


def flexible_add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers that can be either int or float."""
    return a + b


def apply_operation(operation: Callable[[int, int], int], x: int, y: int) -> int:
    """Apply a binary operation to two integers.

    Callable indicates a function type.
    """
    return operation(x, y)


def demo_list_type_annotation() -> List[int]:
    """Demonstrate list type annotation."""
    numbers: List[int] = [1, 2, 3, 4, 5]
    return numbers


def demo_dict_type_annotation() -> Dict[str, int]:
    """Demonstrate dict type annotation."""
    ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
    return ages


def main() -> None:
    """Demonstrate type annotation concepts."""
    # Test untyped function
    assert add_untyped(10, 5) == 15
    assert add_untyped([1, 2], [3]) == [1, 2, 3]
    assert add_untyped("hi ", "there") == "hi there"
    print("✓ Untyped functions work with multiple types")

    # Test typed function
    assert add_typed(10, 5) == 15
    print("✓ Typed functions work correctly")

    # Test list type annotation
    result = process_list([1, 2, 3, 4, 5])
    assert result == 15
    print("✓ List type annotation works correctly")

    # Test dict type annotation
    mapping = create_mapping(["a", "b", "c"], [1, 2, 3])
    assert mapping == {"a": 1, "b": 2, "c": 3}
    print("✓ Dict type annotation works correctly")

    # Test Optional return type
    assert find_first_positive([-1, -2, 3, -4]) == 3
    assert find_first_positive([-1, -2, -3]) is None
    print("✓ Optional return type works correctly")

    # Test Union type annotation
    assert flexible_add(10, 5) == 15
    assert flexible_add(10.5, 5.5) == 16.0
    assert flexible_add(10, 5.5) == 15.5
    print("✓ Union type annotation works correctly")

    # Test Callable type annotation
    add_op = lambda x, y: x + y
    result = apply_operation(add_op, 3, 7)
    assert result == 10
    print("✓ Callable type annotation works correctly")

    # Test variable annotations
    numbers = demo_list_type_annotation()
    assert numbers == [1, 2, 3, 4, 5]
    print("✓ Variable type annotations work correctly")

    ages = demo_dict_type_annotation()
    assert ages == {"Alice": 25, "Bob": 30}
    print("✓ Dict variable annotation works correctly")

    print("\nAll type annotation concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
