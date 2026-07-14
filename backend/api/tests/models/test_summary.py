"""Unit tests for Summary model."""

import pytest
from pydantic import ValidationError

from api.domain.models.summary import Summary


@pytest.mark.unit
class TestSummaryInstantiation:
    """Test basic instantiation of Summary."""

    def test_create_summary_with_valid_data(self):
        """Summary should store all constructor values."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        assert summary.current_share_price == 10.50
        assert summary.initial_share_price == 10.00
        assert summary.total_bankroll == 1050.00

    def test_create_summary_with_zero_values(self):
        """Summary should handle zero values correctly."""
        summary = Summary(
            current_share_price=0.0,
            initial_share_price=0.0,
            total_bankroll=0.0,
        )

        assert summary.current_share_price == 0.0
        assert summary.initial_share_price == 0.0
        assert summary.total_bankroll == 0.0

    def test_create_summary_with_decimal_precision(self):
        """Summary should preserve decimal precision."""
        summary = Summary(
            current_share_price=12.3456,
            initial_share_price=10.9876,
            total_bankroll=5678.1234,
        )

        assert summary.current_share_price == 12.3456
        assert summary.initial_share_price == 10.9876
        assert summary.total_bankroll == 5678.1234

    def test_create_summary_with_camel_case_input(self):
        """Summary should accept camelCase field names."""
        summary = Summary(
            currentSharePrice=11.00,
            initialSharePrice=10.00,
            totalBankroll=1100.00,
        )

        assert summary.current_share_price == 11.00
        assert summary.initial_share_price == 10.00
        assert summary.total_bankroll == 1100.00


@pytest.mark.unit
class TestSummaryValidation:
    """Test Pydantic validation behavior."""

    def test_summary_requires_all_fields(self):
        """Summary should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Summary(current_share_price=10.00)

        errors = exc_info.value.errors()
        assert len(errors) >= 2  # Missing required fields

    def test_summary_validates_numeric_fields(self):
        """Summary should validate numeric fields."""
        with pytest.raises(ValidationError):
            Summary(
                current_share_price="not a number",
                initial_share_price=10.00,
                total_bankroll=1000.00,
            )

    def test_summary_converts_numeric_strings(self):
        """Summary should convert numeric strings to floats."""
        summary = Summary(
            current_share_price="10.50",
            initial_share_price="10.00",
            total_bankroll="1050.00",
        )

        assert summary.current_share_price == 10.50
        assert summary.initial_share_price == 10.00
        assert summary.total_bankroll == 1050.00
        assert isinstance(summary.current_share_price, float)

    def test_summary_validates_current_share_price_type(self):
        """Summary should validate current_share_price is numeric."""
        with pytest.raises(ValidationError):
            Summary(
                current_share_price=None,
                initial_share_price=10.00,
                total_bankroll=1000.00,
            )

    def test_summary_validates_initial_share_price_type(self):
        """Summary should validate initial_share_price is numeric."""
        with pytest.raises(ValidationError):
            Summary(
                current_share_price=10.50,
                initial_share_price=None,
                total_bankroll=1000.00,
            )

    def test_summary_validates_total_bankroll_type(self):
        """Summary should validate total_bankroll is numeric."""
        with pytest.raises(ValidationError):
            Summary(
                current_share_price=10.50,
                initial_share_price=10.00,
                total_bankroll=None,
            )


@pytest.mark.unit
class TestSummaryEquality:
    """Test model equality behavior."""

    def test_summary_equality_same_values(self):
        """Summaries with identical values should be equal."""
        summary1 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )
        summary2 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        assert summary1 == summary2

    def test_summary_inequality_different_current_price(self):
        """Summaries with different current prices should not be equal."""
        summary1 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )
        summary2 = Summary(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        assert summary1 != summary2

    def test_summary_inequality_different_initial_price(self):
        """Summaries with different initial prices should not be equal."""
        summary1 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )
        summary2 = Summary(
            current_share_price=10.50,
            initial_share_price=9.50,
            total_bankroll=1050.00,
        )

        assert summary1 != summary2

    def test_summary_inequality_different_bankroll(self):
        """Summaries with different bankrolls should not be equal."""
        summary1 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )
        summary2 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=2000.00,
        )

        assert summary1 != summary2


