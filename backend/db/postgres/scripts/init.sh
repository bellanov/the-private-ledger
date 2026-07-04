#!/bin/bash
#
# Initialize a Postgres database and seed it with data.
set -e


psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER "$TEST_USER" WITH PASSWORD 'local';
	CREATE DATABASE test_db;
	GRANT ALL PRIVILEGES ON DATABASE test_db TO $TEST_USER;
EOSQL

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -a -f /app/scripts/db/dump.sql
