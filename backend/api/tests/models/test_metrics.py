"""Unit tests for Metrics model."""

import pytest
from pydantic import ValidationError

from api.domain.models.metrics import Metrics


@pytest.mark.unit
class TestMetricsInstantiation:
    """Test basic instantiation of Metrics."""

    def test_create_metric_with_valid_data(self):
        """Metrics should store all constructor values."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric.current_share_price == 10.50
        assert metric.initial_share_price == 10.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1050.00

    def test_create_metric_with_zero_values(self):
        """Metrics should handle zero values correctly."""
        metric = Metrics(
            current_share_price=0.0,
            initial_share_price=0.0,
            total_shares=0.0,
            total_bankroll=0.0,
        )

        assert metric.current_share_price == 0.0
        assert metric.initial_share_price == 0.0
        assert metric.total_shares == 0.0
        assert metric.total_bankroll == 0.0

    def test_create_metric_with_decimal_precision(self):
        """Metrics should preserve decimal precision."""
        metric = Metrics(
            current_share_price=12.3456,
            initial_share_price=10.9876,
            total_shares=123.456,
            total_bankroll=5678.1234,
        )

        assert metric.current_share_price == 12.3456
        assert metric.initial_share_price == 10.9876
        assert metric.total_shares == 123.456
        assert metric.total_bankroll == 5678.1234

    def test_create_metric_with_camel_case_input(self):
        """Metrics should accept camelCase field names."""
        metric = Metrics(
            currentSharePrice=11.00,
            initialSharePrice=10.00,
            totalShares=100.0,
            totalBankroll=1100.00,
        )

        assert metric.current_share_price == 11.00
        assert metric.initial_share_price == 10.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1100.00


@pytest.mark.unit
class TestMetricsValidation:
    """Test Pydantic validation behavior."""

    def test_metric_requires_all_fields(self):
        """Metrics should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Metrics(current_share_price=10.00)

        errors = exc_info.value.errors()
        assert len(errors) >= 3  # Missing required fields

    def test_metric_validates_numeric_fields(self):
        """Metrics should validate numeric fields."""
        with pytest.raises(ValidationError):
            Metrics(
                current_share_price="not a number",
                initial_share_price=10.00,
                total_shares=100.0,
                total_bankroll=1000.00,
            )

    def test_metric_converts_numeric_strings(self):
        """Metrics should convert numeric strings to floats."""
        metric = Metrics(
            current_share_price="10.50",
            initial_share_price="10.00",
            total_shares="100.0",
            total_bankroll="1050.00",
        )

        assert metric.current_share_price == 10.50
        assert metric.initial_share_price == 10.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1050.00
        assert isinstance(metric.current_share_price, float)

    def test_metric_validates_current_share_price_type(self):
        """Metrics should validate current_share_price is numeric."""
        with pytest.raises(ValidationError):
            Metrics(
                current_share_price=None,
                initial_share_price=10.00,
                total_shares=100.0,
                total_bankroll=1000.00,
            )

    def test_metric_validates_initial_share_price_type(self):
        """Metrics should validate initial_share_price is numeric."""
        with pytest.raises(ValidationError):
            Metrics(
                current_share_price=10.50,
                initial_share_price=None,
                total_shares=100.0,
                total_bankroll=1000.00,
            )

    def test_metric_validates_total_shares_type(self):
        """Metrics should validate total_shares is numeric."""
        with pytest.raises(ValidationError):
            Metrics(
                current_share_price=10.50,
                initial_share_price=10.00,
                total_shares=None,
                total_bankroll=1000.00,
            )

    def test_metric_validates_total_bankroll_type(self):
        """Metrics should validate total_bankroll is numeric."""
        with pytest.raises(ValidationError):
            Metrics(
                current_share_price=10.50,
                initial_share_price=10.00,
                total_shares=100.0,
                total_bankroll=None,
            )


