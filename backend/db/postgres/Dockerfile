# Initialize and seed a Postgres database.
FROM postgres:latest AS db

ENV POSTGRES_TEST_USER=test_user
ENV TEST_DB=test_db

# Establish working directory
WORKDIR /app

# Seed the database
COPY ./scripts/init.sh /docker-entrypoint-initdb.d
COPY ./scripts/dump.sql ./scripts/db/dump.sql