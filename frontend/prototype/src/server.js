const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:8000';

// TODO: iterate through the pages and create routes dynamically
const PAGES = {
  accounts: {
    endpoint: '/accounts',
    render: 'accounts',
  },
  performance: {
    endpoint: '/performance',
    render: 'performance',
  },
  transactions: {
    endpoint: '/transactions',
    render: 'transactions',
  },
};

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

// Index
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

// Pages
for (const [page, config] of Object.entries(PAGES)) {
  app.get(config.endpoint, async (req, res) => {
    try {
      const response = await fetch(`${API_BASE_URL}${config.endpoint}`);
      const data = await response.json();
      res.render(config.render, { [page]: data });
    } catch (error) {
      console.error(`Error fetching ${page}:`, error);
      res.status(500).send('Internal Server Error');
    }
  });

  app.get(`/${page}.html`, async (req, res) => {
    res.render(`${page}.html`);
  });
}

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
