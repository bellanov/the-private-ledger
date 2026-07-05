"""Unit tests for lists sample."""

import pytest

from samples.lists.lists import (
    demo_list_append,
    demo_list_basics,
    demo_list_concatenation,
    demo_list_creation,
    demo_list_indexing,
    demo_list_membership,
    demo_list_slicing,
    demo_list_stride,
    demo_list_unpacking,
    demo_list_unpacking_underscore,
)


@pytest.mark.unit
def test_demo_list_creation():
    """Test list creation."""
    int_list, hetero_list, list_of_lists = demo_list_creation()
    assert int_list == [1, 2, 3]
    assert hetero_list == ["string", 0.1, True]


@pytest.mark.unit
def test_demo_list_basics():
    """Test basic list operations."""
    length, total = demo_list_basics()
    assert length == 3
    assert total == 6


@pytest.mark.unit
def test_demo_list_indexing():
    """Test indexing and negative indexing."""
    z, o, n, e = demo_list_indexing()
    assert z == 0
    assert o == 1
    assert n == 9
    assert e == 8


@pytest.mark.unit
def test_demo_list_slicing():
    """Test list slicing."""
    first_three, three_to_end, one_to_four, last_three, without = demo_list_slicing()
    assert first_three == [0, 1, 2]
    assert three_to_end == list(range(3, 10))
    assert one_to_four == [1, 2, 3, 4]
    assert last_three == [7, 8, 9]


@pytest.mark.unit
def test_demo_list_stride():
    """Test list stride."""
    every_third, five_to_three = demo_list_stride()
    assert every_third == [0, 3, 6, 9]
    assert five_to_three == [5, 4, 3]


@pytest.mark.unit
def test_demo_list_membership():
    """Test list membership."""
    is_member, not_member = demo_list_membership()
    assert is_member is True
    assert not_member is False


@pytest.mark.unit
def test_demo_list_concatenation():
    """Test list concatenation."""
    x_extended, y = demo_list_concatenation()
    assert x_extended == [1, 2, 3, 4, 5, 6]
    assert y == [1, 2, 3, 4, 5, 6]


@pytest.mark.unit
def test_demo_list_append():
    """Test list append."""
    last, length = demo_list_append()
    assert last == 0
    assert length == 4


@pytest.mark.unit
def test_demo_list_unpacking():
    """Test list unpacking."""
    x, y = demo_list_unpacking()
    assert x == 1
    assert y == 2


@pytest.mark.unit
def test_demo_list_unpacking_underscore():
    """Test unpacking with underscore."""
    y = demo_list_unpacking_underscore()
    assert y == 2
