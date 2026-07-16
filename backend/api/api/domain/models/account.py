"""Account Model."""

from pydantic import Field

from api.domain.models.pydantic import CamelCaseModel


class Account(CamelCaseModel):
    """Represents an account.

    Attributes:
        account_id: The ID of the account associated with the transaction.
        account_balance: The balance of the account.
        current_value: The current value of the account.
        total_shares: The total number of shares in the account.
        ownership: The ownership percentage of the account.
        return_on_investment: Return on investment metrics.
    """

    account_id: str = Field(..., pattern=r"^PL-[a-f0-9]{32}$")
    account_balance: float
    current_value: float
    total_shares: float
    ownership: float
    return_on_investment: float
