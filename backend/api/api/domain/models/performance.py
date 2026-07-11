"""Performance Tracker Model."""

from dataclasses import dataclass


@dataclass
class Performance:
    """Tracks daily performance metrics.

    Attributes:
        date: The date of the performance record.
        record: A string representing the performance record.
        share_price: The price per share.
        total_bankroll: The total bankroll for the day.
        units_won: The number of units won.
        return_on_investment: The return on investment for the day.
    """

    date: str
    record: str
    return_on_investment: float
    shares: float
    share_price: float
    total_bankroll: float
    unit_price: float
    units_won: float
