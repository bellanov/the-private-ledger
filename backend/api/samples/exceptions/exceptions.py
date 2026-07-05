"""Exceptions.

Overview of *Exceptions* and their usage.

Exceptions provide a way to handle errors and unusual conditions in your code.
"""


def safe_divide(x: int, y: int) -> str:
    """Safely divide two numbers, handling ZeroDivisionError."""
    try:
        result = x / y
        return f"{x} / {y} = {result}"
    except ZeroDivisionError:
        return "cannot divide by zero"


def safe_int_conversion(value: str) -> str:
    """Safely convert a string to an integer."""
    try:
        result = int(value)
        return f"Converted {value} to {result}"
    except ValueError:
        return f"cannot convert {value} to integer"


def safe_list_access(lst: list, index: int) -> str:
    """Safely access a list element."""
    try:
        result = lst[index]
        return f"Element at index {index} is {result}"
    except IndexError:
        return f"index {index} is out of range"


def safe_dict_access(d: dict, key: str) -> str:
    """Safely access a dictionary value."""
    try:
        result = d[key]
        return f"Value for key '{key}' is {result}"
    except KeyError:
        return f"key '{key}' not found in dictionary"


def safe_file_read(filename: str) -> str:
    """Safely read a file."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"file '{filename}' not found"
    except IOError:
        return f"error reading file '{filename}'"


def exception_with_multiple_handlers(value: str) -> str:
    """Demonstrate multiple exception handlers."""
    try:
        # Try to convert to int, then access an element
        num = int(value)
        result = [1, 2, 3][num]
        return str(result)
    except ValueError:
        return "invalid number format"
    except IndexError:
        return "index out of range"


def finally_example(value: str) -> tuple[str, bool]:
    """Demonstrate finally clause."""
    finally_executed = False
    try:
        result = int(value)
    except ValueError:
        result_msg = "invalid number"
    finally:
        finally_executed = True

    return f"Result: {result if 'result' in locals() else 'unknown'}", finally_executed


def main() -> None:
    """Demonstrate exception concepts."""
    # Test basic exception handling
    result = safe_divide(10, 2)
    assert result == "10 / 2 = 5.0"
    print("✓ Basic division works correctly")

    result = safe_divide(10, 0)
    assert result == "cannot divide by zero"
    print("✓ ZeroDivisionError handling works correctly")

    # Test ValueError handling
    result = safe_int_conversion("42")
    assert "42" in result
    print("✓ Valid integer conversion works correctly")

    result = safe_int_conversion("not_a_number")
    assert "cannot convert" in result
    print("✓ ValueError handling works correctly")

    # Test IndexError handling
    result = safe_list_access([10, 20, 30], 1)
    assert "20" in result
    print("✓ Valid list access works correctly")

    result = safe_list_access([10, 20, 30], 10)
    assert "out of range" in result
    print("✓ IndexError handling works correctly")

    # Test KeyError handling
    result = safe_dict_access({"a": 1, "b": 2}, "a")
    assert "1" in result
    print("✓ Valid dict access works correctly")

    result = safe_dict_access({"a": 1, "b": 2}, "z")
    assert "not found" in result
    print("✓ KeyError handling works correctly")

    # Test FileNotFoundError handling
    result = safe_file_read("nonexistent_file.txt")
    assert "not found" in result
    print("✓ FileNotFoundError handling works correctly")

    # Test multiple exception handlers
    result = exception_with_multiple_handlers("not_a_number")
    assert "invalid number format" in result
    print("✓ ValueError in multiple handlers works correctly")

    result = exception_with_multiple_handlers("10")
    assert "out of range" in result
    print("✓ IndexError in multiple handlers works correctly")

    # Test finally clause
    msg, finally_exec = finally_example("42")
    assert finally_exec is True
    print("✓ Finally clause executes correctly")

    print("\nAll exception concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
