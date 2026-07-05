# Builder Pattern

Summary of the *Builder Pattern* and its usage.

## Description

The **Builder Pattern** constructs complex objects step-by-step, separating the construction logic from the final representation. It is especially useful when an object requires many optional parameters or multi-step configuration.

**Key Benefits:**

- *Readable construction* — method chaining reads like natural language
- *Validation at build time* — catch missing or invalid config in one place before the object is created
- *Immutable result* — the final object is separate and decoupled from its builder
- *Common real-world uses:* SQL/HTTP request builders, test data factories, and configuration objects.

## Solutions

### HTTP Request Builder (`builder.py`)

Uses an `HttpRequestBuilder` to incrementally configure an `HttpRequest` object. Each builder method returns `self` to enable fluent method chaining, and `build()` validates and produces the final immutable object.

```python
get_request = (
    HttpRequestBuilder("GET", "https://api.example.com/users")
    .header("Accept", "application/json")
    .header("Authorization", "Bearer token123")
    .param("page", "1")
    .param("limit", "25")
    .timeout(10)
    .build()
)
```

Validation is centralized in `build()`, so invalid configurations are caught before the object is created.

```python
def build(self) -> HttpRequest:
    if not self._url:
        raise ValueError("URL is required")
    if self._method in ("GET", "DELETE") and self._body:
        raise ValueError(f"{self._method} requests should not have a body")
    return HttpRequest(...)
```

Adding support for a new configuration option is as simple as adding a new method to the builder.

```python
def timeout(self, seconds: int) -> "HttpRequestBuilder":
    self._timeout = seconds
    return self
```

### SQL Query Builder (`query_builder.py`)

Uses a `QueryBuilder` to compose a SQL `SELECT` statement step-by-step. Calling `.select()`, `.where()`, and `.limit()` accumulates state, and `.build()` assembles the final `Query` object.

```python
query = (
    QueryBuilder("users")
    .select("id", "name", "email")
    .where("active = true")
    .where("age > 18")
    .limit(10)
    .build()
)

print(query)
# Output: SELECT id, name, email FROM users WHERE active = true AND age > 18 LIMIT 10
```

Multiple `.where()` calls are additive — each appends a condition that is joined with `AND` at build time, demonstrating how the builder pattern naturally handles repeated or variadic configuration.

```python
def where(self, condition):
    self._conditions.append(condition)
    return self
```
