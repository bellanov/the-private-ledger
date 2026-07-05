"""Unit tests for type_annotations sample."""

import pytest

from samples.type_annotations.type_annotations import (
    add_typed,
    add_untyped,
    apply_operation,
    create_mapping,
    demo_dict_type_annotation,
    demo_list_type_annotation,
    find_first_positive,
    flexible_add,
    process_list,
)


@pytest.mark.unit
def test_add_untyped_with_integers():
    """Test untyped function with integers."""
    assert add_untyped(10, 5) == 15


@pytest.mark.unit
def test_add_untyped_with_lists():
    """Test untyped function with lists."""
    assert add_untyped([1, 2], [3]) == [1, 2, 3]


@pytest.mark.unit
def test_add_untyped_with_strings():
    """Test untyped function with strings."""
    assert add_untyped("hi ", "there") == "hi there"


@pytest.mark.unit
def test_add_typed():
    """Test typed function."""
    assert add_typed(10, 5) == 15


@pytest.mark.unit
def test_process_list():
    """Test list type annotation."""
    result = process_list([1, 2, 3, 4, 5])
    assert result == 15


@pytest.mark.unit
def test_process_list_empty():
    """Test list type annotation with empty list."""
    result = process_list([])
    assert result == 0


@pytest.mark.unit
def test_create_mapping():
    """Test dict type annotation."""
    mapping = create_mapping(["a", "b", "c"], [1, 2, 3])
    assert mapping == {"a": 1, "b": 2, "c": 3}


@pytest.mark.unit
def test_find_first_positive():
    """Test Optional return type with positive number."""
    result = find_first_positive([-1, -2, 3, -4])
    assert result == 3


@pytest.mark.unit
def test_find_first_positive_not_found():
    """Test Optional return type when not found."""
    result = find_first_positive([-1, -2, -3])
    assert result is None


@pytest.mark.unit
def test_flexible_add_integers():
    """Test Union type with integers."""
    assert flexible_add(10, 5) == 15


@pytest.mark.unit
def test_flexible_add_floats():
    """Test Union type with floats."""
    assert flexible_add(10.5, 5.5) == 16.0


@pytest.mark.unit
def test_flexible_add_mixed():
    """Test Union type with mixed int and float."""
    assert flexible_add(10, 5.5) == 15.5


@pytest.mark.unit
def test_apply_operation():
    """Test Callable type annotation."""
    add_op = lambda x, y: x + y
    result = apply_operation(add_op, 3, 7)
    assert result == 10


@pytest.mark.unit
def test_apply_operation_multiply():
    """Test Callable type annotation with multiplication."""
    multiply = lambda x, y: x * y
    result = apply_operation(multiply, 3, 7)
    assert result == 21


@pytest.mark.unit
def test_demo_list_type_annotation():
    """Test variable list type annotation."""
    numbers = demo_list_type_annotation()
    assert numbers == [1, 2, 3, 4, 5]


@pytest.mark.unit
def test_demo_dict_type_annotation():
    """Test variable dict type annotation."""
    ages = demo_dict_type_annotation()
    assert ages == {"Alice": 25, "Bob": 30}
