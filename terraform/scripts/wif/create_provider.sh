#!/bin/bash
#
# Create GitHub Providers.

gcloud config set project $GCP_PROJECT

echo "Attach the GitHub Repository { ${GITHUB_REPO} } to providers."

gcloud iam workload-identity-pools providers create-oidc "${GITHUB_REPO}" \
  --location="global" \
  --workload-identity-pool="${WORKLOAD_IDENTITY_POOL}" \
  --display-name="My GitHub repo Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
  --attribute-condition="assertion.repository_owner == '${GITHUB_ORG}'" \
  --issuer-uri="https://token.actions.githubusercontent.com"

sleep 3

gcloud iam workload-identity-pools providers describe "${GITHUB_REPO}" \
  --location="global" \
  --workload-identity-pool="${WORKLOAD_IDENTITY_POOL}" \
  --format="value(name)"