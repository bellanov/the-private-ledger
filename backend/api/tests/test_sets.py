"""Unit tests for sets sample."""

import pytest

from samples.sets.sets import (
    demo_distinct_items,
    demo_empty_set,
    demo_set_creation,
    demo_set_membership_performance,
    demo_set_operations,
)


@pytest.mark.unit
def test_demo_set_creation():
    """Test set creation."""
    primes = demo_set_creation()
    assert primes == {2, 3, 5, 7}
    assert isinstance(primes, set)


@pytest.mark.unit
def test_demo_empty_set():
    """Test empty set creation."""
    s = demo_empty_set()
    assert s == {1, 2}
    assert isinstance(s, set)
    assert len(s) == 2


@pytest.mark.unit
def test_demo_set_operations():
    """Test basic set operations."""
    length, has_2, has_3 = demo_set_operations()
    assert length == 2
    assert has_2 is True
    assert has_3 is False


@pytest.mark.unit
def test_demo_set_membership_performance():
    """Test fast membership testing with sets."""
    result = demo_set_membership_performance()
    assert result is False  # "zip" should not be in the stopwords


@pytest.mark.unit
def test_demo_distinct_items():
    """Test finding distinct items in a collection."""
    item_list = [1, 2, 3, 1, 2, 3]
    num_items, num_distinct, distinct_list = demo_distinct_items(item_list)
    assert num_items == 6
    assert num_distinct == 3
    assert distinct_list == [1, 2, 3]


@pytest.mark.unit
def test_demo_distinct_items_all_unique():
    """Test finding distinct items when all are unique."""
    item_list = [1, 2, 3, 4, 5]
    num_items, num_distinct, distinct_list = demo_distinct_items(item_list)
    assert num_items == 5
    assert num_distinct == 5
    assert distinct_list == [1, 2, 3, 4, 5]


@pytest.mark.unit
def test_demo_distinct_items_all_same():
    """Test finding distinct items when all are the same."""
    item_list = [1, 1, 1, 1]
    num_items, num_distinct, distinct_list = demo_distinct_items(item_list)
    assert num_items == 4
    assert num_distinct == 1
    assert distinct_list == [1]
