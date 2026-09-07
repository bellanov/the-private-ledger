# Terraform Deployment

_Terraform_ is used to deploy infrastructure into the `development`, `staging`, and `production` environments.

| Environment   | Description                                         |
| ------------- | --------------------------------------------------- |
| _development_ | Manages infrastructure undergoing **development**.  |
| _staging_     | Manages infrastructure undergoing **validation**.   |
| _production_  | Manages infrastructure that is **customer-facing**. |

Various _Scripts_ are available to support the deployment of infrastructure.

| Script    | Description                                                      |
| --------- | ---------------------------------------------------------------- |
| _ci_      | Scripts to **lint** and **format** the codebase.                 |
| _project_ | Scripts to establish the **Workload Identity Federation (WIF)**. |

# Workload Identity Federation (WIF)

Summary of the steps to establish WIF for Terraform.

_Prerequisites:_

It is recommended that an environment file be established with the following variables set:

- The `GCP_PROJECT` environment variable must be set to the Google Cloud *Project ID*.
- The `SERVICE_ACCOUNT` environment variable must be set to the desired name of the _Service Account_.
- The `SERVICE_ACCOUNT_EMAIL` environment variable must be set to the email of the _Service Account_.
- The `WORKLOAD_IDENTITY_PROVIDER` environment variable must be set to the desired name of the _Workload Identity Provider_.
- The `WORKLOAD_IDENTITY_POOL` environment variable must be set to the desired name of the _Workload Identity Pool_.
- The `WIF_PRINCIPAL` environment variable must be set to the desired principal for the _Workload Identity Provider_.
- The `REPO_PRINCIPAL` environment variable must be set to the desired principal for the _GitHub Repository_.

1. Create a **Service Account** in the Google Cloud project.

    ```sh
    terraform/scripts/wif/create_service_account.sh
    ```

2. Create a **Workload Identity Pool** in the Google Cloud project.

    ```sh
    terraform/scripts/wif/create_identity_pool.sh
    
    Created workload identity pool [github].
    projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github
    ```

    Be sure to grab the `PROJECT_NUMBER` from the output and set it as an `ENVIRONMENT_VARIABLE`.

3. Create a **Workload Identity Provider** in the Google Cloud project.

    ```sh
    terraform/scripts/wif/create_provider.sh
    ```

    Use this value as the workload_identity_provider value in the GitHub Actions YAML:

    ```yaml
    - uses: 'google-github-actions/auth@v3'
    with:
        project_id: 'my-project'
        workload_identity_provider: '...' # "projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github/providers/my-repo"
    ```

4. Grant the **Service Account** the necessary **roles** to access resources.

    ```sh
    terraform/scripts/wif/grant_service_account_roles.sh
    ```

5. Configure Terraform to use the **Workload Identity Federation (WIF)** for authentication.

    ```sh
    terraform/scripts/wif/configure_terraform_wif.sh
    ```
