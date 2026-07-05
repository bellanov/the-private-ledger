"""zip & Argument Unpacking.

Overview of *zip & Argument Unpacking* in Python.

The zip function combines multiple iterables, and the unpacking operator (*) allows
passing sequences as individual arguments.
"""


def demo_zip_basic() -> list:
    """Demonstrate basic zip functionality."""
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    # zip is lazy, so convert to list
    return [pair for pair in zip(list1, list2)]


def demo_zip_different_lengths() -> list:
    """Demonstrate zip with lists of different lengths."""
    list1 = ["a", "b", "c", "d"]
    list2 = [1, 2, 3]  # shorter list

    # zip stops when shortest list ends
    return list(zip(list1, list2))


def demo_unzip() -> tuple:
    """Demonstrate 'unzipping' a list of tuples."""
    pairs = [("a", 1), ("b", 2), ("c", 3)]

    # Use * to unpack pairs as individual arguments to zip
    letters, numbers = zip(*pairs)
    return letters, numbers


def demo_argument_unpacking_basic() -> int:
    """Demonstrate argument unpacking with a function."""

    def add(a, b):
        return a + b

    # Normal call
    result1 = add(1, 2)  # returns 3

    # Unpacked call
    result2 = add(*[1, 2])  # returns 3

    return result1, result2


def demo_argument_unpacking_multiple() -> int:
    """Demonstrate unpacking with more than 2 arguments."""

    def sum_three(a, b, c):
        return a + b + c

    return sum_three(*[1, 2, 3])


def demo_zip_with_three_lists() -> list:
    """Demonstrate zipping three lists together."""
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = [True, False, True]

    return list(zip(list1, list2, list3))


def demo_zip_with_enumerate_like() -> list:
    """Demonstrate using zip to create index-value pairs."""
    items = ["apple", "banana", "cherry"]
    return list(zip(range(len(items)), items))


def main() -> None:
    """Demonstrate zip and argument unpacking concepts."""
    # Test basic zip
    result = demo_zip_basic()
    assert result == [("a", 1), ("b", 2), ("c", 3)]
    print("✓ Basic zip works correctly")

    # Test zip with different lengths
    result = demo_zip_different_lengths()
    assert result == [("a", 1), ("b", 2), ("c", 3)]
    assert len(result) == 3  # Stops at shortest list
    print("✓ Zip with different lengths works correctly")

    # Test unzipping
    letters, numbers = demo_unzip()
    assert letters == ("a", "b", "c")
    assert numbers == (1, 2, 3)
    print("✓ Unzipping works correctly")

    # Test argument unpacking
    result1, result2 = demo_argument_unpacking_basic()
    assert result1 == 3
    assert result2 == 3
    print("✓ Argument unpacking works correctly")

    # Test unpacking with multiple arguments
    result = demo_argument_unpacking_multiple()
    assert result == 6
    print("✓ Unpacking with multiple arguments works correctly")

    # Test zip with three lists
    result = demo_zip_with_three_lists()
    assert result == [("a", 1, True), ("b", 2, False), ("c", 3, True)]
    print("✓ Zipping three lists works correctly")

    # Test zip with enumerate-like behavior
    result = demo_zip_with_enumerate_like()
    assert result == [(0, "apple"), (1, "banana"), (2, "cherry")]
    print("✓ Zip with enumerate-like behavior works correctly")

    print("\nAll zip and argument unpacking concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
