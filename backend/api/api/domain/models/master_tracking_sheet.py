"""Master Tracking Sheet Model."""

from dataclasses import dataclass


@dataclass
class MasterTrackingSheet:
    """Represents a master tracking sheet.

    Attributes:
        date: The date of the transaction.
        account_id: The ID of the account associated with the transaction.
        amount: The amount of the transaction.
        type: The type of the transaction (deposit, withdrawal).
        shares: The number of shares involved in the transaction.
        note: Type of note (Venmo, Bank Transfer, etc.).
    """

    account_id: str
    account_balance: float
    current_value: float
    shares_owned: float
    ownership: float
    return_on_investment: dict[str, str]
