"""Functions.

Overview of *Functions* and their usage.

Functions are a fundamental way to organize code and make it reusable.
"""


def double(x):
    """Multiply input by 2.

    This function multiplies its input by 2.
    """
    return x * 2


def apply_to_one(f):
    """Call function f with 1 as its argument."""
    return f(1)


def my_print(message: str = "my default message") -> None:
    """Print a message, using a default if none is provided."""
    print(message)


def higher_order_function(operation, x: int, y: int) -> int:
    """Apply a binary operation to two numbers."""
    return operation(x, y)


def make_adder(x: int):
    """Create a function that adds x to its argument."""

    def adder(y: int) -> int:
        return x + y

    return adder


def parameter_with_default(x: int, y: int = 1) -> int:
    """Demonstrate parameter with default value."""
    return x + y


def main() -> None:
    """Demonstrate function concepts."""
    # Test basic function
    assert double(3) == 6
    print("✓ Basic function works correctly")

    # Test first-class function - assign to variable
    my_double = double
    assert my_double(5) == 10
    print("✓ Assigning function to variable works correctly")

    # Test passing function as argument
    x = apply_to_one(my_double)
    assert x == 2
    print("✓ Passing function as argument works correctly")

    # Test lambda with function argument
    y = apply_to_one(lambda x: x + 4)
    assert y == 5
    print("✓ Lambda function works correctly")

    # Test default parameter
    import io
    import sys

    # Capture print output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    my_print("hello")
    output1 = sys.stdout.getvalue()

    # Capture default output
    sys.stdout = io.StringIO()
    my_print()
    output2 = sys.stdout.getvalue()

    sys.stdout = old_stdout
    assert "hello" in output1
    assert "my default message" in output2
    print("✓ Default parameters work correctly")

    # Test higher-order function
    add = lambda x, y: x + y
    result = higher_order_function(add, 3, 4)
    assert result == 7
    print("✓ Higher-order function works correctly")

    # Test closure (function that returns function)
    add_5 = make_adder(5)
    assert add_5(3) == 8
    assert add_5(10) == 15
    print("✓ Closure works correctly")

    # Test parameter with default
    assert parameter_with_default(5) == 6  # y defaults to 1
    assert parameter_with_default(5, 3) == 8
    print("✓ Parameters with default values work correctly")

    print("\nAll function concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