@pytest.mark.unit
class TestMetricsEquality:
    """Test model equality behavior."""

    def test_metric_equality_same_values(self):
        """Metrics with identical values should be equal."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric1 == metric2

    def test_metric_inequality_different_current_price(self):
        """Metrics with different current prices should not be equal."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric1 != metric2

    def test_metric_inequality_different_initial_price(self):
        """Metrics with different initial prices should not be equal."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=10.50,
            initial_share_price=9.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric1 != metric2

    def test_metric_inequality_different_total_shares(self):
        """Metrics with different total_shares should not be equal."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=200.0,
            total_bankroll=1050.00,
        )

        assert metric1 != metric2

    def test_metric_inequality_different_bankroll(self):
        """Metrics with different bankrolls should not be equal."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=2000.00,
        )

        assert metric1 != metric2


@pytest.mark.unit
class TestMetricsSerialization:
    """Test Pydantic serialization behavior."""

    def test_metric_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        data = metric.model_dump()

        assert data["current_share_price"] == 10.50
        assert data["initial_share_price"] == 10.00
        assert data["total_shares"] == 100.0
        assert data["total_bankroll"] == 1050.00

    def test_metric_model_dump_json(self):
        """model_dump_json should return JSON string."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        json_str = metric.model_dump_json()

        assert isinstance(json_str, str)
        assert "10.5" in json_str or "10.50" in json_str
        assert "10.0" in json_str or "10.00" in json_str
        assert "100.0" in json_str or "100" in json_str
        assert "1050.0" in json_str or "1050.00" in json_str

    def test_metric_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        data = metric.model_dump(by_alias=True)

        assert "currentSharePrice" in data
        assert "initialSharePrice" in data
        assert "totalShares" in data
        assert "totalBankroll" in data

    def test_metric_has_all_attributes(self):
        """Metrics should have all expected attributes."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert hasattr(metric, "current_share_price")
        assert hasattr(metric, "initial_share_price")
        assert hasattr(metric, "total_shares")
        assert hasattr(metric, "total_bankroll")


@pytest.mark.unit
class TestMetricsSharePriceRelationships:
    """Test share price relationship validations."""

    def test_current_price_greater_than_initial(self):
        """Current share price can be greater than initial (profit)."""
        metric = Metrics(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1200.00,
        )

        assert metric.current_share_price > metric.initial_share_price

    def test_current_price_less_than_initial(self):
        """Current share price can be less than initial (loss)."""
        metric = Metrics(
            current_share_price=8.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=800.00,
        )

        assert metric.current_share_price < metric.initial_share_price

    def test_current_price_equals_initial(self):
        """Current share price can equal initial (break-even)."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1000.00,
        )

        assert metric.current_share_price == metric.initial_share_price

    def test_price_change_calculation(self):
        """Calculate price change from initial to current."""
        metric = Metrics(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1200.00,
        )

        price_change = metric.current_share_price - metric.initial_share_price

        assert price_change == 2.00

    def test_percentage_change_calculation(self):
        """Calculate percentage change from initial to current."""
        metric = Metrics(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1100.00,
        )

        percentage_change = (
            (metric.current_share_price - metric.initial_share_price)
            / metric.initial_share_price
            * 100
        )

        assert percentage_change == 10.0


