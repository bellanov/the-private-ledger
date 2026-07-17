# Invalid OpenAPI Spec Examples

This directory contains OpenAPI specification examples that intentionally violate the Spectral rules defined in `.spectral.yml`. These examples demonstrate what types of issues the validation will catch.

## Examples

### Error-Level Violations

These violations will cause the CI/CD pipeline to fail:

- **`missing-operation-summary.yaml`** - Operation missing `summary` field
- **`missing-operation-id.yaml`** - Operation missing `operationId` field
- **`missing-responses.yaml`** - Operation missing `responses` object
- **`multiple-errors.yaml`** - Multiple error-level violations in one spec

### Warning-Level Violations

These violations will produce warnings but won't fail the pipeline:

- **`missing-info-fields.yaml`** - Missing `info.contact` and `info.license`
- **`missing-servers.yaml`** - Missing `servers` array
- **`missing-tags.yaml`** - Operation missing `tags` array
- **`missing-schema-descriptions.yaml`** - Schema properties missing `description` fields

## Testing

These examples are provided for reference and documentation purposes. They are not validated by the CI/CD workflow in `.github/workflows/validate.yml`, which only checks the `specs/` directory.
