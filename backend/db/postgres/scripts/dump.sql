-- Seed the local development database with data.

-- Create Table
CREATE TABLE IF NOT EXISTS test_data (
  "id" TEXT NOT NULL,
  "name" TEXT NOT NULL,
  "email" TEXT NOT NULL,

  PRIMARY KEY ("id")
);

-- Seed
INSERT INTO test_data (id, name, email) VALUES ('userid', 'Gopher', 'hello@gopher.com');