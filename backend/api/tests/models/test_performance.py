"""Unit tests for Performance model."""

import pytest
from pydantic import ValidationError

from api.domain.models.performance import Performance


@pytest.mark.unit
class TestPerformanceInstantiation:
    """Test basic instantiation of Performance."""

    def test_create_performance_with_valid_data(self):
        """Performance should store all constructor values."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=15.5,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=5.0,
        )

        assert performance.date == "2026-07-14"
        assert performance.record == "10-5"
        assert performance.return_on_investment == 15.5
        assert performance.shares == 100.0
        assert performance.share_price == 10.0
        assert performance.total_bankroll == 1000.0
        assert performance.unit_price == 10.0
        assert performance.units_won == 5.0

    def test_create_performance_with_zero_values(self):
        """Performance should handle zero values correctly."""
        performance = Performance(
            date="2026-07-14",
            record="0-0",
            return_on_investment=0.0,
            shares=0.0,
            share_price=0.0,
            total_bankroll=0.0,
            unit_price=0.0,
            units_won=0.0,
        )

        assert performance.record == "0-0"
        assert performance.return_on_investment == 0.0
        assert performance.shares == 0.0
        assert performance.total_bankroll == 0.0

    def test_create_performance_with_decimal_precision(self):
        """Performance should preserve decimal precision."""
        performance = Performance(
            date="2026-07-14",
            record="25-10",
            return_on_investment=12.345,
            shares=123.456,
            share_price=45.678,
            total_bankroll=5678.901,
            unit_price=23.456,
            units_won=78.901,
        )

        assert performance.return_on_investment == 12.345
        assert performance.shares == 123.456
        assert performance.share_price == 45.678

    def test_create_performance_with_camel_case_input(self):
        """Performance should accept camelCase field names."""
        performance = Performance(
            date="2026-07-14",
            record="5-3",
            returnOnInvestment=10.0,
            shares=100.0,
            sharePrice=10.0,
            totalBankroll=1000.0,
            unitPrice=10.0,
            unitsWon=2.0,
        )

        assert performance.return_on_investment == 10.0
        assert performance.total_bankroll == 1000.0


@pytest.mark.unit
class TestPerformanceValidation:
    """Test Pydantic validation behavior."""

    def test_performance_requires_all_fields(self):
        """Performance should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Performance(date="2026-07-14")

        errors = exc_info.value.errors()
        assert len(errors) >= 7  # Missing required fields

    def test_performance_validates_numeric_fields(self):
        """Performance should validate numeric fields."""
        with pytest.raises(ValidationError):
            Performance(
                date="2026-07-14",
                record="5-3",
                return_on_investment="not a number",
                shares=100.0,
                share_price=10.0,
                total_bankroll=1000.0,
                unit_price=10.0,
                units_won=2.0,
            )

    def test_performance_validates_date_type(self):
        """Performance should validate date is a string."""
        with pytest.raises(ValidationError):
            Performance(
                date=12345,
                record="5-3",
                return_on_investment=10.0,
                shares=100.0,
                share_price=10.0,
                total_bankroll=1000.0,
                unit_price=10.0,
                units_won=2.0,
            )

    def test_performance_converts_numeric_strings(self):
        """Performance should convert numeric strings to floats."""
        performance = Performance(
            date="2026-07-14",
            record="5-3",
            return_on_investment="10.0",
            shares="100.0",
            share_price="10.0",
            total_bankroll="1000.0",
            unit_price="10.0",
            units_won="2.0",
        )

        assert performance.return_on_investment == 10.0
        assert performance.shares == 100.0
        assert isinstance(performance.return_on_investment, float)


@pytest.mark.unit
class TestPerformanceRecordValidation:
    """Test record field pattern validation."""

    def test_record_with_valid_format(self):
        """Record should accept W-L format like '10-5'."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        assert performance.record == "10-5"

    def test_record_with_zero_values(self):
        """Record should accept '0-0' format."""
        performance = Performance(
            date="2026-07-14",
            record="0-0",
            return_on_investment=0.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=0.0,
        )

        assert performance.record == "0-0"

    def test_record_with_large_numbers(self):
        """Record should accept large win-loss values."""
        performance = Performance(
            date="2026-07-14",
            record="100-99",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=1.0,
        )

        assert performance.record == "100-99"

    def test_record_rejects_invalid_format(self):
        """Record should reject formats that don't match W-L pattern."""
        with pytest.raises(ValidationError) as exc_info:
            Performance(
                date="2026-07-14",
                record="10-5-2",
                return_on_investment=10.0,
                shares=100.0,
                share_price=10.0,
                total_bankroll=1000.0,
                unit_price=10.0,
                units_won=2.0,
            )

        errors = exc_info.value.errors()
        assert any("pattern" in str(e).lower() for e in errors)

    def test_record_rejects_missing_hyphen(self):
        """Record should reject format without hyphen."""
        with pytest.raises(ValidationError):
            Performance(
                date="2026-07-14",
                record="10",
                return_on_investment=10.0,
                shares=100.0,
                share_price=10.0,
                total_bankroll=1000.0,
                unit_price=10.0,
                units_won=2.0,
            )

    def test_record_rejects_non_numeric_values(self):
        """Record should reject non-numeric win-loss values."""
        with pytest.raises(ValidationError):
            Performance(
                date="2026-07-14",
                record="a-b",
                return_on_investment=10.0,
                shares=100.0,
                share_price=10.0,
                total_bankroll=1000.0,
                unit_price=10.0,
                units_won=2.0,
            )


