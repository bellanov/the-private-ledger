"""Lists.

Overview of *Lists* and their usage.

Lists are the fundamental ordered collection type in Python, similar to arrays
in other languages but with more built-in functionality.
"""


def demo_list_creation() -> tuple[list[int], list, list]:
    """Demonstrate creating different types of lists."""
    integer_list = [1, 2, 3]
    heterogeneous_list = ["string", 0.1, True]
    list_of_lists = [integer_list, heterogeneous_list, []]

    return integer_list, heterogeneous_list, list_of_lists


def demo_list_basics() -> tuple[int, int]:
    """Demonstrate basic list operations."""
    integer_list = [1, 2, 3]
    list_length = len(integer_list)  # equals 3
    list_sum = sum(integer_list)  # equals 6

    return list_length, list_sum


def demo_list_indexing() -> tuple[int, int, int, int]:
    """Demonstrate indexing and negative indexing."""
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    zero = x[0]  # equals 0, lists are 0-indexed
    one = x[1]  # equals 1
    nine = x[-1]  # equals 9, last element
    eight = x[-2]  # equals 8, next-to-last element

    return zero, one, nine, eight


def demo_list_slicing() -> tuple[list[int], list[int], list[int], list[int], list[int]]:
    """Demonstrate list slicing."""
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    first_three = x[:3]  # [0, 1, 2]
    three_to_end = x[3:]  # [3, 4, ..., 9]
    one_to_four = x[1:5]  # [1, 2, 3, 4]
    last_three = x[-3:]  # [7, 8, 9]
    without_first_and_last = x[1:-1]  # [1, 2, ..., 8]

    return first_three, three_to_end, one_to_four, last_three, without_first_and_last


def demo_list_stride() -> tuple[list[int], list[int]]:
    """Demonstrate slicing with stride."""
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    every_third = x[::3]  # [0, 3, 6, 9]
    five_to_three = x[5:2:-1]  # [5, 4, 3]

    return every_third, five_to_three


def demo_list_membership() -> tuple[bool, bool]:
    """Demonstrate the 'in' operator for list membership."""
    return 1 in [1, 2, 3], 0 in [1, 2, 3]


def demo_list_concatenation() -> tuple[list[int], list[int]]:
    """Demonstrate list concatenation."""
    x = [1, 2, 3]
    x_extended = x.copy()  # Make a copy to avoid modifying the original
    x_extended.extend([4, 5, 6])  # x_extended is now [1, 2, 3, 4, 5, 6]

    y = x + [4, 5, 6]  # y is [1, 2, 3, 4, 5, 6]; x is unchanged

    return x_extended, y


def demo_list_append() -> tuple[int, int]:
    """Demonstrate appending to a list."""
    x = [1, 2, 3]
    x.append(0)  # x is now [1, 2, 3, 0]
    y = x[-1]  # equals 0
    z = len(x)  # equals 4

    return y, z


def demo_list_unpacking() -> tuple[int, int]:
    """Demonstrate list unpacking."""
    x, y = [1, 2]  # now x is 1, y is 2
    return x, y


def demo_list_unpacking_underscore() -> int:
    """Demonstrate using underscore for unwanted values during unpacking."""
    _, y = [1, 2]  # now y == 2, didn't care about the first element
    return y


def main() -> None:
    """Demonstrate list concepts."""
    # Test list creation
    int_list, hetero_list, list_of_lists = demo_list_creation()
    assert int_list == [1, 2, 3]
    assert hetero_list == ["string", 0.1, True]
    print("✓ List creation works correctly")

    # Test basic operations
    length, total = demo_list_basics()
    assert length == 3
    assert total == 6
    print("✓ Basic list operations work correctly")

    # Test indexing
    z, o, n, e = demo_list_indexing()
    assert z == 0 and o == 1 and n == 9 and e == 8
    print("✓ List indexing (including negative) works correctly")

    # Test slicing
    first_three, three_to_end, one_to_four, last_three, without = demo_list_slicing()
    assert first_three == [0, 1, 2]
    assert three_to_end == list(range(3, 10))
    assert one_to_four == [1, 2, 3, 4]
    assert last_three == [7, 8, 9]
    print("✓ List slicing works correctly")

    # Test stride
    every_third, five_to_three = demo_list_stride()
    assert every_third == [0, 3, 6, 9]
    assert five_to_three == [5, 4, 3]
    print("✓ List stride works correctly")

    # Test membership
    is_member, not_member = demo_list_membership()
    assert is_member is True
    assert not_member is False
    print("✓ List membership check works correctly")

    # Test concatenation
    x_extended, y = demo_list_concatenation()
    assert x_extended == [1, 2, 3, 4, 5, 6]
    assert y == [1, 2, 3, 4, 5, 6]
    print("✓ List concatenation works correctly")

    # Test append
    last, length = demo_list_append()
    assert last == 0
    assert length == 4
    print("✓ List append works correctly")

    # Test unpacking
    x, y = demo_list_unpacking()
    assert x == 1 and y == 2
    print("✓ List unpacking works correctly")

    # Test unpacking with underscore
    y = demo_list_unpacking_underscore()
    assert y == 2
    print("✓ Unpacking with underscore works correctly")

    print("\nAll list concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
