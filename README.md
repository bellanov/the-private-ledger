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
