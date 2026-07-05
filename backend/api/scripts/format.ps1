#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort samples
isort tests

echo "Formatting code base..."
black samples
black tests