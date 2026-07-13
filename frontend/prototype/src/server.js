const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.static(path.join(__dirname, "../public")));
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "html");
app.set("views", path.join(__dirname, "../views"));

// Custom view engine to render HTML files
app.engine("html", (filepath, options, callback) => {
  const fs = require("fs");
  fs.readFile(filepath, "utf8", (err, content) => {
    if (err) return callback(err);
    return callback(null, content);
  });
});

// Routes

// Home page
app.get("/", (req, res) => {
  res.render("index.html");
});

// Accounts
app.get("/accounts", (req, res) => {
  res.render("accounts.html");
});

// Performance
app.get("/performance", (req, res) => {
  res.render("performance.html");
});

// Transactions
app.get("/transactions", (req, res) => {
  res.render("transactions.html");
});

// Error handling middleware
// eslint-disable-next-line no-unused-vars
app.use((err, req, res, next) => {
  console.error(err); // eslint-disable-line no-console
  res.status(500).send("Internal Server Error");
});

// Start server
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`HTMX Template server running on http://localhost:${PORT}`); // eslint-disable-line no-console
  });
}

module.exports = app;
