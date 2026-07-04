-- Seed the local development database with data.

CREATE TABLE IF NOT EXISTS theprivateledger (
  "id" TEXT NOT NULL,
  "name" TEXT NOT NULL,
  "email" TEXT NOT NULL,

  PRIMARY KEY ("id")
);

-- Seed
INSERT INTO theprivateledger (id, name, email) VALUES ('userid', 'Gopher', 'hello@gopher.com');