@pytest.mark.unit
class TestMetricsBankrollCalculations:
    """Test total bankroll calculations."""

    def test_bankroll_equals_shares_times_price(self):
        """Bankroll should equal current_share_price * total_shares."""
        metric = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        expected_bankroll = metric.current_share_price * metric.total_shares

        assert metric.total_bankroll == expected_bankroll

    def test_bankroll_larger_than_initial_investment(self):
        """Bankroll can be larger than initial investment (profit)."""
        metric = Metrics(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1200.00,
        )

        initial_investment = metric.initial_share_price * metric.total_shares

        assert metric.total_bankroll > initial_investment

    def test_bankroll_smaller_than_initial_investment(self):
        """Bankroll can be smaller than initial investment (loss)."""
        metric = Metrics(
            current_share_price=8.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=800.00,
        )

        initial_investment = metric.initial_share_price * metric.total_shares

        assert metric.total_bankroll < initial_investment

    def test_roi_calculation(self):
        """Calculate ROI from metric data."""
        metric = Metrics(
            current_share_price=11.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1100.00,
        )

        initial_investment = metric.initial_share_price * metric.total_shares
        roi = (metric.total_bankroll - initial_investment) / initial_investment * 100

        assert roi == 10.0

    def test_bankroll_with_fractional_shares(self):
        """Bankroll calculation should work with fractional shares."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=50.5,
            total_bankroll=505.00,
        )

        expected_bankroll = metric.current_share_price * metric.total_shares

        assert metric.total_bankroll == expected_bankroll


@pytest.mark.unit
class TestMetricsEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_metric_with_very_small_floats(self):
        """Metrics should handle very small decimal values."""
        metric = Metrics(
            current_share_price=0.01,
            initial_share_price=0.01,
            total_shares=100.0,
            total_bankroll=1.00,
        )

        assert metric.current_share_price == 0.01
        assert metric.initial_share_price == 0.01
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1.00

    def test_metric_with_large_values(self):
        """Metrics should handle large financial values."""
        metric = Metrics(
            current_share_price=15000.00,
            initial_share_price=10000.00,
            total_shares=100.0,
            total_bankroll=1_500_000.00,
        )

        assert metric.current_share_price == 15000.00
        assert metric.initial_share_price == 10000.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1_500_000.00

    def test_metric_with_negative_values(self):
        """Metrics should handle negative values (edge case)."""
        metric = Metrics(
            current_share_price=-5.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=-500.00,
        )

        assert metric.current_share_price == -5.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == -500.00

    def test_metric_with_fractional_cents(self):
        """Metrics should handle fractional cent values."""
        metric = Metrics(
            current_share_price=10.123,
            initial_share_price=10.456,
            total_shares=100.0,
            total_bankroll=1012.30,
        )

        assert metric.current_share_price == 10.123
        assert metric.initial_share_price == 10.456
        assert metric.total_shares == 100.0

    def test_multiple_metrics_are_independent(self):
        """Multiple Metrics instances should not share state."""
        metric1 = Metrics(
            current_share_price=10.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            current_share_price=12.00,
            initial_share_price=10.00,
            total_shares=200.0,
            total_bankroll=2400.00,
        )

        assert metric1.current_share_price != metric2.current_share_price
        assert metric1.total_shares != metric2.total_shares
        assert metric1.total_bankroll != metric2.total_bankroll

    def test_metric_with_same_initial_and_current_price(self):
        """Metrics with identical prices represents break-even."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1000.00,
        )

        price_difference = metric.current_share_price - metric.initial_share_price

        assert price_difference == 0.0

    def test_metric_with_very_high_precision(self):
        """Metrics should handle high precision decimals."""
        metric = Metrics(
            current_share_price=10.123456789,
            initial_share_price=10.987654321,
            total_shares=123.456789,
            total_bankroll=1012.3456789,
        )

        assert metric.current_share_price == 10.123456789
        assert metric.initial_share_price == 10.987654321
        assert metric.total_shares == 123.456789
        assert metric.total_bankroll == 1012.3456789

    def test_metric_with_fractional_shares(self):
        """Metrics should handle fractional share ownership."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=0.5,
            total_bankroll=5.00,
        )

        assert metric.total_shares == 0.5
        assert metric.total_bankroll == metric.current_share_price * metric.total_shares

    def test_metric_with_large_share_count(self):
        """Metrics should handle large numbers of shares."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=1_000_000.0,
            total_bankroll=10_000_000.00,
        )

        assert metric.total_shares == 1_000_000.0
        assert metric.total_bankroll == 10_000_000.00


@pytest.mark.unit
class TestMetricsTypicalScenarios:
    """Test typical usage scenarios."""

    def test_startup_scenario(self):
        """Metrics at ledger startup with initial deposit."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1000.00,
        )

        assert metric.current_share_price == metric.initial_share_price
        assert metric.total_bankroll == 1000.00
        assert metric.total_shares == 100.0

    def test_profitable_scenario(self):
        """Metrics showing profit after successful betting."""
        metric = Metrics(
            current_share_price=12.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1250.00,
        )

        profit = metric.total_bankroll - (
            metric.initial_share_price * metric.total_shares
        )

        assert profit == 250.00
        assert metric.current_share_price > metric.initial_share_price

    def test_loss_scenario(self):
        """Metrics showing loss after unsuccessful betting."""
        metric = Metrics(
            current_share_price=7.50,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=750.00,
        )

        loss = (
            metric.initial_share_price * metric.total_shares
        ) - metric.total_bankroll

        assert loss == 250.00
        assert metric.current_share_price < metric.initial_share_price

    def test_small_gain_scenario(self):
        """Metrics showing small incremental gain."""
        metric = Metrics(
            current_share_price=10.05,
            initial_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1005.00,
        )

        gain = metric.total_bankroll - (
            metric.initial_share_price * metric.total_shares
        )

        assert gain == 5.00
        assert 0 < gain < 10

    def test_multi_account_scenario(self):
        """Metrics with multiple accounts owning shares."""
        metric = Metrics(
            current_share_price=10.00,
            initial_share_price=10.00,
            total_shares=250.0,  # 3 accounts with varying shares
            total_bankroll=2500.00,
        )

        assert metric.total_shares == 250.0
        assert metric.total_bankroll == metric.current_share_price * metric.total_shares
