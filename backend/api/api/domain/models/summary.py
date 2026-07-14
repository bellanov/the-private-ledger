"""Summary Model."""

from api.domain.models.pydantic import CamelCaseModel


class Summary(CamelCaseModel):
    """Represents a summary of the ledger.

    Attributes:
        current_share_price: The current price of a share.
        initial_share_price: The initial price of a share.
        total_bankroll: The total bankroll of the account.
    """

    current_share_price: float
    initial_share_price: float
    total_bankroll: float
