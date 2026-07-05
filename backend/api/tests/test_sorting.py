"""Unit tests for sorting sample."""

import pytest

from samples.sorting.sorting import (
    demo_reverse_sort,
    demo_sort_by_key,
    demo_sort_case_insensitive,
    demo_sort_in_place,
    demo_sort_strings,
    demo_sort_strings_by_length,
    demo_sort_tuples_by_element,
    demo_sorted_function,
)


@pytest.mark.unit
def test_demo_sort_in_place():
    """Test in-place sorting."""
    result = demo_sort_in_place()
    assert result == [1, 2, 3, 4]


@pytest.mark.unit
def test_demo_sorted_function():
    """Test sorted function vs sort method."""
    y, x = demo_sorted_function()
    assert y == [1, 2, 3, 4]
    assert x == [4, 1, 2, 3]  # x unchanged


@pytest.mark.unit
def test_demo_reverse_sort():
    """Test reverse sorting."""
    result = demo_reverse_sort()
    assert result == [4, 3, 2, 1]


@pytest.mark.unit
def test_demo_sort_by_key():
    """Test sorting with a key function."""
    result = demo_sort_by_key()
    assert result == [-4, 3, -2, 1]


@pytest.mark.unit
def test_demo_sort_tuples_by_element():
    """Test sorting tuples by a specific element."""
    result = demo_sort_tuples_by_element()
    assert result[0][0] == "the"
    assert result[0][1] == 5


@pytest.mark.unit
def test_demo_sort_strings():
    """Test sorting strings."""
    result = demo_sort_strings()
    assert result == ["apple", "banana", "cherry", "date"]


@pytest.mark.unit
def test_demo_sort_strings_by_length():
    """Test sorting strings by length."""
    result = demo_sort_strings_by_length()
    assert result == ["date", "apple", "banana", "cherry"]


@pytest.mark.unit
def test_demo_sort_case_insensitive():
    """Test case-insensitive string sorting."""
    result = demo_sort_case_insensitive()
    assert result[0] == "apple"
