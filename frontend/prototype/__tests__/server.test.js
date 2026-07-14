const request = require("supertest");
const app = require("../src/server");

describe("Private Ledger Prototype Server", () => {
  describe("[unit] GET /", () => {
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

  describe("[unit] GET /menu", () => {
    it("should return menu HTML", async () => {
      const res = await request(app).get("/menu");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("menu");
    });
  });

  describe("[unit] GET /options", () => {
    it("should return options HTML", async () => {
      const res = await request(app).get("/options");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Serif");
      expect(res.text).toContain("Sans-Serif");
    });
  });

  describe("[integration] GET /accounts", () => {
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
    });
  });

  describe("[unit] GET /accounts.html", () => {
    it("should return full accounts page", async () => {
      const res = await request(app).get("/accounts.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Accounts");
    });
  });

  describe("[integration] GET /performance", () => {
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
  });

  describe("[unit] GET /performance.html", () => {
    it("should return full performance page", async () => {
      const res = await request(app).get("/performance.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Performance");
    });
  });

  describe("[integration] GET /transactions", () => {
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

  describe("[unit] GET /transactions.html", () => {
    it("should return full transactions page", async () => {
      const res = await request(app).get("/transactions.html");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("<!doctype html>");
      expect(res.text).toContain("Transactions");
    });
  });

  describe("[unit] Static Files", () => {
    it("should serve CSS files", async () => {
      const res = await request(app).get("/styles.css");
      expect(res.statusCode).toBe(200);
      expect(res.type).toContain("css");
    });
  });

  describe("[unit] Error Handling", () => {
    it("should handle 404 routes gracefully", async () => {
      const res = await request(app).get("/nonexistent");
      expect(res.statusCode).toBe(404);
    });
  });

  describe("[integration] Content Type Headers", () => {
    it("should return HTML content for home page", async () => {
      const res = await request(app).get("/");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for partial endpoints", async () => {
      const res = await request(app).get("/accounts");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for full page endpoints", async () => {
      const res = await request(app).get("/accounts.html");
      expect(res.headers["content-type"]).toContain("text/html");
    });
  });
});
