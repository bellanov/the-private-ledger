const request = require('supertest');
const app = require('../src/server');

describe('HTMX Template Server', () => {
  describe('GET /', () => {
    it('should return the home page', async () => {
      const res = await request(app).get('/');
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain('HTMX Template');
      expect(res.text).toContain('<!DOCTYPE html>');
    });

    it('should include HTMX script tag', async () => {
      const res = await request(app).get('/');
      expect(res.text).toContain('htmx.org');
    });
  });

  describe('GET /api/todos', () => {
    it('should return todos list HTML', async () => {
      const res = await request(app).get('/api/todos');
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain('Learn HTMX');
      expect(res.text).toContain('Build a project');
      expect(res.text).toContain('Deploy to production');
    });

    it('should contain todo items with checkboxes', async () => {
      const res = await request(app).get('/api/todos');
      expect(res.text).toContain('type="checkbox"');
      expect(res.text).toContain('hx-put="/api/todos/');
    });

    it('should contain delete buttons', async () => {
      const res = await request(app).get('/api/todos');
      expect(res.text).toContain('hx-delete="/api/todos/');
      expect(res.text).toContain('Delete');
    });
  });

  describe('POST /api/todos', () => {
    it('should return 400 if title is missing', async () => {
      const res = await request(app)
        .post('/api/todos')
        .send('');
      expect(res.statusCode).toBe(400);
      expect(res.text).toContain('Title is required');
    });

    it('should add a new todo and return HTML', async () => {
      const res = await request(app)
        .post('/api/todos')
        .set('Content-Type', 'application/x-www-form-urlencoded')
        .send('title=Test Todo');
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain('todo-item');
      expect(res.text).toContain('type="checkbox"');
    });

    it('should return a todo item with delete button', async () => {
      const res = await request(app)
        .post('/api/todos')
        .set('Content-Type', 'application/x-www-form-urlencoded')
        .send('title=Another Todo');
      expect(res.text).toContain('hx-delete="/api/todos/');
      expect(res.text).toContain('Delete');
    });
  });

  describe('PUT /api/todos/:id', () => {
    it('should return 200 and update todo', async () => {
      const res = await request(app)
        .put('/api/todos/1')
        .send({ completed: 'true' });
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain('todo-item');
    });

    it('should return HTML for a todo with checkbox', async () => {
      const res = await request(app)
        .put('/api/todos/1')
        .send({ completed: 'true' });
      expect(res.text).toContain('type="checkbox"');
      expect(res.text).toContain('hx-put="/api/todos/');
    });
  });

  describe('DELETE /api/todos/:id', () => {
    it('should return 204 No Content', async () => {
      const res = await request(app).delete('/api/todos/1');
      expect(res.statusCode).toBe(204);
    });
  });

  describe('GET /api/counter', () => {
    beforeEach(() => {
      app.resetCounter();
    });

    it('should increment counter by the count parameter', async () => {
      const res = await request(app).get('/api/counter?count=1');
      expect(res.statusCode).toBe(200);
      expect(res.text).toBe('1');
    });

    it('should handle decrement (negative count)', async () => {
      // Start with 5
      await request(app).get('/api/counter?count=5');
      // Then decrement by 2
      const res = await request(app).get('/api/counter?count=-2');
      expect(res.statusCode).toBe(200);
      expect(res.text).toBe('3');
    });

    it('should handle default count of 0 (no change)', async () => {
      const res = await request(app).get('/api/counter');
      expect(res.statusCode).toBe(200);
      expect(res.text).toBe('0');
    });

    it('should return a string response', async () => {
      const res = await request(app).get('/api/counter?count=0');
      expect(typeof res.text).toBe('string');
    });
  });

  describe('Static Files', () => {
    it('should serve CSS files', async () => {
      const res = await request(app).get('/styles.css');
      expect(res.statusCode).toBe(200);
      expect(res.type).toContain('css');
    });
  });

  describe('Error Handling', () => {
    it('should handle 404 routes gracefully', async () => {
      const res = await request(app).get('/nonexistent');
      expect(res.statusCode).toBe(404);
    });
  });

  describe('HTMX Integration Patterns', () => {
    it('should support hx-put requests for updates', async () => {
      const res = await request(app)
        .put('/api/todos/1')
        .send({ completed: 'true' });
      expect(res.statusCode).toBe(200);
    });

    it('should support hx-delete requests for removal', async () => {
      const res = await request(app).delete('/api/todos/1');
      expect(res.statusCode).toBe(204);
    });

    it('should return HTML fragments for HTMX swapping', async () => {
      const res = await request(app).get('/api/todos');
      expect(res.text).toContain('id=');
      expect(res.text).not.toContain('<!DOCTYPE html>');
    });

    it('should support form-based interactions', async () => {
      const res = await request(app)
        .post('/api/todos')
        .set('Content-Type', 'application/x-www-form-urlencoded')
        .send('title=Form Test');
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain('todo-item');
    });
  });

  describe('Content Type Headers', () => {
    it('should return HTML content for home page', async () => {
      const res = await request(app).get('/');
      expect(res.headers['content-type']).toContain('text/html');
    });

    it('should return text content for API endpoints', async () => {
      const res = await request(app).get('/api/counter');
      expect(res.statusCode).toBe(200);
    });
  });
});
