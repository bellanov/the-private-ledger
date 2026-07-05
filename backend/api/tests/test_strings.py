"""Unit tests for strings sample."""

import pytest

from samples.strings.strings import (
    demo_escape_characters,
    demo_multiline_strings,
    demo_string_concatenation,
    demo_string_delimiters,
)


@pytest.mark.unit
def test_demo_string_delimiters():
    """Test string delimiters."""
    single, double = demo_string_delimiters()
    assert single == double == "data science"


@pytest.mark.unit
def test_demo_escape_characters():
    """Test escape characters and raw strings."""
    tab_len, not_tab_len = demo_escape_characters()
    assert tab_len == 1
    assert not_tab_len == 2


@pytest.mark.unit
def test_demo_multiline_strings():
    """Test multiline strings."""
    multiline = demo_multiline_strings()
    assert "first line" in multiline
    assert "second line" in multiline
    assert "third line" in multiline


@pytest.mark.unit
def test_demo_string_concatenation():
    """Test string concatenation methods."""
    name1, name2, name3 = demo_string_concatenation("Joel", "Grus")
    assert name1 == "Joel Grus"
    assert name2 == "Joel Grus"
    assert name3 == "Joel Grus"
    assert name1 == name2 == name3
