const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// In-memory state (for demo purposes only)
let counterState = 0;

// Middleware
app.use(express.static(path.join(__dirname, '../public')));
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'html');
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

// API: Get todos list
app.get('/api/todos', (req, res) => {
  const todos = [
    { id: 1, title: 'Learn HTMX', completed: true },
    { id: 2, title: 'Build a project', completed: false },
    { id: 3, title: 'Deploy to production', completed: false }
  ];
  res.render('todos-list.html', { todos });
});

// API: Add a new todo
app.post('/api/todos', (req, res) => {
  const { title } = req.body;
  if (!title) {
    return res.status(400).send('Title is required');
  }
  
  // In a real app, this would save to a database
  const newTodo = {
    id: Date.now(),
    title: title,
    completed: false
  };
  
  res.render('todo-item.html', { todo: newTodo });
});

// API: Toggle todo completion
app.put('/api/todos/:id', (req, res) => {
  const { id } = req.params;
  const { completed } = req.body;
  
  // In a real app, this would update the database
  const todo = {
    id: parseInt(id),
    title: `Todo ${id}`,
    completed: completed === 'true'
  };
  
  res.render('todo-item.html', { todo });
});

// API: Delete a todo
app.delete('/api/todos/:id', (req, res) => {
  // In a real app, this would delete from the database
  res.status(204).send();
});

// API: Get counter value (for AJAX interactions)
app.get('/api/counter', (req, res) => {
  const increment = parseInt(req.query.count) || 0;
  counterState += increment;
  res.send(counterState.toString());
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

// Export reset function for testing
app.resetCounter = () => {
  counterState = 0;
};

module.exports = app;
