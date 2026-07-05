"""Sorting.

Overview of *Sorting* and its usage.

Python provides flexible sorting capabilities for organizing data in various ways.
"""


def demo_sort_in_place() -> list:
    """Demonstrate sorting a list in place."""
    x = [4, 1, 2, 3]
    x.sort()  # sorts x in place
    return x


def demo_sorted_function() -> tuple[list, list]:
    """Demonstrate sorted function vs sort method."""
    x = [4, 1, 2, 3]
    y = sorted(x)  # y is [1, 2, 3, 4], x is unchanged
    return y, x


def demo_reverse_sort() -> list:
    """Demonstrate sorting in reverse order."""
    x = [4, 1, 2, 3]
    y = sorted(x, reverse=True)  # [4, 3, 2, 1]
    return y


def demo_sort_by_key() -> list:
    """Demonstrate sorting with a key function."""
    # Sort by absolute value from largest to smallest
    x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
    return x


def demo_sort_tuples_by_element() -> list:
    """Demonstrate sorting tuples by a specific element."""
    word_counts = [("the", 5), ("quick", 3), ("brown", 2), ("fox", 1)]
    # Sort by count (second element) from highest to lowest
    sorted_wc = sorted(
        word_counts, key=lambda word_and_count: word_and_count[1], reverse=True
    )
    return sorted_wc


def demo_sort_strings() -> list:
    """Demonstrate sorting strings."""
    words = ["banana", "apple", "cherry", "date"]
    return sorted(words)


def demo_sort_strings_by_length() -> list:
    """Demonstrate sorting strings by length."""
    words = ["banana", "apple", "cherry", "date"]
    return sorted(words, key=len)


def demo_sort_case_insensitive() -> list:
    """Demonstrate case-insensitive string sorting."""
    words = ["Banana", "apple", "Cherry", "date"]
    return sorted(words, key=str.lower)


def main() -> None:
    """Demonstrate sorting concepts."""
    # Test in-place sort
    sorted_list = demo_sort_in_place()
    assert sorted_list == [1, 2, 3, 4]
    print("✓ In-place sort works correctly")

    # Test sorted function
    y, x = demo_sorted_function()
    assert y == [1, 2, 3, 4]
    assert x == [4, 1, 2, 3]  # x unchanged
    print("✓ sorted() function preserves original list")

    # Test reverse sort
    rev_sorted = demo_reverse_sort()
    assert rev_sorted == [4, 3, 2, 1]
    print("✓ Reverse sort works correctly")

    # Test sort by key function
    by_abs = demo_sort_by_key()
    assert by_abs == [-4, 3, -2, 1]
    print("✓ Sort by key (abs) works correctly")

    # Test sort tuples by element
    sorted_counts = demo_sort_tuples_by_element()
    assert sorted_counts[0][0] == "the"  # "the" has highest count (5)
    assert sorted_counts[0][1] == 5
    print("✓ Sort tuples by specific element works correctly")

    # Test sort strings
    sorted_words = demo_sort_strings()
    assert sorted_words == ["apple", "banana", "cherry", "date"]
    print("✓ Sort strings alphabetically works correctly")

    # Test sort strings by length
    by_length = demo_sort_strings_by_length()
    assert by_length == ["date", "apple", "banana", "cherry"]
    assert all(
        len(by_length[i]) <= len(by_length[i + 1]) for i in range(len(by_length) - 1)
    )
    print("✓ Sort strings by length works correctly")

    # Test case-insensitive sort
    case_insensitive = demo_sort_case_insensitive()
    assert case_insensitive[0] == "apple"  # lowercase comes first
    print("✓ Case-insensitive sort works correctly")

    print("\nAll sorting concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
