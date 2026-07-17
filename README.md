# The Private Ledger

Solution for creating and managing *Ledgers*.

# Requirements

- [Docker Compose](https://docs.docker.com/compose/)
- [NodeJS 22+](https://nodejs.org/en)
- [Python 3.12+](https://www.python.org/)

## Development

The project utilizes **Docker** to containerize various aspects of the *frontend* / *backend*, and **Docker Compose** to deploy them locally.

![Local Development Diagram](./diagrams/Local.svg)

### Project Structure

Applications are distributed across the `backend` and `frontend` directories.

```sh
├───backend
│   ├───api
│   └───db
│       ├───mongodb
│       └───postgres
├───diagrams
├───frontend
│   ├───mobile
│   └───web
└───scripts
```

| Directory | Description |
| -------- | -------- | 
| *backend*   | Contains applications deployed to the backend.   | 
| *diagrams*   | Contains architectural diagrams.   | 
| *frontend*   | Contains applications deployed to the frontend.   | 
| *scripts*   | Contains scripts to help accelerate development.  | 

## API

### Models

Summary of the models used within the `api` project. The elements are translated into `camelCase` when exposed.

[OpenAPI Specification: YAML](https://github.com/bellanov/the-private-ledger/blob/main/backend/api/openapi.yaml)

[OpenAPI Specification: JSON](https://github.com/bellanov/the-private-ledger/blob/main/backend/api/openapi.json)

![Models](./diagrams/Models.svg)