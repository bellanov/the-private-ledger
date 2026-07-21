"""ThePrivateLedger API."""

from pathlib import Path

import pandas as pd
from fastapi import FastAPI

from api.domain.models.account import Account
from api.domain.models.ledger import Ledger
from api.domain.models.metrics import Metrics
from api.domain.models.performance import Performance
from api.domain.models.transaction import Transaction

BASE_DIR = Path(__file__).resolve()

DATA_DIR = BASE_DIR.parent / "domain" / "data"
TRANSACTION = DATA_DIR / "Transaction.csv"
PERFORMANCE = DATA_DIR / "Performance.csv"
ACCOUNT = DATA_DIR / "Account.csv"
LEDGER = DATA_DIR / "Ledger.csv"

db = {
    "transactions": pd.read_csv(TRANSACTION).to_dict(orient="records"),
    "performance": pd.read_csv(PERFORMANCE).to_dict(orient="records"),
    "accounts": pd.read_csv(ACCOUNT).to_dict(orient="records"),
    "ledgers": pd.read_csv(LEDGER).to_dict(orient="records"),
}

print("Initialized Mock Database:")
print(f"Account: {len(db['accounts'])} records")
print(f"Transaction: {len(db['transactions'])} records")
print(f"Performance: {len(db['performance'])} records")
print(f"Ledger: {len(db['ledgers'])} records")

app = FastAPI()


@app.get("/accounts", response_model=list[Account])
def get_accounts():
    return db["accounts"]


@app.get("/accounts/{account_id}", response_model=list[Account])
def get_account(account_id: str):
    return [
        account for account in db["accounts"] if account["account_id"] == account_id
    ]


@app.get("/ledgers", response_model=list[Ledger])
def get_ledgers():
    return db["ledgers"]


@app.get("/ledgers/{ledger_id}", response_model=list[Ledger])
def get_ledger(ledger_id: str):
    return [ledger for ledger in db["ledgers"] if ledger["id"] == ledger_id]


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


@app.get("/metrics", response_model=Metrics)
def get_metrics():
    total_bankroll = sum(
        float(account["account_balance"]) for account in db["accounts"]
    )
    total_shares = sum(float(account["total_shares"]) for account in db["accounts"])
    average_share_price = total_bankroll / total_shares

    metrics = {
        "total_bankroll": total_bankroll,
        "average_share_price": average_share_price,
        "total_shares": total_shares,
    }
    return metrics
