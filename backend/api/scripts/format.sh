#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
uv run isort api
uv run isort tests

echo "Formatting code base..."
uv run black api 
uv run black tests
