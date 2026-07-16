"""Ledger Model."""

from pydantic import Field

from api.domain.models.pydantic import CamelCaseModel


class Ledger(CamelCaseModel):
    """Represents a ledger.

    Attributes:
        id: The ID of the ledger.
        name: The name of the ledger.
        current_share_price: The current price of a share.
        initial_share_price: The initial price of a share.
    """

    id: str = Field(..., pattern=r"^[a-f0-9]{32}$")
    name: str
    description: str
    current_share_price: float
    initial_share_price: float
