
resource "google_project_service" "service" {
  for_each = toset(local.services)
  project  = var.project_id
  service  = each.key
}

resource "google_service_account" "service_account" {
  for_each     = local.service_accounts
  project      = var.project_id
  account_id   = each.key
  description  = each.value.description
  display_name = each.value.description
}

# TODO: Add a policy to restrict the maximum age of service account keys to enhance security.
# resource "google_org_policy_policy" "allowed_sa_key_age" {
#   name   = "organizations/YOUR_ORG_ID/policies/iam.allowedServiceAccountKeyAge"
#   parent = "organizations/YOUR_ORG_ID"

#   spec {
#     rules {
#       values {
#         allowed_values = ["in:30d"] # Set your desired max key age limit (e.g., 30 days)
#       }
#     }
#   }
# }

locals {
  services = []

  # TODO: Dynamically generate service accounts and roles based on a map of service accounts and their roles
  service_accounts = {
    developer = {
      description = "Developer Service Account"
      roles = [
        "roles/iam.serviceAccountUser",
        "roles/iam.serviceAccountTokenCreator",
        "roles/iam.workloadIdentityUser",
      ]
    }

    tester = {
      description = "Tester Service Account"
      roles = [
        "roles/iam.serviceAccountUser"
      ]
    }

    operations = {
      description = "Operations Service Account"
      roles       = []
    }
  }
}