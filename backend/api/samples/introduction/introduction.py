"""Introduction.

A general introduction to the Python programming language, including
installation instructions and core concepts.
"""


def demo_zen_of_python() -> str:
    """Demonstrate the Zen of Python principles.

    Key principles include:
    - There should be one—and preferably only one—obvious way to do it.
    - Beautiful is better than ugly.
    - Explicit is better than implicit.
    - Simple is better than complex.
    """
    return "The Zen of Python guides Pythonic code design"


def is_pythonic_example() -> bool:
    """Show Pythonic vs non-Pythonic ways.

    Pythonic way:
        for item in items:
            print(item)

    Non-Pythonic way:
        for i in range(len(items)):
            print(items[i])
    """
    items = [1, 2, 3]
    results = []

    # Pythonic way
    for item in items:
        results.append(item)

    return results == items


def beautiful_is_better() -> str:
    """Demonstrate beautiful code principles."""
    # Beautiful: clear variable names and structure
    total_count = 0
    for i in range(5):
        total_count += i

    return f"Beautiful code is easier to understand and maintain"


def explicit_is_better_than_implicit() -> dict:
    """Demonstrate explicit over implicit principle."""
    # Explicit: clear what's happening
    data = {"name": "Alice", "age": 30}

    # This is explicit - we know what we're getting
    name = data.get("name", "Unknown")

    # This is less explicit - might raise KeyError
    # age = data["age"]  # Could fail if key doesn't exist

    return data


def simple_is_better_than_complex() -> int:
    """Demonstrate simple over complex principle."""
    # Simple way
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)

    # Complex way (avoid this)
    # total = reduce(lambda x, y: x + y, numbers)

    return total


def demo_python_basics() -> tuple:
    """Demonstrate Python basic concepts."""
    # Dynamic typing
    x = 10
    x = "hello"
    x = [1, 2, 3]

    # Type checking
    var_int = 42
    var_str = "Python"
    var_list = [1, 2, 3]

    return (
        isinstance(var_int, int),
        isinstance(var_str, str),
        isinstance(var_list, list),
    )


def main() -> None:
    """Demonstrate Python introduction concepts."""
    # Test Zen of Python
    zen = demo_zen_of_python()
    assert "Zen" in zen
    print("✓ Zen of Python principle understood")

    # Test Pythonic example
    assert is_pythonic_example() is True
    print("✓ Pythonic code patterns work correctly")

    # Test beautiful code
    beautiful = beautiful_is_better()
    assert "Beautiful" in beautiful
    print("✓ Beautiful code principle demonstrated")

    # Test explicit is better
    data = explicit_is_better_than_implicit()
    assert "name" in data
    print("✓ Explicit is better than implicit demonstrated")

    # Test simple is better
    total = simple_is_better_than_complex()
    assert total == 15
    print("✓ Simple is better than complex demonstrated")

    # Test Python basics
    is_int, is_str, is_list = demo_python_basics()
    assert is_int is True
    assert is_str is True
    assert is_list is True
    print("✓ Python basic types work correctly")

    print("\nAll Python introduction concepts demonstrated successfully!")
    print("\nKey Takeaways:")
    print("- Python is dynamically typed")
    print("- Pythonic code follows specific conventions")
    print("- Explicit, simple, and beautiful code is preferred")
    print("- Python's readability is one of its greatest strengths")


if __name__ == "__main__":
    main()
