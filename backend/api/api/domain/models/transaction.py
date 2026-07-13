"""Transactions Model."""

from dataclasses import dataclass

from api.domain.models.pydantic import CamelCaseModel


@dataclass
class Transaction(CamelCaseModel):
    """Represents a financial transaction.

    Attributes:
        date: The date of the transaction.
        account_id: The ID of the account associated with the transaction.
        amount: The amount of the transaction.
        type: The type of the transaction (deposit, withdrawal).
        shares: The number of shares involved in the transaction.
        note: Type of note (Venmo, Bank Transfer, etc.).
    """

    date: str
    account_id: str
    amount: float
    type: str
    shares: float
    note: str
