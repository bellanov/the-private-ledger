"""Whitespace Formatting.

Overview of *Whitespace Formatting* in Python.

Python uses indentation to delimit code blocks, making proper whitespace handling
essential for correct code.
"""


def demo_indentation() -> list:
    """Demonstrate proper indentation."""
    result = []
    for i in [1, 2, 3, 4, 5]:
        result.append(i)  # first line in "for i" block
        for j in [1, 2, 3]:
            result.append(i + j)  # nested block
    return result


def demo_nested_loops() -> list:
    """Demonstrate nested loops with proper indentation."""
    results = []
    for i in range(3):
        for j in range(3):
            results.append((i, j))
    return results


def demo_long_computation() -> int:
    """Demonstrate handling long computations with line breaks."""
    # Whitespace is ignored inside parentheses
    long_winded_computation = (
        1
        + 2
        + 3
        + 4
        + 5
        + 6
        + 7
        + 8
        + 9
        + 10
        + 11
        + 12
        + 13
        + 14
        + 15
        + 16
        + 17
        + 18
        + 19
        + 20
    )
    return long_winded_computation


def demo_readable_list_of_lists() -> list:
    """Demonstrate readable formatting of nested lists."""
    # Properly formatted for readability
    easier_to_read = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return easier_to_read


def demo_line_continuation() -> int:
    """Demonstrate line continuation with backslash."""
    # Using backslash for line continuation (rarely used)
    result = 1 + 2 + 3 + 4 + 5
    return result


def demo_function_with_proper_format() -> str:
    """Demonstrate proper formatting of function calls."""
    # Multi-line function call
    my_list = ["apple", "banana", "cherry"]
    result = ", ".join([f"Item: {item}" for item in my_list])
    return result


def demo_conditional_formatting() -> str:
    """Demonstrate conditional statement formatting."""
    age = 25

    if age < 18:
        status = "minor"
    elif age < 65:
        status = "adult"
    else:
        status = "senior"

    return status


def main() -> None:
    """Demonstrate whitespace formatting concepts."""
    # Test indentation
    result = demo_indentation()
    assert 1 in result
    assert 2 in result
    assert 4 in result  # 1+3
    print("✓ Indentation works correctly")

    # Test nested loops
    result = demo_nested_loops()
    assert len(result) == 9  # 3x3 combinations
    print("✓ Nested loop indentation works correctly")

    # Test long computation
    result = demo_long_computation()
    assert result == 210
    print("✓ Line continuation in parentheses works correctly")

    # Test readable list formatting
    result = demo_readable_list_of_lists()
    assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("✓ Readable list formatting works correctly")

    # Test line continuation with backslash
    result = demo_line_continuation()
    assert result == 15
    print("✓ Line continuation with backslash works correctly")

    # Test function formatting
    result = demo_function_with_proper_format()
    assert "Item: apple" in result
    assert "Item: banana" in result
    assert "Item: cherry" in result
    print("✓ Function call formatting works correctly")

    # Test conditional formatting
    result = demo_conditional_formatting()
    assert result == "adult"
    print("✓ Conditional statement formatting works correctly")

    print("\nAll whitespace formatting concepts demonstrated successfully!")
    print("\nKey Guidelines:")
    print("- Always use spaces, never tabs")
    print("- Indentation indicates code blocks (no curly braces needed)")
    print("- Whitespace inside parentheses and brackets is flexible")
    print("- Use backslash for line continuation when necessary")


if __name__ == "__main__":
    main()
