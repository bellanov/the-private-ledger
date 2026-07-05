"""Sets.

Overview of *Sets* and their usage.

Sets represent collections of distinct elements and provide fast membership testing.
"""


def demo_set_creation() -> set:
    """Demonstrate creating sets."""
    primes_below_10 = {2, 3, 5, 7}
    return primes_below_10


def demo_empty_set() -> set:
    """Demonstrate creating an empty set."""
    # Note: {} creates an empty dict, not an empty set
    s = set()
    s.add(1)  # s is now {1}
    s.add(2)  # s is now {1, 2}
    s.add(2)  # s is still {1, 2} - sets only contain distinct elements

    return s


def demo_set_operations() -> tuple[int, bool, bool]:
    """Demonstrate basic set operations."""
    s = {1, 2}

    x = len(s)  # equals 2
    y = 2 in s  # equals True
    z = 3 in s  # equals False

    return x, y, z


def demo_set_membership_performance() -> bool:
    """Demonstrate fast membership testing with sets."""
    # Create a large set of stopwords
    stopwords_list = (
        ["a", "an", "at"] + [f"word{i}" for i in range(100)] + ["yet", "you"]
    )
    stopwords_set = set(stopwords_list)

    # Membership check is very fast on sets
    result = "zip" in stopwords_set

    return result


def demo_distinct_items(item_list: list) -> tuple[int, int, list]:
    """Demonstrate finding distinct items in a collection."""
    num_items = len(item_list)  # 6
    item_set = set(item_list)  # {1, 2, 3}
    num_distinct_items = len(item_set)  # 3
    distinct_item_list = sorted(list(item_set))  # sorted for consistent output

    return num_items, num_distinct_items, distinct_item_list


def main() -> None:
    """Demonstrate set concepts."""
    # Test set creation
    primes = demo_set_creation()
    assert primes == {2, 3, 5, 7}
    print("✓ Set creation works correctly")

    # Test empty set
    s = demo_empty_set()
    assert s == {1, 2}
    print("✓ Empty set creation works correctly")

    # Test set operations
    length, has_2, has_3 = demo_set_operations()
    assert length == 2
    assert has_2 is True
    assert has_3 is False
    print("✓ Set operations work correctly")

    # Test membership performance
    result = demo_set_membership_performance()
    assert result is False  # "zip" should not be in the stopwords
    print("✓ Set membership testing works correctly")

    # Test finding distinct items
    item_list = [1, 2, 3, 1, 2, 3]
    num_items, num_distinct, distinct_list = demo_distinct_items(item_list)
    assert num_items == 6
    assert num_distinct == 3
    assert distinct_list == [1, 2, 3]
    print("✓ Finding distinct items works correctly")

    print("\nAll set concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
