const request = require("supertest");
const app = require("../src/server");

describe("[unit] Private Ledger Prototype Server", () => {
  describe("GET /", () => {
    it("should return the home page", async () => {
      const res = await request(app).get("/");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Prototypes");
    });

    it("should include HTMX script tag", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain("htmx.org");
    });

    it("should contain menu section", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain('hx-get="/menu"');
    });

    it("should contain options section", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain('hx-get="/options"');
    });
  });

  describe("GET /menu", () => {
    it("should return menu HTML", async () => {
      const res = await request(app).get("/menu");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("menu");
    });
  });

  describe("GET /options", () => {
    it("should return options HTML", async () => {
      const res = await request(app).get("/options");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Serif");
      expect(res.text).toContain("Sans-Serif");
    });
  });


  describe("GET /accounts.html", () => {
    it("should return full accounts page", async () => {
      const res = await request(app).get("/accounts.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Accounts");
    });
  });

  describe("GET /performance.html", () => {
    it("should return full performance page", async () => {
      const res = await request(app).get("/performance.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Performance");
    });
  });

  describe("GET /transactions.html", () => {
    it("should return full transactions page", async () => {
      const res = await request(app).get("/transactions.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Transactions");
    });
  });

  describe("GET /styles.css", () => {
    it("should serve CSS files", async () => {
      const res = await request(app).get("/styles.css");
      expect(res.statusCode).toBe(200);
      expect(res.type).toContain("css");
    });
  });

  describe("GET /nonexistent", () => {
    it("should handle 404 routes gracefully", async () => {
      const res = await request(app).get("/nonexistent");
      expect(res.statusCode).toBe(404);
    });
  });
});
