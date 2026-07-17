#!/usr/bin/env bash
set -euo pipefail

# Run Swagger UI in Docker to visualize the OpenAPI spec.
# Prefer specs/openapy.yml as requested; fall back to specs/openapi.yaml if needed.
SPEC="${1:-openapi.yml}"
SPEC_FILE="specs/${SPEC}"
if [[ ! -f "$SPEC_FILE" ]]; then
  SPEC_FILE="specs/openapi.yaml"
  echo "Warning: OpenAPI (${SPEC}) not found. Falling back to ${SPEC_FILE}."
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Error: docker is not installed or not in PATH."
  exit 1
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Starting Swagger UI at http://localhost:8080"
echo "Using spec: ${SPEC_FILE}"

docker run --rm -p 8080:8080 \
  -e SWAGGER_JSON="/openapi/${SPEC_FILE#specs/}" \
  -v "${PROJECT_ROOT}/specs:/openapi" \
  swaggerapi/swagger-ui
