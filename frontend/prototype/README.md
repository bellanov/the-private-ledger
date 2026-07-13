# HTMX Template

A template demonstrating good design patterns for developing web applications with HTMX, HTML, CSS, and Node.js/Express.

## Overview

This template showcases best practices for building dynamic web applications using HTMX, which allows you to access modern browser features directly from HTML without writing much JavaScript.

## Features

- **HTMX Integration**: Modern AJAX interactions directly from HTML
- **Express.js Server**: Lightweight backend for serving HTML and handling HTMX requests
- **Responsive Design**: Mobile-friendly UI with modern styling
- **Comprehensive Tests**: Full test coverage with Jest and Supertest
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Linting**: Code quality checking with ESLint

## Technology Stack

- **Frontend**: HTML5, CSS3, HTMX
- **Backend**: Node.js, Express.js
- **Testing**: Jest, Supertest
- **DevOps**: GitHub Actions, ESLint

## Project Structure

```
├── src/
│   └── server.js           # Express server with HTMX endpoints
├── views/
│   ├── index.html          # Home page
│   ├── todos-list.html     # Todo list template
│   ├── todo-item.html      # Individual todo item template
│   └── counter.html        # Counter value template
├── public/
│   └── styles.css          # Application styles
├── __tests__/
│   └── server.test.js      # Comprehensive test suite
├── package.json            # Project dependencies and scripts
├── jest.config.js          # Jest testing configuration
├── .eslintrc.json          # ESLint configuration
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions CI/CD workflow
└── .gitignore              # Git ignore patterns
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd html-template
```

2. Install dependencies:

```bash
npm install
```

## Usage

### Development Mode

Start the development server with auto-reload:

```bash
npm run dev
```

Then open your browser and navigate to `http://localhost:3000`

### Production Mode

Start the server:

```bash
npm start
```

The server will be available at `http://localhost:3000`

## Running Tests

Run all tests with coverage:

```bash
npm test
```

Run tests in watch mode:

```bash
npm run test:watch
```

## Linting

Check code quality:

```bash
npm run lint
```

This will automatically fix formatting issues.

## HTMX Design Patterns

This template demonstrates several key HTMX patterns:

### 1. **Dynamic Content Loading**

```html
<div hx-get="/api/todos" hx-trigger="load" hx-swap="innerHTML">Loading...</div>
```

### 2. **Form Submission**

```html
<form hx-post="/api/todos" hx-target="#todos-list" hx-swap="beforeend">
  <input name="title" placeholder="Add a todo" />
  <button type="submit">Add</button>
</form>
```

### 3. **Update Operations**

```html
<input
  type="checkbox"
  hx-put="/api/todos/1"
  hx-vals='{"completed": "true"}'
  hx-target="closest .todo-item"
  hx-swap="outerHTML"
/>
```

### 4. **Deletion**

```html
<button
  hx-delete="/api/todos/1"
  hx-target="closest .todo-item"
  hx-swap="outerHTML swap:1s"
>
  Delete
</button>
```

### 5. **Request Debouncing**

```html
<input
  type="text"
  hx-get="/api/search"
  hx-trigger="keyup changed delay:500ms"
  hx-target="#search-results"
/>
```

## API Endpoints

### GET /

Returns the home page with HTMX examples.

### GET /api/todos

Returns the list of todos as HTML.

### POST /api/todos

Creates a new todo item.

- **Parameters**: `title` (required)
- **Returns**: HTML for the new todo item

### PUT /api/todos/:id

Updates a todo item.

- **Parameters**: `completed` (true/false)
- **Returns**: Updated todo item HTML

### DELETE /api/todos/:id

Deletes a todo item.

- **Returns**: 204 No Content

### GET /api/counter

Returns the incremented counter value.

- **Parameters**: `count` (optional, defaults to 0)
- **Returns**: Plain text number

## GitHub Actions CI/CD

The project includes a GitHub Actions workflow that:

1. **Tests** on Node.js 16.x, 18.x, and 20.x
2. **Lints** code with ESLint
3. **Runs** the test suite with coverage
4. **Builds** and verifies the application starts
5. **Checks** for security vulnerabilities

Workflow triggers:

- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

## Best Practices Demonstrated

1. **Semantic HTML**: Proper use of HTML5 elements
2. **Progressive Enhancement**: Works without JavaScript
3. **REST API Design**: Proper HTTP methods and status codes
4. **Component Isolation**: Reusable HTML templates
5. **Error Handling**: Proper error status codes and messages
6. **Testing**: Comprehensive unit tests with high coverage
7. **Code Quality**: ESLint configuration for consistent code
8. **Security**: Regular dependency audits in CI/CD

## Development Workflow

1. Create a feature branch
2. Make changes and add tests
3. Run `npm test` to verify
4. Run `npm run lint` to check code quality
5. Push and create a pull request
6. GitHub Actions will automatically test and validate

## License

Licensed under Apache License 2.0. See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please ensure:

- All tests pass
- Code is properly linted
- New features include tests
- Commit messages are descriptive
