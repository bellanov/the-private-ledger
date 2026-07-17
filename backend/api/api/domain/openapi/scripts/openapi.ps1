# Run Swagger UI in Docker to visualize the OpenAPI spec.
# Prefer specs/openapy.yml as requested; fall back to specs/openapi.yaml if needed.
param(
    [int]$Port = 8080,
    [string]$Spec = "openapi.yml"
)

$specFile = "specs/$Spec"
if (-not (Test-Path -Path $specFile)) {
    $specFile = "specs/openapi.yaml"
    Write-Warning "OpenAPI ($Spec) not found. Falling back to $specFile."
}

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Error "docker is not installed or not in PATH."
    exit 1
}

$projectRoot = Split-Path -Parent $PSScriptRoot
$specName = Split-Path -Leaf $specFile

Write-Host "Starting Swagger UI at http://localhost:$Port"
Write-Host "Using spec: $specFile"

docker run --rm -p "${Port}:8080" `
  -e "SWAGGER_JSON=/openapi/$specName" `
  -v "${projectRoot}/specs:/openapi" `
  swaggerapi/swagger-ui
