"""Performance Tracker Model."""

from dataclasses import dataclass


@dataclass
class PerformanceTracker:
    """Tracks daily performance metrics.

    Attributes:
        date: The date of the performance record.
        total_bankroll: The total bankroll for the day.
        units_won: The number of units won.
        share_price: The price per share.
        record: A string representing the performance record.
    """
    date: str
    total_bankroll: float
    units_won: float
    share_price: float
    record: str
