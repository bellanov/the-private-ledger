#!/bin/bash
#
# Create GitHub Identity Pool.

gcloud config set project $GCP_PROJECT

# Create a Workload Identity Pool
gcloud iam workload-identity-pools delete "${WORKLOAD_IDENTITY_POOL}" \
    --project="$GCP_PROJECT" \
    --location="global" \
    --quiet
