#!/bin/bash
#
# Grant permissions to the Workload Identity User.

gcloud config set project $GCP_PROJECT

# Grant permissions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding "$SERVICE_ACCOUNT_EMAIL" \
  --role="roles/iam.workloadIdentityUser" \
  --member="${REPO_PRINCIPAL}"

# Grant permissions to access Terraform state
gcloud storage buckets add-iam-policy-binding "gs://$GCP_PROJECT" \
    --member="${WIF_PRINCIPAL}" \
    --role="roles/storage.objectUser"

# Grant permissions for API management
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="${WIF_PRINCIPAL}" \
  --role="roles/serviceusage.serviceUsageAdmin"

# Grant permissions for service account management
gcloud projects add-iam-policy-binding $GCP_PROJECT \
  --member="${WIF_PRINCIPAL}" \
  --role="roles/iam.serviceAccountAdmin"
