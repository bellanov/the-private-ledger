#!/bin/bash
#
# Create GitHub Providers.

gcloud config set project $GCP_PROJECT

# Delete the GitHub OIDC Provider from the Pool
if gcloud iam workload-identity-pools providers describe github-provider \
    --location="global" \
    --workload-identity-pool="github-actions-pool" \
    --project="$GCP_PROJECT" >/dev/null 2>&1; then
    gcloud iam workload-identity-pools providers delete github-provider \
        --location="global" \
        --workload-identity-pool="github-actions-pool" \
        --project="$GCP_PROJECT" \
        --quiet
    echo "WIF provider deleted."
else
    echo "WIF provider does not exist."
fi
