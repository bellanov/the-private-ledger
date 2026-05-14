#!/bin/bash
#
# Lint Code Base.

# Lint Code
echo "Linting code base..."

# stop the build if there are Python syntax errors or undefined names
flake8 notebooks --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 notebooks --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Check for code formatting issues
black --check notebooks
isort --check notebooks

# Lint Tests
echo "Linting tests..."

# stop the build if there are Python syntax errors or undefined names
flake8 tests --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Check test formatting issues
black --check tests
isort --check tests
