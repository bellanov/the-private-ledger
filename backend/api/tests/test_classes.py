"""Unit tests for classes sample."""

import pytest

from samples.classes.classes import CountingClicker, NoResetClicker


@pytest.mark.unit
def test_counting_clicker_initialization():
    """Test CountingClicker initialization."""
    clicker = CountingClicker()
    assert clicker.read() == 0


@pytest.mark.unit
def test_counting_clicker_initialization_with_value():
    """Test CountingClicker initialization with a starting count."""
    clicker = CountingClicker(10)
    assert clicker.read() == 10


@pytest.mark.unit
def test_counting_clicker_single_click():
    """Test single click on CountingClicker."""
    clicker = CountingClicker()
    clicker.click()
    assert clicker.read() == 1


@pytest.mark.unit
def test_counting_clicker_multiple_clicks():
    """Test multiple clicks on CountingClicker."""
    clicker = CountingClicker()
    clicker.click()
    clicker.click(2)
    assert clicker.read() == 3


@pytest.mark.unit
def test_counting_clicker_reset():
    """Test reset on CountingClicker."""
    clicker = CountingClicker()
    clicker.click()
    clicker.click(2)
    assert clicker.read() == 3
    clicker.reset()
    assert clicker.read() == 0


@pytest.mark.unit
def test_counting_clicker_click_after_reset():
    """Test clicking after reset."""
    clicker = CountingClicker()
    clicker.click(5)
    clicker.reset()
    clicker.click(2)
    assert clicker.read() == 2


@pytest.mark.unit
def test_no_reset_clicker_initialization():
    """Test NoResetClicker initialization."""
    clicker = NoResetClicker()
    assert clicker.read() == 0


@pytest.mark.unit
def test_no_reset_clicker_click():
    """Test clicking on NoResetClicker."""
    clicker = NoResetClicker()
    clicker.click()
    assert clicker.read() == 1


@pytest.mark.unit
def test_no_reset_clicker_reset_does_nothing():
    """Test that reset on NoResetClicker does nothing."""
    clicker = NoResetClicker()
    clicker.click()
    assert clicker.read() == 1
    clicker.reset()
    assert clicker.read() == 1  # Count should remain 1


@pytest.mark.unit
def test_no_reset_clicker_inherits_from_counting_clicker():
    """Test that NoResetClicker is a subclass of CountingClicker."""
    clicker = NoResetClicker()
    assert isinstance(clicker, CountingClicker)