@pytest.mark.unit
class TestSummarySerialization:
    """Test Pydantic serialization behavior."""

    def test_summary_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        data = summary.model_dump()

        assert data["current_share_price"] == 10.50
        assert data["initial_share_price"] == 10.00
        assert data["total_bankroll"] == 1050.00

    def test_summary_model_dump_json(self):
        """model_dump_json should return JSON string."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        json_str = summary.model_dump_json()

        assert isinstance(json_str, str)
        assert "10.5" in json_str or "10.50" in json_str
        assert "10.0" in json_str or "10.00" in json_str
        assert "1050.0" in json_str or "1050.00" in json_str

    def test_summary_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        data = summary.model_dump(by_alias=True)

        assert "currentSharePrice" in data
        assert "initialSharePrice" in data
        assert "totalBankroll" in data

    def test_summary_has_all_attributes(self):
        """Summary should have all expected attributes."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        assert hasattr(summary, "current_share_price")
        assert hasattr(summary, "initial_share_price")
        assert hasattr(summary, "total_bankroll")


@pytest.mark.unit
class TestSummarySharePriceRelationships:
    """Test share price relationship validations."""

    def test_current_price_greater_than_initial(self):
        """Current share price can be greater than initial (profit)."""
        summary = Summary(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_bankroll=1200.00,
        )

        assert summary.current_share_price > summary.initial_share_price

    def test_current_price_less_than_initial(self):
        """Current share price can be less than initial (loss)."""
        summary = Summary(
            current_share_price=8.00,
            initial_share_price=10.00,
            total_bankroll=800.00,
        )

        assert summary.current_share_price < summary.initial_share_price

    def test_current_price_equals_initial(self):
        """Current share price can equal initial (break-even)."""
        summary = Summary(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_bankroll=1000.00,
        )

        assert summary.current_share_price == summary.initial_share_price

    def test_price_change_calculation(self):
        """Calculate price change from initial to current."""
        summary = Summary(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_bankroll=1200.00,
        )

        price_change = summary.current_share_price - summary.initial_share_price

        assert price_change == 2.00

    def test_percentage_change_calculation(self):
        """Calculate percentage change from initial to current."""
        summary = Summary(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_bankroll=1100.00,
        )

        percentage_change = (
            (summary.current_share_price - summary.initial_share_price)
            / summary.initial_share_price
            * 100
        )

        assert percentage_change == 10.0


@pytest.mark.unit
class TestSummaryBankrollCalculations:
    """Test total bankroll calculations."""

    def test_bankroll_with_100_shares(self):
        """Bankroll should equal current_share_price * 100 shares."""
        summary = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )

        expected_bankroll = summary.current_share_price * 100

        assert summary.total_bankroll == expected_bankroll

    def test_bankroll_larger_than_initial_investment(self):
        """Bankroll can be larger than initial investment (profit)."""
        summary = Summary(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_bankroll=1200.00,
        )

        initial_investment = summary.initial_share_price * 100

        assert summary.total_bankroll > initial_investment

    def test_bankroll_smaller_than_initial_investment(self):
        """Bankroll can be smaller than initial investment (loss)."""
        summary = Summary(
            current_share_price=8.00,
            initial_share_price=10.00,
            total_bankroll=800.00,
        )

        initial_investment = summary.initial_share_price * 100

        assert summary.total_bankroll < initial_investment

    def test_roi_calculation(self):
        """Calculate ROI from summary data."""
        summary = Summary(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_bankroll=1100.00,
        )

        initial_investment = summary.initial_share_price * 100
        roi = (summary.total_bankroll - initial_investment) / initial_investment * 100

        assert roi == 10.0


