"""Unit tests for generators sample."""

import itertools

import pytest

from samples.generators.generators import (
    build_pipeline,
    chain_sources,
    counter,
    fibonacci,
    filter_short,
    first_match,
    flatten,
    parse_lines,
    read_chunks,
    running_average,
    sum_of_squares,
    to_uppercase,
)


@pytest.mark.unit
def test_read_chunks():
    """Test basic generator function."""
    chunks = list(read_chunks("Hello, World!", size=4))
    assert chunks == ["Hell", "o, W", "orld", "!"]


@pytest.mark.unit
def test_read_chunks_with_default_size():
    """Test read_chunks with default size."""
    chunks = list(read_chunks("Hello"))
    assert len(chunks) == 2  # "Hell" and "o"


@pytest.mark.unit
def test_parse_lines():
    """Test parse_lines generator."""
    lines = ["  hello  ", "  ", "world"]
    result = list(parse_lines(lines))
    assert result == ["hello", "world"]


@pytest.mark.unit
def test_to_uppercase():
    """Test to_uppercase generator."""
    lines = ["hello", "world"]
    result = list(to_uppercase(lines))
    assert result == ["HELLO", "WORLD"]


@pytest.mark.unit
def test_filter_short():
    """Test filter_short generator."""
    lines = ["hi", "hello", "world", "a"]
    result = list(filter_short(lines, min_len=5))
    assert result == ["hello", "world"]


@pytest.mark.unit
def test_build_pipeline():
    """Test generator pipeline."""
    raw = ["  hello  ", "hi", "  WORLD  ", "", "  python  "]
    result = list(build_pipeline(raw))
    # After parse_lines, to_uppercase, and filter_short (min_len=5)
    assert "HELLO" in result
    assert "WORLD" in result
    assert "PYTHON" in result


@pytest.mark.unit
def test_fibonacci_first_10():
    """Test Fibonacci generator."""
    fibs = list(itertools.islice(fibonacci(), 10))
    assert fibs == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


@pytest.mark.unit
def test_counter_basic():
    """Test counter generator."""
    counts = list(itertools.islice(counter(0, 1), 5))
    assert counts == [0, 1, 2, 3, 4]


@pytest.mark.unit
def test_counter_with_start_and_step():
    """Test counter with custom start and step."""
    counts = list(itertools.islice(counter(5, 2), 6))
    assert counts == [5, 7, 9, 11, 13, 15]


@pytest.mark.unit
def test_running_average():
    """Test two-way generator communication."""
    gen = running_average()
    next(gen)  # prime the coroutine
    avg1 = gen.send(10)
    avg2 = gen.send(20)
    avg3 = gen.send(30)

    assert avg1 == 10.0
    assert avg2 == 15.0
    assert abs(avg3 - 20.0) < 0.01  # 20.0 with floating point tolerance


@pytest.mark.unit
def test_flatten():
    """Test flatten generator."""
    nested = [1, [2, 3], [4, [5, 6]], 7]
    result = list(flatten(nested))
    assert result == [1, 2, 3, 4, 5, 6, 7]


@pytest.mark.unit
def test_flatten_empty():
    """Test flatten with empty list."""
    result = list(flatten([]))
    assert result == []


@pytest.mark.unit
def test_chain_sources():
    """Test chain_sources generator."""
    result = list(chain_sources([1, 2], [3, 4], [5]))
    assert result == [1, 2, 3, 4, 5]


@pytest.mark.unit
def test_sum_of_squares():
    """Test generator expression for sum of squares."""
    result = sum_of_squares(6)
    assert result == 55  # 0+1+4+9+16+25


@pytest.mark.unit
def test_first_match():
    """Test generator expression for first match."""
    words = ["apple", "avocado", "banana", "apricot"]
    result = first_match(words, "ap")
    assert result == "apple"


@pytest.mark.unit
def test_first_match_no_match():
    """Test first_match with no matches."""
    words = ["apple", "avocado", "banana", "apricot"]
    result = first_match(words, "z")
    assert result is None
