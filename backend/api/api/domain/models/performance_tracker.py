"""Performance Tracker Model."""

from dataclasses import dataclass


@dataclass
class PerformanceTracker:
    """Tracks daily performance metrics.

    Attributes:
        date: The date of the performance record.
        record: A string representing the performance record.
        share_price: The price per share.
        total_bankroll: The total bankroll for the day.
        units_won: The number of units won.
    """

    date: str
    record: str
    share_price: float
    total_bankroll: float
    units_won: float
