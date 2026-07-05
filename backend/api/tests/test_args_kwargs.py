"""Unit tests for args_kwargs sample."""

import pytest

from samples.args_kwargs.args_kwargs import (
    doubler,
    doubler_correct,
    f1,
    f2,
    other_way_magic,
)


@pytest.mark.unit
def test_doubler_single_argument():
    """Test doubler with single argument function."""
    g = doubler(f1)
    assert g(3) == 8  # (3 + 1) * 2
    assert g(-1) == 0  # (-1 + 1) * 2


@pytest.mark.unit
def test_f1_function():
    """Test f1 function."""
    assert f1(3) == 4
    assert f1(-1) == 0


@pytest.mark.unit
def test_f2_function():
    """Test f2 function."""
    assert f2(1, 2) == 3
    assert f2(10, 20) == 30


@pytest.mark.unit
def test_doubler_correct_single_argument():
    """Test doubler_correct with single argument function."""
    g = doubler_correct(f1)
    assert g(3) == 8


@pytest.mark.unit
def test_doubler_correct_multiple_arguments():
    """Test doubler_correct with multiple argument function."""
    g = doubler_correct(f2)
    assert g(1, 2) == 6


@pytest.mark.unit
def test_other_way_magic_with_args():
    """Test other_way_magic with positional arguments."""
    result = other_way_magic(1, 2, 3)
    assert result == 6


@pytest.mark.unit
def test_other_way_magic_with_kwargs():
    """Test other_way_magic with keyword arguments."""
    result = other_way_magic(x=10, y=20, z=30)
    assert result == 60


@pytest.mark.unit
def test_unpacking_list():
    """Test unpacking list as arguments."""
    args_list = [1, 2, 3]
    result = other_way_magic(*args_list)
    assert result == 6


@pytest.mark.unit
def test_unpacking_dict():
    """Test unpacking dict as keyword arguments."""
    kwargs_dict = {"x": 10, "y": 20, "z": 30}
    result = other_way_magic(**kwargs_dict)
    assert result == 60
