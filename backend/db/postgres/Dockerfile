# Initialize and seed a Postgres database.
FROM postgres:latest AS db

# Establish working directory
WORKDIR /app

# Seed the database
COPY ./scripts/init.sh /docker-entrypoint-initdb.d
COPY ./scripts/dump.sql ./scripts/db/dump.sql