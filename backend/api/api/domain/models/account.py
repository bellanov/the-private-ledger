"""Account Model."""

from dataclasses import dataclass
from uuid import uuid4

from pydantic import Field

from api.domain.models.pydantic import CamelCaseModel


class Account(CamelCaseModel):
    """Represents an account.

    Attributes:
        account_id: The ID of the account associated with the transaction.
        account_balance: The balance of the account.
        current_value: The current value of the account.
        shares_owned: The number of shares owned in the account.
        ownership: The ownership percentage of the account.
        return_on_investment: Return on investment metrics.
    """

    account_id: str
    account_balance: float
    current_value: float
    shares_owned: float
    ownership: float
    return_on_investment: float
