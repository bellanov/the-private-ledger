"""Unit tests for hello_world sample."""

import pytest

from samples.hello_world.app import hello_world


@pytest.mark.unit
def test_hello_world():
    """Test that hello_world returns the correct greeting."""
    result = hello_world()
    assert result == "Hello, World!"


@pytest.mark.unit
def test_hello_world_is_string():
    """Test that hello_world returns a string."""
    result = hello_world()
    assert isinstance(result, str)
