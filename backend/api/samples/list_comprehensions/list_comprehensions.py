"""List Comprehensions.

Overview of *List Comprehensions* and their usage.

List comprehensions provide a concise and Pythonic way to create and transform lists.
"""


def demo_basic_comprehension() -> list:
    """Demonstrate basic list comprehension."""
    even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
    return even_numbers


def demo_transformation() -> list:
    """Demonstrate transformation with list comprehension."""
    squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
    return squares


def demo_combined_filter_transform() -> list:
    """Demonstrate combined filtering and transformation."""
    even_numbers = [x for x in range(5) if x % 2 == 0]
    even_squares = [x * x for x in even_numbers]  # [0, 4, 16]
    return even_squares


def demo_dict_comprehension() -> dict:
    """Demonstrate dictionary comprehension."""
    square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    return square_dict


def demo_set_comprehension() -> set:
    """Demonstrate set comprehension."""
    square_set = {x * x for x in [1, -1]}  # {1}
    return square_set


def demo_underscore_for_unused() -> list:
    """Demonstrate using underscore for unused values."""
    even_numbers = [0, 2, 4]
    zeros = [0 for _ in even_numbers]  # has the same length as even_numbers
    return zeros


def demo_multiple_for_loops() -> list:
    """Demonstrate list comprehension with multiple for loops."""
    pairs = [(x, y) for x in range(3) for y in range(3)]
    return pairs


def demo_nested_for_with_reference() -> list:
    """Demonstrate later for loops using earlier results."""
    increasing_pairs = [
        (x, y) for x in range(5) for y in range(x + 1, 5)  # only pairs with x < y
    ]
    return increasing_pairs


def main() -> None:
    """Demonstrate list comprehension concepts."""
    # Test basic filtering
    even_numbers = demo_basic_comprehension()
    assert even_numbers == [0, 2, 4]
    print("✓ Basic list comprehension works correctly")

    # Test transformation
    squares = demo_transformation()
    assert squares == [0, 1, 4, 9, 16]
    print("✓ Transformation with list comprehension works correctly")

    # Test combined filter and transform
    even_squares = demo_combined_filter_transform()
    assert even_squares == [0, 4, 16]
    print("✓ Combined filter and transform works correctly")

    # Test dict comprehension
    square_dict = demo_dict_comprehension()
    assert square_dict == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    print("✓ Dictionary comprehension works correctly")

    # Test set comprehension
    square_set = demo_set_comprehension()
    assert square_set == {1}
    print("✓ Set comprehension works correctly")

    # Test underscore usage
    zeros = demo_underscore_for_unused()
    assert len(zeros) == 3
    assert all(z == 0 for z in zeros)
    print("✓ Using underscore for unused values works correctly")

    # Test multiple for loops
    pairs = demo_multiple_for_loops()
    assert len(pairs) == 9  # 3x3 = 9 pairs
    assert (0, 0) in pairs
    assert (2, 2) in pairs
    print("✓ Multiple for loops in comprehension works correctly")

    # Test nested for with later referencing earlier
    increasing_pairs = demo_nested_for_with_reference()
    assert (0, 1) in increasing_pairs
    assert (2, 3) in increasing_pairs
    assert (0, 0) not in increasing_pairs  # x < y condition
    assert len(increasing_pairs) == 10  # C(5,2) = 10
    print("✓ Nested for loops with reference works correctly")

    print("\nAll list comprehension concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
