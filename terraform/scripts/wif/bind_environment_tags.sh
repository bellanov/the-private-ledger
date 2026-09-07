#!/bin/bash
#
# Bind Environment Tags.

gcloud config set project $GCP_PROJECT

gcloud resource-manager tags bindings create \
    --tag-value=${GCP_ORGANIZATION}/environment/${ENVIRONMENT} \
    --parent=//://googleapis.com