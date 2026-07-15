"""Metrics Model."""

from api.domain.models.pydantic import CamelCaseModel


class Metrics(CamelCaseModel):
    """Represents metrics of the ledger.

    Attributes:
        current_share_price: The current price of a share (total_bankroll / total_shares).
        initial_share_price: The initial price of a share.
        total_shares: The total number of shares owned by all accounts.
        total_bankroll: The total bankroll of the Ledger.
    """

    current_share_price: float
    initial_share_price: float
    total_shares: float
    total_bankroll: float
