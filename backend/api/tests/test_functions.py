"""Unit tests for functions sample."""

import pytest

from samples.functions.functions import (
    apply_to_one,
    double,
    higher_order_function,
    make_adder,
    parameter_with_default,
)


@pytest.mark.unit
def test_double():
    """Test basic function."""
    assert double(3) == 6
    assert double(5) == 10
    assert double(0) == 0
    assert double(-2) == -4


@pytest.mark.unit
def test_double_with_float():
    """Test double with floating point numbers."""
    assert double(2.5) == 5.0
    assert double(1.5) == 3.0


@pytest.mark.unit
def test_apply_to_one():
    """Test passing function as argument."""
    result = apply_to_one(double)
    assert result == 2


@pytest.mark.unit
def test_apply_to_one_with_lambda():
    """Test lambda function with apply_to_one."""
    result = apply_to_one(lambda x: x + 4)
    assert result == 5


@pytest.mark.unit
def test_higher_order_function():
    """Test higher-order function."""
    add = lambda x, y: x + y
    result = higher_order_function(add, 3, 4)
    assert result == 7


@pytest.mark.unit
def test_higher_order_function_with_subtract():
    """Test higher-order function with subtraction."""
    subtract = lambda x, y: x - y
    result = higher_order_function(subtract, 10, 3)
    assert result == 7


@pytest.mark.unit
def test_make_adder():
    """Test closure (function that returns function)."""
    add_5 = make_adder(5)
    assert add_5(3) == 8
    assert add_5(10) == 15


@pytest.mark.unit
def test_make_adder_multiple_closures():
    """Test multiple closures with different values."""
    add_5 = make_adder(5)
    add_10 = make_adder(10)
    assert add_5(3) == 8
    assert add_10(3) == 13


@pytest.mark.unit
def test_parameter_with_default():
    """Test parameters with default values."""
    assert parameter_with_default(5) == 6  # y defaults to 1
    assert parameter_with_default(5, 3) == 8
    assert parameter_with_default(5, 0) == 5
