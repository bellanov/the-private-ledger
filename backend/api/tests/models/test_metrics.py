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
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric.average_share_price == 10.50
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1050.00

    def test_create_metric_with_zero_values(self):
        """Metrics should handle zero values correctly."""
        metric = Metrics(
            average_share_price=0.0,
            total_shares=0.0,
            total_bankroll=0.0,
        )

        assert metric.average_share_price == 0.0
        assert metric.total_shares == 0.0
        assert metric.total_bankroll == 0.0

    def test_create_metric_with_decimal_precision(self):
        """Metrics should preserve decimal precision."""
        metric = Metrics(
            average_share_price=12.3456,
            total_shares=123.456,
            total_bankroll=5678.1234,
        )

        assert metric.average_share_price == 12.3456
        assert metric.total_shares == 123.456
        assert metric.total_bankroll == 5678.1234

    def test_create_metric_with_camel_case_input(self):
        """Metrics should accept camelCase field names."""
        metric = Metrics(
            averageSharePrice=11.00,
            totalShares=100.0,
            totalBankroll=1100.00,
        )

        assert metric.average_share_price == 11.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1100.00


@pytest.mark.unit
class TestMetricsValidation:
    """Test Pydantic validation behavior."""

    def test_metric_requires_all_fields(self):
        """Metrics should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Metrics(average_share_price=10.00)

        errors = exc_info.value.errors()
        assert len(errors) >= 2  # Missing required fields

    def test_metric_validates_numeric_fields(self):
        """Metrics should validate numeric fields."""
        with pytest.raises(ValidationError):
            Metrics(
                average_share_price="not a number",
                total_shares=100.0,
                total_bankroll=1000.00,
            )

    def test_metric_converts_numeric_strings(self):
        """Metrics should convert numeric strings to floats."""
        metric = Metrics(
            average_share_price="10.50",
            total_shares="100.0",
            total_bankroll="1050.00",
        )

        assert metric.average_share_price == 10.50
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1050.00
        assert isinstance(metric.average_share_price, float)

    def test_metric_validates_average_share_price_type(self):
        """Metrics should validate average_share_price is numeric."""
        with pytest.raises(ValidationError):
            Metrics(
                average_share_price=None,
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
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert metric1 == metric2

    def test_metric_inequality_different_average_price(self):
        """Metrics with different average prices should not be equal."""
        metric1 = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            average_share_price=11.00,
            total_shares=100.0,
            total_bankroll=1100.00,
        )

        assert metric1 != metric2

    def test_metric_inequality_different_total_shares(self):
        """Metrics with different total_shares should not be equal."""
        metric1 = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            average_share_price=10.50,
            total_shares=200.0,
            total_bankroll=2100.00,
        )

        assert metric1 != metric2

    def test_metric_inequality_different_bankroll(self):
        """Metrics with different bankrolls should not be equal."""
        metric1 = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            average_share_price=10.50,
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
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        data = metric.model_dump()

        assert data["average_share_price"] == 10.50
        assert data["total_shares"] == 100.0
        assert data["total_bankroll"] == 1050.00

    def test_metric_model_dump_json(self):
        """model_dump_json should return JSON string."""
        metric = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        json_str = metric.model_dump_json()

        assert isinstance(json_str, str)
        assert "10.5" in json_str or "10.50" in json_str
        assert "100.0" in json_str or "100" in json_str
        assert "1050.0" in json_str or "1050.00" in json_str

    def test_metric_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        metric = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        data = metric.model_dump(by_alias=True)

        assert "averageSharePrice" in data
        assert "totalShares" in data
        assert "totalBankroll" in data

    def test_metric_has_all_attributes(self):
        """Metrics should have all expected attributes."""
        metric = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        assert hasattr(metric, "average_share_price")
        assert hasattr(metric, "total_shares")
        assert hasattr(metric, "total_bankroll")


@pytest.mark.unit
class TestMetricsAveragePriceRelationships:
    """Test average share price calculations and relationships."""

    def test_bankroll_equals_average_price_times_shares(self):
        """Bankroll should equal average_share_price * total_shares."""
        metric = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )

        expected_bankroll = metric.average_share_price * metric.total_shares

        assert metric.total_bankroll == expected_bankroll

    def test_average_price_high_with_high_bankroll(self):
        """Higher average share price should correlate with higher bankroll."""
        metric1 = Metrics(
            average_share_price=5.00,
            total_shares=100.0,
            total_bankroll=500.00,
        )
        metric2 = Metrics(
            average_share_price=15.00,
            total_shares=100.0,
            total_bankroll=1500.00,
        )

        assert metric2.average_share_price > metric1.average_share_price
        assert metric2.total_bankroll > metric1.total_bankroll

    def test_more_shares_with_same_price(self):
        """More shares at same average price increases bankroll."""
        metric1 = Metrics(
            average_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1000.00,
        )
        metric2 = Metrics(
            average_share_price=10.00,
            total_shares=500.0,
            total_bankroll=5000.00,
        )

        assert metric1.average_share_price == metric2.average_share_price
        assert metric2.total_shares > metric1.total_shares
        assert metric2.total_bankroll > metric1.total_bankroll

    def test_price_to_bankroll_ratio(self):
        """Calculate price to bankroll ratio."""
        metric = Metrics(
            average_share_price=10.00,
            total_shares=150.0,
            total_bankroll=1500.00,
        )

        price_to_bankroll_ratio = metric.total_bankroll / metric.average_share_price

        assert price_to_bankroll_ratio == metric.total_shares


@pytest.mark.unit
class TestMetricsEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_metric_with_very_small_floats(self):
        """Metrics should handle very small decimal values."""
        metric = Metrics(
            average_share_price=0.01,
            total_shares=100.0,
            total_bankroll=1.00,
        )

        assert metric.average_share_price == 0.01
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1.00

    def test_metric_with_large_values(self):
        """Metrics should handle large financial values."""
        metric = Metrics(
            average_share_price=15000.00,
            total_shares=100.0,
            total_bankroll=1_500_000.00,
        )

        assert metric.average_share_price == 15000.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == 1_500_000.00

    def test_metric_with_negative_values(self):
        """Metrics should handle negative values (edge case)."""
        metric = Metrics(
            average_share_price=-5.00,
            total_shares=100.0,
            total_bankroll=-500.00,
        )

        assert metric.average_share_price == -5.00
        assert metric.total_shares == 100.0
        assert metric.total_bankroll == -500.00

    def test_metric_with_fractional_cents(self):
        """Metrics should handle fractional cent values."""
        metric = Metrics(
            average_share_price=10.123,
            total_shares=100.0,
            total_bankroll=1012.30,
        )

        assert metric.average_share_price == 10.123
        assert metric.total_shares == 100.0

    def test_multiple_metrics_are_independent(self):
        """Multiple Metrics instances should not share state."""
        metric1 = Metrics(
            average_share_price=10.50,
            total_shares=100.0,
            total_bankroll=1050.00,
        )
        metric2 = Metrics(
            average_share_price=12.00,
            total_shares=200.0,
            total_bankroll=2400.00,
        )

        assert metric1.average_share_price != metric2.average_share_price
        assert metric1.total_shares != metric2.total_shares
        assert metric1.total_bankroll != metric2.total_bankroll

    def test_metric_with_very_high_precision(self):
        """Metrics should handle high precision decimals."""
        metric = Metrics(
            average_share_price=10.123456789,
            total_shares=123.456789,
            total_bankroll=1012.3456789,
        )

        assert metric.average_share_price == 10.123456789
        assert metric.total_shares == 123.456789
        assert metric.total_bankroll == 1012.3456789

    def test_metric_with_fractional_shares(self):
        """Metrics should handle fractional share ownership."""
        metric = Metrics(
            average_share_price=10.00,
            total_shares=0.5,
            total_bankroll=5.00,
        )

        assert metric.total_shares == 0.5
        assert metric.total_bankroll == metric.average_share_price * metric.total_shares

    def test_metric_with_large_share_count(self):
        """Metrics should handle large numbers of shares."""
        metric = Metrics(
            average_share_price=10.00,
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
            average_share_price=10.00,
            total_shares=100.0,
            total_bankroll=1000.00,
        )

        assert metric.total_bankroll == 1000.00
        assert metric.total_shares == 100.0
        assert metric.average_share_price == 10.00

    def test_profitable_scenario(self):
        """Metrics showing healthy portfolio value."""
        metric = Metrics(
            average_share_price=12.50,
            total_shares=100.0,
            total_bankroll=1250.00,
        )

        assert metric.total_bankroll == 1250.00
        assert metric.average_share_price == 12.50
        assert metric.total_bankroll == metric.average_share_price * metric.total_shares

    def test_loss_scenario(self):
        """Metrics showing reduced portfolio value."""
        metric = Metrics(
            average_share_price=7.50,
            total_shares=100.0,
            total_bankroll=750.00,
        )

        assert metric.total_bankroll == 750.00
        assert metric.average_share_price == 7.50
        assert metric.total_bankroll == metric.average_share_price * metric.total_shares

    def test_small_gain_scenario(self):
        """Metrics showing modest average share price."""
        metric = Metrics(
            average_share_price=10.05,
            total_shares=100.0,
            total_bankroll=1005.00,
        )

        assert metric.total_bankroll == 1005.00
        assert metric.average_share_price == 10.05
        # Use approximate comparison for floating-point arithmetic
        assert (
            abs(
                metric.total_bankroll
                - (metric.average_share_price * metric.total_shares)
            )
            < 0.01
        )

    def test_multi_account_scenario(self):
        """Metrics with multiple accounts owning shares."""
        metric = Metrics(
            average_share_price=10.00,
            total_shares=250.0,  # 3 accounts with varying shares
            total_bankroll=2500.00,
        )

        assert metric.total_shares == 250.0
        assert metric.total_bankroll == metric.average_share_price * metric.total_shares
