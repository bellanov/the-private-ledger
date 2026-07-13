const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:8000';
// TODO: iterate through the pages and create routes dynamically
const PAGES = ['accounts', 'index', 'performance', 'transactions'];

// Middleware
app.use(express.static(path.join(__dirname, '../public')));
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../views'));

// Custom view engine to render HTML files
app.engine('html', (filepath, options, callback) => {
  const fs = require('fs');
  fs.readFile(filepath, 'utf8', (err, content) => {
    if (err) return callback(err);
    return callback(null, content);
  });
});

// Routes

// Home page
app.get('/', (req, res) => {
  res.render('index.html');
});

// Menu
app.get('/menu', async (req, res) => {
  res.render('menu');
});

// Options
app.get('/options', async (req, res) => {
  res.render('options');
});

// Accounts
app.get('/accounts', async (req, res) => {
  const response = await fetch(`${API_BASE_URL}/accounts`);
  const accounts = await response.json();
  res.render('accounts', { accounts });
});

app.get('/accounts.html', async (req, res) => {
  res.render('accounts.html');
});

// Performance
app.get('/performance', async (req, res) => {
  const response = await fetch(`${API_BASE_URL}/performance`);
  const performance = await response.json();
  res.render('performance', { performance });
});

app.get('/performance.html', async (req, res) => {
  res.render('performance.html');
});

// Transactions
app.get('/transactions', async (req, res) => {
  const response = await fetch(`${API_BASE_URL}/transactions`);
  const transactions = await response.json();
  res.render('transactions', { transactions });
});

app.get('/transactions.html', async (req, res) => {
  res.render('transactions.html');
});

// Error handling middleware
// eslint-disable-next-line no-unused-vars
app.use((err, req, res, next) => {
  console.error(err); // eslint-disable-line no-console
  res.status(500).send('Internal Server Error');
});

// Start server
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Prototype server running on http://localhost:${PORT}`); // eslint-disable-line no-console
  });
}

module.exports = app;
