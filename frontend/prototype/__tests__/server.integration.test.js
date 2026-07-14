const request = require("supertest");
const app = require("../src/server");

describe("[integration] Private Ledger Prototype Server", () => {
  describe("GET /summary", () => {
    it("should return summary HTML", async () => {
      const res = await request(app).get("/summary");
      expect(res.statusCode).toBe(200);
      expect(res.text).toContain("Summary");
    });

    it("should return table structure", async () => {
      const res = await request(app).get("/summary");
      expect(res.text).toContain("<table>");
      expect(res.text).toContain("</table>");
    });

    it("should contain summary fields", async () => {
      const res = await request(app).get("/summary");
      expect(res.text).toContain("Current Share Price");
      expect(res.text).toContain("Initial Share Price");
      expect(res.text).toContain("Total Bankroll");
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

  describe("Content Type Headers", () => {
    it("should return HTML content for home page", async () => {
      const res = await request(app).get("/");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for partial endpoints", async () => {
      const res = await request(app).get("/summary");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for accounts partial", async () => {
      const res = await request(app).get("/accounts");
      expect(res.headers["content-type"]).toContain("text/html");
    });

    it("should return HTML content for full page endpoints", async () => {
      const res = await request(app).get("/summary.html");
      expect(res.headers["content-type"]).toContain("text/html");
    });
  });
});
