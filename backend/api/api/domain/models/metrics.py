"""Metrics Model."""

from api.domain.models.pydantic import CamelCaseModel


class Metrics(CamelCaseModel):
    """Represents metrics of the ledger.

    Attributes:
        average_share_price: The average price of a share across all ledgers.
        total_shares: The total number of shares owned by all accounts.
        total_bankroll: The total bankroll of the Ledger.
    """

    average_share_price: float
    total_shares: float
    total_bankroll: float
