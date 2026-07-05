"""defaultdict.

Overview of *defaultdict* and its usage.

defaultdict is a dictionary subclass that provides default values for missing keys,
eliminating the need for checking if a key exists.
"""

from collections import defaultdict


def demo_word_count_manual(document: list[str]) -> dict:
    """Demonstrate manual word counting without defaultdict."""
    word_counts = {}
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def demo_word_count_try_except(document: list[str]) -> dict:
    """Demonstrate word counting using try/except."""
    word_counts = {}
    for word in document:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1
    return word_counts


def demo_word_count_defaultdict(document: list[str]) -> dict:
    """Demonstrate word counting using defaultdict."""
    word_counts = defaultdict(int)  # int() produces 0
    for word in document:
        word_counts[word] += 1
    return dict(word_counts)  # Convert back to regular dict for comparison


def demo_defaultdict_list() -> dict:
    """Demonstrate defaultdict with list as default factory."""
    dd_list = defaultdict(list)  # list() produces an empty list
    dd_list[2].append(1)  # now dd_list contains {2: [1]}
    dd_list[2].append(3)
    dd_list[5].append(10)
    return dict(dd_list)


def demo_defaultdict_dict() -> dict:
    """Demonstrate defaultdict with dict as default factory."""
    dd_dict = defaultdict(dict)  # dict() produces an empty dict
    dd_dict["Joel"]["City"] = "Seattle"  # {"Joel" : {"City": "Seattle"}}
    dd_dict["Alice"]["City"] = "Portland"
    return dict(dd_dict)


def demo_defaultdict_custom() -> dict:
    """Demonstrate defaultdict with custom default factory."""
    dd_pair = defaultdict(lambda: [0, 0])  # Define custom types
    dd_pair[2][1] = 1  # now dd_pair contains {2: [0, 1]}
    dd_pair[5][0] = 10
    return dict(dd_pair)


def main() -> None:
    """Demonstrate defaultdict concepts."""
    document = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog", "the"]

    # Test manual approach
    word_counts_manual = demo_word_count_manual(document)
    assert word_counts_manual["the"] == 3
    assert word_counts_manual["quick"] == 1
    print("✓ Manual word counting works correctly")

    # Test try/except approach
    word_counts_try = demo_word_count_try_except(document)
    assert word_counts_try["the"] == 3
    assert word_counts_try["quick"] == 1
    print("✓ Try/except word counting works correctly")

    # Test defaultdict approach
    word_counts_dd = demo_word_count_defaultdict(document)
    assert word_counts_dd["the"] == 3
    assert word_counts_dd["quick"] == 1
    print("✓ defaultdict word counting works correctly")

    # Test defaultdict(list)
    dd_list = demo_defaultdict_list()
    assert dd_list[2] == [1, 3]
    assert dd_list[5] == [10]
    print("✓ defaultdict with list works correctly")

    # Test defaultdict(dict)
    dd_dict = demo_defaultdict_dict()
    assert dd_dict["Joel"]["City"] == "Seattle"
    assert dd_dict["Alice"]["City"] == "Portland"
    print("✓ defaultdict with dict works correctly")

    # Test defaultdict with custom factory
    dd_pair = demo_defaultdict_custom()
    assert dd_pair[2] == [0, 1]
    assert dd_pair[5] == [10, 0]
    print("✓ defaultdict with custom factory works correctly")

    print("\nAll defaultdict concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
