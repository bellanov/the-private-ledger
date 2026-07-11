"""Unit tests for Performance model."""

import pytest

from api.domain.models.performance import Performance


@pytest.mark.unit
def test_performance_initialization_sets_all_fields():
    model = Performance(
        date="2026-07-11",
        record="10-5",
        return_on_investment=0.12,
        shares=200.0,
        share_price=12.5,
        total_bankroll=2500.0,
        unit_price=25.0,
        units_won=3.75,
    )

    assert model.date == "2026-07-11"
    assert model.record == "10-5"
    assert model.return_on_investment == 0.12
    assert model.shares == 200.0
    assert model.share_price == 12.5
    assert model.total_bankroll == 2500.0
    assert model.unit_price == 25.0
    assert model.units_won == 3.75


@pytest.mark.unit
def test_performance_equality_same_values():
    left = Performance(
        "2026-07-11",
        "10-5",
        0.12,
        200.0,
        12.5,
        2500.0,
        25.0,
        3.75,
    )
    right = Performance(
        "2026-07-11",
        "10-5",
        0.12,
        200.0,
        12.5,
        2500.0,
        25.0,
        3.75,
    )

    assert left == right
