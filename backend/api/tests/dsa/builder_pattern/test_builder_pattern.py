"""Unit tests for builder pattern sample."""

import pytest

from samples.dsa.builder_pattern.query_builder import Query, QueryBuilder


@pytest.mark.unit
def test_query_builder_basic():
    """Test basic QueryBuilder."""
    query = QueryBuilder("users").build()
    assert isinstance(query, Query)
    assert query.table == "users"


@pytest.mark.unit
def test_query_builder_with_select():
    """Test QueryBuilder with select."""
    query = QueryBuilder("users").select("id", "name").build()
    assert query.fields == ["id", "name"]


@pytest.mark.unit
def test_query_builder_with_where():
    """Test QueryBuilder with where clause."""
    query = QueryBuilder("users").where("active = true").build()
    assert "active = true" in query.conditions


@pytest.mark.unit
def test_query_builder_with_limit():
    """Test QueryBuilder with limit."""
    query = QueryBuilder("users").limit(10).build()
    assert query.limit == 10


@pytest.mark.unit
def test_query_builder_chaining():
    """Test QueryBuilder method chaining."""
    query = (
        QueryBuilder("users")
        .select("id", "name", "email")
        .where("active = true")
        .where("age > 18")
        .limit(10)
        .build()
    )
    assert query.table == "users"
    assert query.fields == ["id", "name", "email"]
    assert len(query.conditions) == 2
    assert query.limit == 10


@pytest.mark.unit
def test_query_repr():
    """Test Query string representation."""
    query = (
        QueryBuilder("users")
        .select("id", "name")
        .where("active = true")
        .limit(5)
        .build()
    )
    query_str = str(query)
    assert "SELECT" in query_str
    assert "id, name" in query_str
    assert "WHERE" in query_str
    assert "LIMIT 5" in query_str


@pytest.mark.unit
def test_query_builder_no_table_raises_error():
    """Test that building without a table raises error."""
    builder = QueryBuilder("")
    with pytest.raises(ValueError, match="Table name is required"):
        builder.build()


@pytest.mark.unit
def test_query_with_no_fields():
    """Test Query repr with no fields (should use *)."""
    query = QueryBuilder("users").build()
    query_str = str(query)
    assert "*" in query_str
