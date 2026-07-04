# svelte-template

Template for general *Svelte* development.

## Prerequisites

A combination of [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/) are used to replicate a *production-like* environment locally. This improves the developer experience, as the developer can be confident that the functionality being developed locally will seamlessly integrate into production environments.

### Docker / Docker Compose

**Docker** is utilized to ensure that deployed resources are ephemeral as development is being conducted. This ensures that current development will be independent and unaffected by previous development.

## Development Workflow

Rapid development within this template revolves around the provided scripts within the `scripts/` directory.

| Script                      | Description |
| -----------                 | ----------- |
| **scripts/build.sh**        | Installs dependencies and builds new Docker images after code changes. |
| **scripts/deploy.sh**       | Spins up new containers and a test database. |
| **scripts/teardown.sh**     | Tears down existing resources. |
| **scripts/purge.sh**        | Cleans up existing containers and start from a clean, pristine state. |

### Tiers

The project is split across two tiers, a **frontend** and a **database**. The frontend directory contains a React project scaffolded by Remix. The db directory contains a **Postgres** database that is seeded on startup with the contents of the `dump.sql` file.

The deployment of these two tiers is managed by Docker Compose via the configuration in `docker-compose.yml`.

### Steps

1. Make changes to either the frontend or database. Execute the build script to generate new Docker images containing the changes.

```sh

# Build
scripts/build.sh

```

2. Once new Docker images are available, they can be deployed via Docker Compose.

```sh

# Deploy
scripts/deploy.sh

# Application Access
# The application is accessible locally on port 8080.
# http://localhost:8080

# PHPMyAdmin Access
# A PHPMyAdmin instance is accessible locally on port 8081. 
# http://localhost:8081
```

3. Tear down existing resources to make room for future changes.

```sh

# Teardown
scripts/teardown.sh

```

4. To purge existing containers and get back to a pristine state, the purge script will clean up existing Docker images.

```sh

# Purge
scripts/purge.sh

```