@pytest.mark.unit
class TestPerformanceEquality:
    """Test model equality behavior."""

    def test_performance_equality_same_values(self):
        """Performance instances with identical values should be equal."""
        performance1 = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )
        performance2 = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        assert performance1 == performance2

    def test_performance_inequality_different_date(self):
        """Performance instances with different dates should not be equal."""
        performance1 = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )
        performance2 = Performance(
            date="2026-07-15",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        assert performance1 != performance2

    def test_performance_inequality_different_record(self):
        """Performance instances with different records should not be equal."""
        performance1 = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )
        performance2 = Performance(
            date="2026-07-14",
            record="11-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        assert performance1 != performance2


@pytest.mark.unit
class TestPerformanceSerialization:
    """Test Pydantic serialization behavior."""

    def test_performance_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        data = performance.model_dump()

        assert data["date"] == "2026-07-14"
        assert data["record"] == "10-5"
        assert data["return_on_investment"] == 10.0
        assert data["shares"] == 100.0
        assert data["share_price"] == 10.0
        assert data["total_bankroll"] == 1000.0
        assert data["unit_price"] == 10.0
        assert data["units_won"] == 2.0

    def test_performance_model_dump_json(self):
        """model_dump_json should return JSON string."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        json_str = performance.model_dump_json()

        assert isinstance(json_str, str)
        assert "2026-07-14" in json_str
        assert "10-5" in json_str

    def test_performance_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        data = performance.model_dump(by_alias=True)

        assert "returnOnInvestment" in data
        assert "sharePrice" in data
        assert "totalBankroll" in data
        assert "unitPrice" in data
        assert "unitsWon" in data

    def test_performance_has_all_attributes(self):
        """Performance should have all expected attributes."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        assert hasattr(performance, "date")
        assert hasattr(performance, "record")
        assert hasattr(performance, "return_on_investment")
        assert hasattr(performance, "shares")
        assert hasattr(performance, "share_price")
        assert hasattr(performance, "total_bankroll")
        assert hasattr(performance, "unit_price")
        assert hasattr(performance, "units_won")


@pytest.mark.unit
class TestPerformanceFinancialCalculations:
    """Test financial relationship validations."""

    def test_share_price_calculation(self):
        """Share price should equal total_bankroll / shares."""
        performance = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )

        calculated_price = performance.total_bankroll / performance.shares

        assert calculated_price == performance.share_price

    def test_positive_roi_scenario(self):
        """ROI should be positive for profit."""
        performance = Performance(
            date="2026-07-14",
            record="15-5",
            return_on_investment=25.5,
            shares=100.0,
            share_price=12.5,
            total_bankroll=1250.0,
            unit_price=10.0,
            units_won=10.0,
        )

        assert performance.return_on_investment > 0
        assert performance.units_won > 0

    def test_negative_roi_scenario(self):
        """ROI should be negative for loss."""
        performance = Performance(
            date="2026-07-14",
            record="5-15",
            return_on_investment=-20.0,
            shares=100.0,
            share_price=8.0,
            total_bankroll=800.0,
            unit_price=10.0,
            units_won=-10.0,
        )

        assert performance.return_on_investment < 0
        assert performance.units_won < 0

    def test_break_even_scenario(self):
        """ROI should be zero for break-even."""
        performance = Performance(
            date="2026-07-14",
            record="10-10",
            return_on_investment=0.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=0.0,
        )

        assert performance.return_on_investment == 0.0
        assert performance.units_won == 0.0


@pytest.mark.unit
class TestPerformanceEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_performance_with_very_small_floats(self):
        """Performance should handle very small decimal values."""
        performance = Performance(
            date="2026-07-14",
            record="1-0",
            return_on_investment=0.01,
            shares=0.001,
            share_price=0.01,
            total_bankroll=0.01,
            unit_price=0.01,
            units_won=0.001,
        )

        assert performance.return_on_investment == 0.01
        assert performance.shares == 0.001

    def test_performance_with_large_values(self):
        """Performance should handle large financial values."""
        performance = Performance(
            date="2026-07-14",
            record="1000-500",
            return_on_investment=500.0,
            shares=10000.0,
            share_price=150.0,
            total_bankroll=1_500_000.0,
            unit_price=100.0,
            units_won=5000.0,
        )

        assert performance.total_bankroll == 1_500_000.0
        assert performance.shares == 10000.0

    def test_multiple_performances_are_independent(self):
        """Multiple Performance instances should not share state."""
        performance1 = Performance(
            date="2026-07-14",
            record="10-5",
            return_on_investment=10.0,
            shares=100.0,
            share_price=10.0,
            total_bankroll=1000.0,
            unit_price=10.0,
            units_won=2.0,
        )
        performance2 = Performance(
            date="2026-07-15",
            record="11-5",
            return_on_investment=15.0,
            shares=100.0,
            share_price=11.5,
            total_bankroll=1150.0,
            unit_price=10.0,
            units_won=5.0,
        )

        assert performance1.date != performance2.date
        assert performance1.total_bankroll != performance2.total_bankroll
