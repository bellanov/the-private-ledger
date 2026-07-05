"""Unit tests for defaultdict sample."""

import pytest

from samples.defaultdict.defaultdict import (
    demo_defaultdict_custom,
    demo_defaultdict_dict,
    demo_defaultdict_list,
    demo_word_count_defaultdict,
    demo_word_count_manual,
    demo_word_count_try_except,
)


@pytest.mark.unit
def test_demo_word_count_manual():
    """Test manual word counting."""
    document = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog", "the"]
    counts = demo_word_count_manual(document)
    assert counts["the"] == 3
    assert counts["quick"] == 1


@pytest.mark.unit
def test_demo_word_count_try_except():
    """Test word counting with try/except."""
    document = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog", "the"]
    counts = demo_word_count_try_except(document)
    assert counts["the"] == 3
    assert counts["quick"] == 1


@pytest.mark.unit
def test_demo_word_count_defaultdict():
    """Test word counting with defaultdict."""
    document = ["the", "quick", "brown", "fox", "jumps", "the", "lazy", "dog", "the"]
    counts = demo_word_count_defaultdict(document)
    assert counts["the"] == 3
    assert counts["quick"] == 1


@pytest.mark.unit
def test_demo_defaultdict_list():
    """Test defaultdict with list."""
    dd_list = demo_defaultdict_list()
    assert dd_list[2] == [1, 3]
    assert dd_list[5] == [10]


@pytest.mark.unit
def test_demo_defaultdict_dict():
    """Test defaultdict with dict."""
    dd_dict = demo_defaultdict_dict()
    assert dd_dict["Joel"]["City"] == "Seattle"
    assert dd_dict["Alice"]["City"] == "Portland"


@pytest.mark.unit
def test_demo_defaultdict_custom():
    """Test defaultdict with custom factory."""
    dd_pair = demo_defaultdict_custom()
    assert dd_pair[2] == [0, 1]
    assert dd_pair[5] == [10, 0]


@pytest.mark.unit
def test_word_count_consistency():
    """Test that all word counting methods produce the same result."""
    document = ["a", "b", "a", "c", "b", "a"]
    manual = demo_word_count_manual(document)
    try_except = demo_word_count_try_except(document)
    defaultdict = demo_word_count_defaultdict(document)

    assert manual == try_except == defaultdict
