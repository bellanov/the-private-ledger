#!/bin/bash
#
# Create Environment Tags.

gcloud config set project $GCP_PROJECT

gcloud resource-manager tags keys create environment \
    --parent=organizations/${GCP_ORGANIZATION} \
    --description="Deployment environment indicator"

gcloud resource-manager tags keys list --parent=organizations/${GCP_ORGANIZATION}