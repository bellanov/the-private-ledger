
output "services" {
  description = "List of enabled services"
  value       = { for service in resource.google_project_service.service : service.id => service }
}

output "service_accounts" {
  description = "List of created service accounts"
  value       = { for sa in resource.google_service_account.service_account : sa.account_id => sa }
}