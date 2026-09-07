#!/bin/bash
#
# Create a Google Cloud Storage bucket for Terraform state.

TIMESTAMP=$(date +%s)

gcloud config set project $GCP_PROJECT

gcloud storage buckets create gs://${GCP_PROJECT} \
    --default-storage-class=STANDARD \
    --location=US \
    --uniform-bucket-level-access \
    --public-access-prevention
