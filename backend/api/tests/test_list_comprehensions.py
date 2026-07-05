"""Unit tests for list_comprehensions sample."""

import pytest

from samples.list_comprehensions.list_comprehensions import (
    demo_basic_comprehension,
    demo_combined_filter_transform,
    demo_dict_comprehension,
    demo_multiple_for_loops,
    demo_nested_for_with_reference,
    demo_set_comprehension,
    demo_transformation,
    demo_underscore_for_unused,
)


@pytest.mark.unit
def test_demo_basic_comprehension():
    """Test basic list comprehension."""
    result = demo_basic_comprehension()
    assert result == [0, 2, 4]


@pytest.mark.unit
def test_demo_transformation():
    """Test transformation with list comprehension."""
    result = demo_transformation()
    assert result == [0, 1, 4, 9, 16]


@pytest.mark.unit
def test_demo_combined_filter_transform():
    """Test combined filtering and transformation."""
    result = demo_combined_filter_transform()
    assert result == [0, 4, 16]


@pytest.mark.unit
def test_demo_dict_comprehension():
    """Test dictionary comprehension."""
    result = demo_dict_comprehension()
    assert result == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


@pytest.mark.unit
def test_demo_set_comprehension():
    """Test set comprehension."""
    result = demo_set_comprehension()
    assert result == {1}


@pytest.mark.unit
def test_demo_underscore_for_unused():
    """Test using underscore for unused values."""
    result = demo_underscore_for_unused()
    assert len(result) == 3
    assert all(z == 0 for z in result)


@pytest.mark.unit
def test_demo_multiple_for_loops():
    """Test list comprehension with multiple for loops."""
    result = demo_multiple_for_loops()
    assert len(result) == 9  # 3x3
    assert (0, 0) in result
    assert (2, 2) in result


@pytest.mark.unit
def test_demo_nested_for_with_reference():
    """Test nested for loops with reference to earlier loop."""
    result = demo_nested_for_with_reference()
    assert (0, 1) in result
    assert (2, 3) in result
    assert (0, 0) not in result
    assert len(result) == 10  # C(5,2) = 10
