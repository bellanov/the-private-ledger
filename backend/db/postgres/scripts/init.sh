#!/bin/bash
#
# Initialize a Postgres database and seed it with data.
set -e

# Create ORM Databases

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER test_db WITH PASSWORD 'local';
	CREATE DATABASE test_db;
	GRANT ALL PRIVILEGES ON DATABASE test_db TO test_db;
EOSQL

# Execute seeding script
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -a -f /app/scripts/db/dump.sql
