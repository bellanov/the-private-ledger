"""Transactions Model."""

from pydantic import Field

from api.domain.models.pydantic import CamelCaseModel


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

    date: str = Field(
        ..., pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(.\d+)?(Z|[+-]\d{2}:\d{2})?$"
    )
    account_id: str = Field(..., pattern=r"^PL-[a-f0-9]{32}$")
    amount: float
    type: str = Field(..., pattern=r"^(DEPOSIT|WITHDRAWAL)$")
    shares: float
    note: str = Field(..., pattern=r"^(venmo|bank|check|cashapp|zelle|apple)$")
