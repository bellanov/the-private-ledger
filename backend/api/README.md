# api

API layer for *ThePrivateLedger*.

# Quickstart

1. Install the required development dependencies.

   ```sh
   pip install -e ".[dev]"
   ```

2. Start the `FastAPI` server.

   ```sh
   scripts/run.ps1
   scripts/run.sh
   ```

# OpenAPI Specification

The API includes OpenAPI 3.1.0 specifications in both JSON and YAML formats:

- `openapi.json` - OpenAPI specification in JSON format
- `openapi.yaml` - OpenAPI specification in YAML format

These specifications document all API endpoints, request/response schemas, and validation rules. The specifications can be used with tools like [Swagger UI](https://swagger.io/tools/swagger-ui/), [Redoc](https://redoc.ly/), or other OpenAPI-compatible tools for interactive documentation and API testing.

## Accessing API Documentation

When the FastAPI server is running, you can access interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
