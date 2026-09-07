#!/bin/bash
#
# Enable the necessary Google Cloud APIs.

gcloud config set project $GCP_PROJECT

gcloud services enable iamcredentials.googleapis.com \
    iam.googleapis.com