"""Unit tests for dictionaries sample."""

import pytest

from samples.dictionaries.dictionaries import (
    demo_dict_access,
    demo_dict_assignment,
    demo_dict_creation,
    demo_dict_get,
    demo_dict_iteration,
    demo_dict_key_error,
    demo_dict_membership,
    demo_dict_membership_check,
    demo_dict_structured_data,
)


@pytest.mark.unit
def test_demo_dict_creation():
    """Test dictionary creation."""
    empty1, empty2, grades = demo_dict_creation()
    assert isinstance(empty1, dict) and len(empty1) == 0
    assert isinstance(empty2, dict) and len(empty2) == 0
    assert grades == {"Joel": 80, "Tim": 95}


@pytest.mark.unit
def test_demo_dict_access():
    """Test accessing values in a dictionary."""
    result = demo_dict_access()
    assert result == 80


@pytest.mark.unit
def test_demo_dict_key_error():
    """Test KeyError handling."""
    grades = {"Joel": 80, "Tim": 95}
    result = demo_dict_key_error(grades)
    assert result == "no grade for Kate!"


@pytest.mark.unit
def test_demo_dict_membership():
    """Test checking for key existence."""
    joel_has, kate_has = demo_dict_membership()
    assert joel_has is True
    assert kate_has is False


@pytest.mark.unit
def test_demo_dict_get():
    """Test get method with default values."""
    joel, kate, no_one = demo_dict_get()
    assert joel == 80
    assert kate == 0
    assert no_one is None


@pytest.mark.unit
def test_demo_dict_assignment():
    """Test assigning and modifying dictionary values."""
    num_students, grades = demo_dict_assignment()
    assert num_students == 3
    assert grades["Tim"] == 99
    assert grades["Kate"] == 100


@pytest.mark.unit
def test_demo_dict_structured_data():
    """Test using dictionaries to represent structured data."""
    tweet = demo_dict_structured_data()
    assert tweet["user"] == "joelgrus"
    assert tweet["retweet_count"] == 100


@pytest.mark.unit
def test_demo_dict_iteration():
    """Test iterating over dictionary keys, values, and items."""
    keys, values, items = demo_dict_iteration()
    assert "user" in keys
    assert "joelgrus" in values
    assert len(items) == 4


@pytest.mark.unit
def test_demo_dict_membership_check():
    """Test membership checks in different dict views."""
    check1, check2, check3 = demo_dict_membership_check()
    assert check1 is True
    assert check2 is True
    assert check3 is True
