"""Unit tests for counters sample."""

from collections import Counter

import pytest

from samples.counters.counters import (
    demo_counter_access,
    demo_counter_creation,
    demo_counter_most_common,
    demo_counter_word_counts,
)


@pytest.mark.unit
def test_demo_counter_creation():
    """Test Counter creation."""
    c = demo_counter_creation()
    assert isinstance(c, Counter)
    assert c[0] == 2
    assert c[1] == 1
    assert c[2] == 1


@pytest.mark.unit
def test_demo_counter_word_counts():
    """Test counting words using Counter."""
    word_counts = demo_counter_word_counts()
    assert isinstance(word_counts, Counter)
    assert word_counts["the"] == 3
    assert word_counts["quick"] == 1
    assert word_counts["lazy"] == 1


@pytest.mark.unit
def test_demo_counter_most_common():
    """Test the most_common method."""
    word_counts = demo_counter_word_counts()
    most_common = demo_counter_most_common(word_counts)
    assert len(most_common) == 3
    assert most_common[0][0] == "the"
    assert most_common[0][1] == 3


@pytest.mark.unit
def test_demo_counter_access():
    """Test accessing Counter values."""
    c = demo_counter_creation()
    count_0, count_1, count_missing = demo_counter_access(c)
    assert count_0 == 2
    assert count_1 == 1
    assert count_missing == 0


@pytest.mark.unit
def test_demo_counter_most_common_with_empty_counter():
    """Test most_common with an empty Counter."""
    empty_counter = Counter()
    most_common = demo_counter_most_common(empty_counter)
    assert most_common == []


@pytest.mark.unit
def test_demo_counter_most_common_requesting_more_than_available():
    """Test most_common requesting more items than available."""
    c = Counter([1, 1, 2, 2, 2])
    most_common = demo_counter_most_common(c)
    # Should return at most 3 items, but Counter only has 2 unique items
    assert len(most_common) == 2
    assert most_common[0] == (2, 3)
