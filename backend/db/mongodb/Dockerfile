# Initialize and seed a MongoDB database.
FROM mongo:latest AS db

# Establish working directory
WORKDIR /app

# Seed the database
COPY ./scripts/init.js /docker-entrypoint-initdb.d
