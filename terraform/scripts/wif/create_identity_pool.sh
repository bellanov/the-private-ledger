#!/bin/bash
#
# Create GitHub Identity Pool.

TIMESTAMP=$(date +%s)

gcloud config set project $GCP_PROJECT

gcloud iam workload-identity-pools create "${WORKLOAD_IDENTITY_POOL}" \
  --location="global" \
  --display-name="GitHub Actions Pool"

gcloud iam workload-identity-pools describe "${WORKLOAD_IDENTITY_POOL}" \
  --location="global" \
  --format="value(name)"
