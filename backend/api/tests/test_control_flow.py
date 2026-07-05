"""Unit tests for control_flow sample."""

import pytest

from samples.control_flow.control_flow import (
    demo_continue_break,
    demo_for_loop,
    demo_if_statements,
    demo_ternary,
    demo_while_loop,
)


@pytest.mark.unit
def test_demo_if_statements_greater_than_2():
    """Test if statements with value > 2."""
    result = demo_if_statements(3)
    assert result == "x is greater than 2"


@pytest.mark.unit
def test_demo_if_statements_greater_than_1():
    """Test if statements with value > 1 but <= 2."""
    result = demo_if_statements(1.5)
    assert result == "x is greater than 1"


@pytest.mark.unit
def test_demo_if_statements_else():
    """Test if statements with value <= 1."""
    result = demo_if_statements(0)
    assert result == "x is 1 or less"


@pytest.mark.unit
def test_demo_ternary_even():
    """Test ternary operator with even number."""
    result = demo_ternary(4)
    assert result == "even"


@pytest.mark.unit
def test_demo_ternary_odd():
    """Test ternary operator with odd number."""
    result = demo_ternary(5)
    assert result == "odd"


@pytest.mark.unit
def test_demo_while_loop():
    """Test while loop."""
    result = demo_while_loop()
    assert result == list(range(10))


@pytest.mark.unit
def test_demo_for_loop():
    """Test for loop."""
    result = demo_for_loop()
    assert result == list(range(10))


@pytest.mark.unit
def test_demo_continue_break():
    """Test continue and break statements."""
    result = demo_continue_break()
    assert result == [0, 1, 2, 4]
