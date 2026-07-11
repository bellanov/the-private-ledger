"""ThePrivateLedger API."""

from datetime import date

from fastapi import FastAPI

from api.domain.models.transaction import Transaction
from api.domain.models.performance import Performance

# TODO: Turn into an enum for transaction types
# TODO: Turn into an enum for note types
# TODO: Dynamically generate account_id
transactions = []

# TODO: Dynamically generate performance records
# TODO: Add validation wherever necessary
performance_records = []

# TODO: Dynamically generate account records
# TODO: Add validation wherever necessary
accounts = []

app = FastAPI()


@app.get("/accounts")
def get_accounts():
    return {"accounts": accounts}


@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    return [
        account
        for account in accounts
        if account.account_id == account_id
    ]

@app.get("/performance")
def get_performance():
    return {"performance_records": performance_records}


@app.get("/performance/{date}")
def get_performance_for_date(date: str):
    return [
        record
        for record in performance_records
        if record.date == date
    ]


@app.get("/transactions")
def get_transactions():
    return {"transactions": transactions}


@app.get("/transactions/{account_id}")
def get_transactions_for_account(account_id: str):
    return [
        transaction
        for transaction in transactions
        if transaction.account_id == account_id
    ]
