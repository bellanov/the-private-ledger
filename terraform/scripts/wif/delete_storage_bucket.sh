#!/bin/bash
#
# Delete the Google Cloud Storage bucket for Terraform state.

gcloud storage buckets delete gs://${GCP_PROJECT}
