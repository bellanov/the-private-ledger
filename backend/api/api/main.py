"""ThePrivateLedger API."""

from fastapi import FastAPI

from api.domain.models.transaction import Transaction
from api.domain.models.performance import Performance

# TODO: Turn into an enum for transaction types
# TODO: Turn into an enum for note types
# TODO: Dynamically generate account_id
transactions = [
    Transaction(
        date="May 12, 5:45 PM",
        account_id="PL-1593",
        amount=100.0,
        type="deposit",
        shares=10.0,
        note="vemmo",
    ),
    Transaction(
        date="May 13, 7:56 AM",
        account_id="PL-4921",
        amount=50,
        type="deposit",
        shares=5,
        note="bank",
    ),
    Transaction(
        date="May 13, 7:56 AM",
        account_id="PL-1593",
        amount=100,
        type="deposit",
        shares=10,
        note="venmo",
    ),
    Transaction(
        date="May 14, 7:19 PM",
        account_id="PL-2359",
        amount=250,
        type="deposit",
        shares=25,
        note="zelle",
    ),
    Transaction(
        date="May 16, 11:25 AM",
        account_id="PL-8107",
        amount=200,
        type="deposit",
        shares=20,
        note="venmo",
    ),
    Transaction(
        date="May 16, 12:39 PM",
        account_id="PL-6044",
        amount=200,
        type="deposit",
        shares=20,
        note="cash app",
    ),
    Transaction(
        date="May 18, 5:45 PM",
        account_id="PL-7210",
        amount=100,
        type="deposit",
        shares=10,
        note="zelle",
    ),
    Transaction(
        date="May 30, 10:20 PM",
        account_id="PL-9543",
        amount=159.15,
        type="deposit",
        shares=15,
        note="apple",
    ),
    Transaction(
        date="May 31, 8:22 PM",
        account_id="PL-1593",
        amount=106.10,
        type="deposit",
        shares=10,
        note="venmo",
    ),
    Transaction(
        date="June 3rd, 12:08 PM",
        account_id="PL-8107",
        amount=106.10,
        type="deposit",
        shares=10,
        note="venmo",
    ),
    Transaction(
        date="June 13, 11:16 PM",
        account_id="PL-4834",
        amount=244.68,
        type="deposit",
        shares=20,
        note="zelle",
    ),
    Transaction(
        date="June 22, 11:11 PM",
        account_id="PL-9543",
        amount=49.64,
        type="deposit",
        shares=4,
        note="apple",
    ),
]

performance_records = [
    Performance(
        date="2026-07-11",
        record="10-5",
        share_price=12.5,
        total_bankroll=2500.0,
        units_won=3.75,
    ),
    Performance(
        date="2026-07-12",
        record="8-7",
        share_price=13.0,
        total_bankroll=2600.0,
        units_won=-1.5,
    ),
    Performance(
        date="2026-07-13",
        record="12-3",
        share_price=14.0,
        total_bankroll=2800.0,
        units_won=4.5,
    ),
    Performance(
        date="2026-07-14",
        record="9-6",
        share_price=14.5,
        total_bankroll=2900.0,
        units_won=-2.0,
    ),
]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


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
