#!/bin/bash
#
# Delete Deployment Service Account.

SERVICE_ACCOUNT=$1

gcloud config set project $GCP_PROJECT
gcloud iam service-accounts delete "$SERVICE_ACCOUNT" --project "$GCP_PROJECT"
