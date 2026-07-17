# openapi-template

A template repository for OpenAPI specifications with automated validation using Spectral and GitHub Actions.

## Overview

This template provides:

- **Automated validation** of OpenAPI specs using Spectral via GitHub Actions
- **Custom ruleset** (`.spectral.yml`) with quality standards for API specifications
- **Example specs** demonstrating both valid and invalid OpenAPI documents
- **CI/CD pipeline** that enforces spec quality on every push and pull request

## Directory Structure

```
.
├── .github/workflows/
│   └── validate.yml          # GitHub Actions workflow for spec validation
├── specs/
│   └── openapi.yaml          # Example valid OpenAPI 3.0.3 specification
├── tests/
│   ├── README.md             # Documentation for the example spec violations
│   └── *.yaml                # Example specs with intentional rule violations
├── .spectral.yml             # Spectral ruleset configuration
└── README.md                 # This file
```

## Getting Started

### Prerequisites

- Node.js 20+ (for running Spectral locally)
- Docker (for visualizing OpenAPI specifications)

### Local Validation

Install Spectral CLI:

```bash
npm install -g @stoplight/spectral-cli
```

Validate your OpenAPI specs:

```bash
# Validate all specs in the specs/ directory
spectral lint specs/**/*.yaml --ruleset .spectral.yml

# Validate a specific file
spectral lint specs/openapi.yaml --ruleset .spectral.yml

# Fail on errors only (same as CI/CD)
spectral lint specs/**/*.yaml --ruleset .spectral.yml --fail-severity error

# Validate using scripts used in CICD
scripts/test.sh
scripts/test.ps1

# Visualize the specification using Docker
scripts/openapi.sh
scripts/openapi.ps1
```

### Client Generation

A series of [Generators](https://openapi-generator.tech/docs/generators) are available that let you generate boilerplate code for various clients from a valid *OpenAPI* spec:

```bash
# Python
npx @openapitools/openapi-generator-cli generate -i specs/openapi.yaml -g python -o python/

# Ruby
npx @openapitools/openapi-generator-cli generate -i specs/openapi.yaml -g ruby -o ruby/

# Ruby
npx @openapitools/openapi-generator-cli generate -i specs/openapi.yaml -g java -o java/
```

## Spectral Ruleset

The `.spectral.yml` file extends the standard `spectral:oas` ruleset and adds custom rules:

### Error-Level Rules (CI Failures)
- **operation-summary-required**: All operations must have a summary
- **operation-id-required**: All operations must have an operationId
- **operation-responses-required**: All operations must define at least one response

### Warning-Level Rules
- **operation-tags-required**: All operations should have at least one tag
- **info-contact-required**: API info must include contact information
- **info-license-required**: API info must include license information
- **servers-required**: At least one server must be defined
- **schema-description-required**: All schema properties should have descriptions

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/validate.yml`) automatically:

1. Triggers on push/PR when specs or the ruleset changes
2. Installs Spectral CLI
3. Validates all YAML files in the `specs/` directory
4. Fails the build if any error-level violations are found

The pipeline validates the `specs/` directory and ignores the `tests/` examples.

## Using This Template

1. **Add your OpenAPI specs** to the `specs/` directory
2. **Customize the ruleset** in `.spectral.yml` to match your API standards
3. **Update or remove** the example `specs/openapi.yaml` file
4. **Push your changes** and let CI/CD validate your specs automatically

## Examples

### Valid Spec
See `specs/openapi.yaml` for a complete example that passes all validation rules.

### Invalid Specs (for reference)
The `tests/` directory contains examples that intentionally violate various rules. See `tests/README.md` for details. These examples are for reference only and are not part of CI validation.
- Understanding what each rule enforces
- Training team members on API quality standards

## License

Apache 2.0
