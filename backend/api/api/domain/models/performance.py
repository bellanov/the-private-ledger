"""Performance Model."""

from dataclasses import dataclass

from api.domain.models.pydantic import CamelCaseModel


class Performance(CamelCaseModel):
    """Represents a performance record.

    Attributes:
        date: The date of the performance record.
        record: A string representing the performance record.
        return_on_investment: The return on investment for the day.
        shares: The number of shares held.
        share_price: The price per share.
        total_bankroll: The total bankroll for the day.
        unit_price: The price per unit.
        units_won: The number of units won.
    """

    date: str
    record: str
    return_on_investment: float
    shares: float
    share_price: float
    total_bankroll: float
    unit_price: float
    units_won: float
