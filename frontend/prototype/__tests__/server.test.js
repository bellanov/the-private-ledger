const request = require("supertest");
const app = require("../src/server");

describe("Private Ledger Prototype Server", () => {
  describe("GET /", () => {
    it("should return the home page", async () => {
      const res = await request(app).get("/");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Prototypes");
      expect(res.text).toContain("<!DOCTYPE html>");
    });

    it("should include HTMX script tag", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain("htmx.org");
    });

    it("should contain accounts section", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain('hx-get="/accounts"');
    });

    it("should contain performance section", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain('hx-get="/performance"');
    });

    it("should contain transactions section", async () => {
      const res = await request(app).get("/");
      expect(res.text).toContain('hx-get="/transactions"');
    });
  });

  describe("GET /accounts", () => {
    it("should return accounts HTML", async () => {
      const res = await request(app).get("/accounts");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Accounts");
    });

    it("should return table structure", async () => {
      const res = await request(app).get("/accounts");
      expect(res.text).toContain("<table>");
      expect(res.text).toContain("</table>");
    });

    it("should contain account headers", async () => {
      const res = await request(app).get("/accounts");
      expect(res.text).toContain("Account ID");
      expect(res.text).toContain("Current Value");
      expect(res.text).toContain("Ownership");
      expect(res.text).toContain("Balance");
    });
  });

  describe("GET /performance", () => {
    it("should return performance HTML", async () => {
      const res = await request(app).get("/performance");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Performance");
    });

    it("should return table structure", async () => {
      const res = await request(app).get("/performance");
      expect(res.text).toContain("<table>");
      expect(res.text).toContain("</table>");
    });

    it("should contain performance fields", async () => {
      const res = await request(app).get("/performance");
      expect(res.text).toContain("Date");
      expect(res.text).toContain("Record");
      expect(res.text).toContain("Return on Investment");
      expect(res.text).toContain("Shares");
      expect(res.text).toContain("Share Price");
      expect(res.text).toContain("Total Bankroll");
      expect(res.text).toContain("Units Won");
      expect(res.text).toContain("Unit Price");
    });

    it("should contain default performance values", async () => {
      const res = await request(app).get("/performance");
      expect(res.text).toContain("2024-06-01");
      expect(res.text).toContain("Positive");
      expect(res.text).toContain("20%");
      expect(res.text).toContain("$200.00");
    });
  });

  describe("GET /transactions", () => {
    it("should return transactions HTML", async () => {
      const res = await request(app).get("/transactions");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Transactions");
    });

    it("should return table structure", async () => {
      const res = await request(app).get("/transactions");
      expect(res.text).toContain("<table>");
      expect(res.text).toContain("</table>");
    });

    it("should contain transaction headers", async () => {
      const res = await request(app).get("/transactions");
      expect(res.text).toContain("Date");
      expect(res.text).toContain("Account ID");
      expect(res.text).toContain("Type");
      expect(res.text).toContain("Amount");
    });
  });

  describe("Static Files", () => {
    it("should serve CSS files", async () => {
      const res = await request(app).get("/styles.css");
      expect(res.statusCode).toBe(200);
      expect(res.type).toContain("css");
    });
  });

  describe("Error Handling", () => {
    it("should handle 404 routes gracefully", async () => {
      const res = await request(app).get("/nonexistent");
      expect(res.statusCode).toBe(404);
    });
  });

  describe("HTMX Integration Patterns", () => {
    it("should return HTML fragments for HTMX swapping", async () => {
      const res = await request(app).get("/accounts");
      expect(res.text).toContain("id=");
      expect(res.text).not.toContain("<!DOCTYPE html>");
    });

    it("should support hx-get requests", async () => {
      const res = await request(app).get("/transactions");
      expect(res.statusCode).toBe(200);
    });

    it("should support hx-get requests", async () => {
      const res = await request(app).get("/performance");
      expect(res.statusCode).toBe(200);
    });
  });

  describe("Content Type Headers", () => {
    it("should return HTML content for home page", async () => {
      const res = await request(app).get("/");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for API endpoints", async () => {
      const res = await request(app).get("/accounts");
      expect(res.headers["content-type"]).toContain("text/html");
    });
  });
});
