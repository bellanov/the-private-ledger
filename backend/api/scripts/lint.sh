#!/bin/bash
#
# Lint Code Base.

# Lint Code
echo "Linting code base..."

# stop the build if there are Python syntax errors or undefined names
uv run flake8 api --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
uv run flake8 api --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Check for code formatting issues
uv run black --check api
uv run isort --check api

echo "Linting tests..."

# stop the build if there are Python syntax errors or undefined names
uv run flake8 tests --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
uv run flake8 tests --count --max-complexity=10 --max-line-length=127 --statistics
# Check test formatting issues
uv run black --check tests
uv run isort --check tests
