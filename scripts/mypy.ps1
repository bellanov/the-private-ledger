#!/bin/bash
#
# Execute Type Checking.

echo "Executing Type Checking..."
mypy --strict notebooks/ tests/
