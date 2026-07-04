# Sample Databases

Describe each sample database and how it's seeded.

## Postgres

The default database is a Postgres instance. It is initialized and seeded via `postgres/scripts/init.sh`, which runs `postgres/scripts/dump.sql` to create and populate the `test_data` table.

## MongoDB

A sample MongoDB database is available under the `mongodb/` directory. It is initialized and seeded via `mongodb/scripts/init.js`, which creates the `test_db` database and populates the `test_data` collection with sample data.