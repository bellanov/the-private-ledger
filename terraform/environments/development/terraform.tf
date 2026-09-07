terraform {
  backend "gcs" {
    bucket = "gcp-development-503118"
    prefix = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.44.0"
    }
  }
}

provider "google" {
  project = var.project_id
}