"""Metrics Model."""

from api.domain.models.pydantic import CamelCaseModel


class Metrics(CamelCaseModel):
    """Represents metrics of the ledger.

    Attributes:
        current_share_price: The current price of a share.
        initial_share_price: The initial price of a share.
        shares_owned: The number of shares owned by all accounts.
        total_bankroll: The total bankroll of the Ledger.
    """

    current_share_price: float
    initial_share_price: float
    shares_owned: float
    total_bankroll: float
