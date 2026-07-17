#!/bin/bash
#
# Validate OpenAPI specifications using Spectral.

# Validate all specs in the specs/ directory
spectral lint specs/**/*.yaml --ruleset .spectral.yml

# Validate a specific file
spectral lint specs/openapi.yaml --ruleset .spectral.yml

# Fail on errors only (same as CI/CD)
spectral lint specs/**/*.yaml --ruleset .spectral.yml --fail-severity error

# Simulate Failures
spectral lint tests/**/*.yaml --ruleset .spectral.yml --fail-severity error
