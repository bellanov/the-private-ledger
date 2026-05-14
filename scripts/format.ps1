#!/bin/bash
#
# Format Code Base.

# Format Imports
echo "Formatting imports..."
isort notebooks
isort tests

# Format Code
echo "Formatting code base..."
black notebooks 

# Format Tests
echo "Formatting tests..."
black tests
