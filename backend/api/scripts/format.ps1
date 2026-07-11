#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort api
isort tests

echo "Formatting code base..."
black api
black tests