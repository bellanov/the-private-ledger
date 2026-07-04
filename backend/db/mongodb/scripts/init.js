// Initialize and seed a MongoDB database with data.

db = db.getSiblingDB("test_db");

db.createCollection("test_data");

db.test_data.insertOne({
  id: "userid",
  name: "Gopher",
  email: "hello@gopher.com"
});
