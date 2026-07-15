"""Ledger Model."""

from api.domain.models.pydantic import CamelCaseModel


class Ledger(CamelCaseModel):
    """Represents a ledger.

    Attributes:
        current_share_price: The current price of a share.
        initial_share_price: The initial price of a share.
    """

    current_share_price: float
    initial_share_price: float
