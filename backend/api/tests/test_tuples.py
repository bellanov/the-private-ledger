"""Unit tests for tuples sample."""

import pytest

from samples.tuples.tuples import (
    demo_tuple_creation,
    demo_tuple_immutability,
    demo_tuple_immutable_operations,
    demo_tuple_multiple_return,
    demo_tuple_unpacking,
    demo_tuple_variable_swap,
)


@pytest.mark.unit
def test_demo_tuple_creation():
    """Test creating tuples."""
    my_tuple, other_tuple = demo_tuple_creation()
    assert my_tuple == (1, 2)
    assert other_tuple == (3, 4)


@pytest.mark.unit
def test_demo_tuple_immutability():
    """Test tuple immutability."""
    result = demo_tuple_immutability((1, 2))
    assert result == "cannot modify a tuple"


@pytest.mark.unit
def test_demo_tuple_multiple_return():
    """Test multiple return values with tuples."""
    result = demo_tuple_multiple_return(2, 3)
    assert result == (5, 6)


@pytest.mark.unit
def test_demo_tuple_unpacking():
    """Test tuple unpacking."""
    s, p = demo_tuple_unpacking()
    assert s == 15
    assert p == 50


@pytest.mark.unit
def test_demo_tuple_variable_swap():
    """Test variable swapping with tuples."""
    x, y = demo_tuple_variable_swap()
    assert x == 2
    assert y == 1


@pytest.mark.unit
def test_demo_tuple_immutable_operations():
    """Test tuple operations."""
    length, contains_1, combined, repeated = demo_tuple_immutable_operations((1, 2))
    assert length == 2
    assert contains_1 is True
    assert combined == (1, 2, 3, 4)
    assert repeated == (1, 2, 1, 2)