@pytest.mark.unit
class TestSummaryEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_summary_with_very_small_floats(self):
        """Summary should handle very small decimal values."""
        summary = Summary(
            current_share_price=0.01,
            initial_share_price=0.01,
            total_bankroll=1.00,
        )

        assert summary.current_share_price == 0.01
        assert summary.initial_share_price == 0.01
        assert summary.total_bankroll == 1.00

    def test_summary_with_large_values(self):
        """Summary should handle large financial values."""
        summary = Summary(
            current_share_price=15000.00,
            initial_share_price=10000.00,
            total_bankroll=1_500_000.00,
        )

        assert summary.current_share_price == 15000.00
        assert summary.initial_share_price == 10000.00
        assert summary.total_bankroll == 1_500_000.00

    def test_summary_with_negative_values(self):
        """Summary should handle negative values (edge case)."""
        summary = Summary(
            current_share_price=-5.00,
            initial_share_price=10.00,
            total_bankroll=-500.00,
        )

        assert summary.current_share_price == -5.00
        assert summary.total_bankroll == -500.00

    def test_summary_with_fractional_cents(self):
        """Summary should handle fractional cent values."""
        summary = Summary(
            current_share_price=10.123,
            initial_share_price=10.456,
            total_bankroll=1012.30,
        )

        assert summary.current_share_price == 10.123
        assert summary.initial_share_price == 10.456

    def test_multiple_summaries_are_independent(self):
        """Multiple Summary instances should not share state."""
        summary1 = Summary(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_bankroll=1050.00,
        )
        summary2 = Summary(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_bankroll=1200.00,
        )

        assert summary1.current_share_price != summary2.current_share_price
        assert summary1.total_bankroll != summary2.total_bankroll

    def test_summary_with_same_initial_and_current_price(self):
        """Summary with identical prices represents break-even."""
        summary = Summary(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_bankroll=1000.00,
        )

        price_difference = summary.current_share_price - summary.initial_share_price

        assert price_difference == 0.0

    def test_summary_with_very_high_precision(self):
        """Summary should handle high precision decimals."""
        summary = Summary(
            current_share_price=10.123456789,
            initial_share_price=10.987654321,
            total_bankroll=1012.3456789,
        )

        assert summary.current_share_price == 10.123456789
        assert summary.initial_share_price == 10.987654321
        assert summary.total_bankroll == 1012.3456789


@pytest.mark.unit
class TestSummaryTypicalScenarios:
    """Test typical usage scenarios."""

    def test_startup_scenario(self):
        """Summary at ledger startup with initial deposit."""
        summary = Summary(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_bankroll=1000.00,
        )

        assert summary.current_share_price == summary.initial_share_price
        assert summary.total_bankroll == 1000.00

    def test_profitable_scenario(self):
        """Summary showing profit after successful betting."""
        summary = Summary(
            current_share_price=12.50,
            initial_share_price=10.00,
            total_bankroll=1250.00,
        )

        profit = summary.total_bankroll - (summary.initial_share_price * 100)

        assert profit == 250.00
        assert summary.current_share_price > summary.initial_share_price

    def test_loss_scenario(self):
        """Summary showing loss after unsuccessful betting."""
        summary = Summary(
            current_share_price=7.50,
            initial_share_price=10.00,
            total_bankroll=750.00,
        )

        loss = (summary.initial_share_price * 100) - summary.total_bankroll

        assert loss == 250.00
        assert summary.current_share_price < summary.initial_share_price

    def test_small_gain_scenario(self):
        """Summary showing small incremental gain."""
        summary = Summary(
            current_share_price=10.05,
            initial_share_price=10.00,
            total_bankroll=1005.00,
        )

        gain = summary.total_bankroll - (summary.initial_share_price * 100)

        assert gain == 5.00
        assert 0 < gain < 10