const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

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

// Accounts
app.get('/accounts', (req, res) => {
  const accounts = [
    { accountId: 'ACC001', accountBalance: 1500.00, currentValue: 1500.00, sharesOwned: 100, ownership: '10%', returnOnInvestment: '20%' },
    { accountId: 'ACC002', accountBalance: 5000.00, currentValue: 5000.00, sharesOwned: 200, ownership: '20%', returnOnInvestment: '25%' }
  ];
  res.render('accounts', { accounts });
});

// Performance
app.get('/performance', (req, res) => {
  const performance = [
    { date: '2024-06-01', record: 'Positive', shares: 100, sharePrice: 12.00, returnOnInvestment: 200.00, totalBankroll: 1200.00, unitsWon: 10, unitPrice: 20.00 },
    { date: '2024-06-02', record: 'Negative', shares: 50, sharePrice: 10.00, returnOnInvestment: -50.00, totalBankroll: 1150.00, unitsWon: 5, unitPrice: 15.00 }
  ];
  res.render('performance', { performance: performance });
});

// Transactions
app.get('/transactions', (req, res) => {
  const transactions = [
    { date: '2024-06-01', accountId: 'ACC001', type: 'Deposit', amount: 500.00, shares: 100 },
    { date: '2024-06-02', accountId: 'ACC002', type: 'Withdrawal', amount: 200.00, shares: 50 }
  ];
  res.render('transactions', { transactions });
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
    console.log(`HTMX Template server running on http://localhost:${PORT}`); // eslint-disable-line no-console
  });
}

module.exports = app;
