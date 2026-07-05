#!/bin/bash
#
# Execute unit tests.

set -e

echo "Executing Unit Tests..."
coverage run -m pytest tests/

echo "Generating Report..."
coverage report -m

echo "Build HTML Report..."
coverage html
