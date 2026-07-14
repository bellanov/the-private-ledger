"""ThePrivateLedger API."""

from pathlib import Path

import pandas as pd
from fastapi import FastAPI

from api.domain.models.account import Account
from api.domain.models.performance import Performance
from api.domain.models.summary import Summary
from api.domain.models.transaction import Transaction

BASE_DIR = Path(__file__).resolve()

TRANSACTION = BASE_DIR.parent / "domain" / "data" / "Transaction.csv"
PERFORMANCE = BASE_DIR.parent / "domain" / "data" / "Performance.csv"
ACCOUNT = BASE_DIR.parent / "domain" / "data" / "Account.csv"

db = {
    "transactions": pd.read_csv(TRANSACTION).to_dict(orient="records"),
    "performance": pd.read_csv(PERFORMANCE).to_dict(orient="records"),
    "accounts": pd.read_csv(ACCOUNT).to_dict(orient="records"),
}

print("Initialized Mock Database:")
print(f"Account: {len(db['accounts'])} records")
print(f"Transaction: {len(db['transactions'])} records")
print(f"Performance: {len(db['performance'])} records")

app = FastAPI()


@app.get("/accounts", response_model=list[Account])
def get_accounts():
    return db["accounts"]


@app.get("/accounts/{account_id}", response_model=list[Account])
def get_account(account_id: str):
    return [
        account for account in db["accounts"] if account["account_id"] == account_id
    ]


@app.get("/performance", response_model=list[Performance])
def get_performance():
    return db["performance"]


@app.get("/performance/{date}", response_model=list[Performance])
def get_performance_for_date(date: str):
    return [record for record in db["performance"] if record["date"] == date]


@app.get("/transactions", response_model=list[Transaction])
def get_transactions():
    return db["transactions"]


@app.get("/transactions/{account_id}", response_model=list[Transaction])
def get_transactions_for_account(account_id: str):
    return [
        transaction
        for transaction in db["transactions"]
        if transaction["account_id"] == account_id
    ]


@app.get("/summary", response_model=Summary)
def get_summary():
    summary = {
        "total_bankroll": sum(
            float(account["account_balance"]) for account in db["accounts"]
        ),
        "current_share_price": "11.98",
        "initial_share_price": "10.00",
    }
    return summary
