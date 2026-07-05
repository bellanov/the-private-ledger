"""Unit tests for truthiness sample."""

import pytest

from samples.truthiness.truthiness import (
    demo_boolean_basics,
    demo_default_value_with_or,
    demo_falsy_values,
    demo_none_checking,
    demo_short_circuit_with_and,
    demo_truthy_values,
)


@pytest.mark.unit
def test_demo_boolean_basics():
    """Test basic boolean comparisons."""
    one_less_than_two, true_equals_false = demo_boolean_basics()
    assert one_less_than_two is True
    assert true_equals_false is False


@pytest.mark.unit
def test_demo_none_checking_with_none():
    """Test None checking with None value."""
    is_check, is_check2 = demo_none_checking(None)
    assert is_check is True


@pytest.mark.unit
def test_demo_none_checking_with_value():
    """Test None checking with non-None value."""
    is_check, is_check2 = demo_none_checking(5)
    assert is_check is False


@pytest.mark.unit
def test_demo_falsy_values():
    """Test falsy values."""
    truthiness = demo_falsy_values()
    assert truthiness["False"] is False
    assert truthiness["None"] is False
    assert truthiness["empty list"] is False
    assert truthiness["empty dict"] is False
    assert truthiness["empty string"] is False
    assert truthiness["empty set"] is False
    assert truthiness["zero int"] is False
    assert truthiness["zero float"] is False


@pytest.mark.unit
def test_demo_truthy_values():
    """Test truthy values."""
    t1, t2, t3, t4 = demo_truthy_values()
    assert t1 is True  # [1] is truthy
    assert t2 is True  # {"a": 1} is truthy
    assert t3 is True  # "hello" is truthy
    assert t4 is True  # 1 is truthy


@pytest.mark.unit
def test_demo_short_circuit_with_and_truthy():
    """Test short-circuit with and for truthy string."""
    result = demo_short_circuit_with_and("hello")
    assert result == "h"


@pytest.mark.unit
def test_demo_short_circuit_with_and_falsy():
    """Test short-circuit with and for empty string."""
    result = demo_short_circuit_with_and("")
    assert result == ""


@pytest.mark.unit
def test_demo_default_value_with_or_none():
    """Test default value with or for None."""
    result = demo_default_value_with_or(None)
    assert result == 0


@pytest.mark.unit
def test_demo_default_value_with_or_value():
    """Test default value with or for actual value."""
    result = demo_default_value_with_or(5)
    assert result == 5
