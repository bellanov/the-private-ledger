"""Counters.

Overview of *Counters* and their usage.

A Counter is a specialized dictionary for counting occurrences of items in
a collection.
"""

from collections import Counter


def demo_counter_creation() -> Counter:
    """Demonstrate creating a Counter."""
    c = Counter([0, 1, 2, 0])  # c is (basically) {0: 2, 1: 1, 2: 1}
    return c


def demo_counter_word_counts() -> Counter:
    """Demonstrate counting words using Counter."""
    document = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog", "the"]
    word_counts = Counter(document)
    return word_counts


def demo_counter_most_common(word_counts: Counter) -> list:
    """Demonstrate the most_common method."""
    # Get the 3 most common words and their counts
    most_common = word_counts.most_common(3)
    return most_common


def demo_counter_access(c: Counter) -> tuple:
    """Demonstrate accessing Counter values."""
    # Counter behaves like a dict
    count_0 = c[0]  # equals 2
    count_1 = c[1]  # equals 1
    count_missing = c[999]  # equals 0 (unlike regular dict)

    return count_0, count_1, count_missing


def main() -> None:
    """Demonstrate Counter concepts."""
    # Test Counter creation
    c = demo_counter_creation()
    assert c[0] == 2
    assert c[1] == 1
    assert c[2] == 1
    print("✓ Counter creation works correctly")

    # Test word counting
    word_counts = demo_counter_word_counts()
    assert word_counts["the"] == 3
    assert word_counts["quick"] == 1
    assert word_counts["lazy"] == 1
    print("✓ Word counting with Counter works correctly")

    # Test most_common
    most_common = demo_counter_most_common(word_counts)
    assert most_common[0][0] == "the"  # "the" is most common
    assert most_common[0][1] == 3  # appears 3 times
    assert len(most_common) == 3  # we asked for 3 most common
    print("✓ Counter.most_common() works correctly")

    # Test Counter access
    count_0, count_1, count_missing = demo_counter_access(c)
    assert count_0 == 2
    assert count_1 == 1
    assert count_missing == 0  # Missing keys return 0, not KeyError
    print("✓ Counter access works correctly")

    print("\nAll Counter concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
