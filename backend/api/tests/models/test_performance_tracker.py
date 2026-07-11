"""Unit tests for PerformanceTracker model."""

import pytest
from api.domain.models.performance_tracker import PerformanceTracker


class TestPerformanceTrackerInstantiation:
    """Test basic instantiation of PerformanceTracker."""

    @pytest.mark.unit
    def test_create_performance_tracker_with_valid_data(self):
        """Test creating a PerformanceTracker with valid data."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=10000.00,
            units_won=5.0,
            share_price=100.00,
            record="5-2-0"
        )
        assert tracker.date == "2026-07-11"
        assert tracker.total_bankroll == 10000.00
        assert tracker.units_won == 5.0
        assert tracker.share_price == 100.00
        assert tracker.record == "5-2-0"

    @pytest.mark.unit
    def test_create_performance_tracker_with_zero_values(self):
        """Test creating a PerformanceTracker with zero values."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=0.0,
            units_won=0.0,
            share_price=0.0,
            record="0-0-0"
        )
        assert tracker.total_bankroll == 0.0
        assert tracker.units_won == 0.0
        assert tracker.share_price == 0.0

    @pytest.mark.unit
    def test_create_performance_tracker_with_negative_values(self):
        """Test creating a PerformanceTracker with negative values."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=-5000.00,
            units_won=-3.0,
            share_price=-50.00,
            record="-3-5-0"
        )
        assert tracker.total_bankroll == -5000.00
        assert tracker.units_won == -3.0
        assert tracker.share_price == -50.00

    @pytest.mark.unit
    def test_create_performance_tracker_with_large_numbers(self):
        """Test creating a PerformanceTracker with large numbers."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=999999999.99,
            units_won=1000000.0,
            share_price=500000.00,
            record="1000000-0-0"
        )
        assert tracker.total_bankroll == 999999999.99
        assert tracker.units_won == 1000000.0
        assert tracker.share_price == 500000.00

    @pytest.mark.unit
    def test_create_performance_tracker_with_decimal_precision(self):
        """Test that PerformanceTracker preserves decimal precision."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1234.56,
            units_won=12.345,
            share_price=123.456,
            record="12.345-0-0"
        )
        assert tracker.total_bankroll == 1234.56
        assert tracker.units_won == 12.345
        assert tracker.share_price == 123.456


class TestPerformanceTrackerDateField:
    """Test date field handling."""

    @pytest.mark.unit
    def test_date_as_iso_format(self):
        """Test date field with ISO format."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=1.0,
            share_price=100.0,
            record="1-0-0"
        )
        assert tracker.date == "2026-07-11"

    @pytest.mark.unit
    def test_date_as_different_format(self):
        """Test date field with different format."""
        tracker = PerformanceTracker(
            date="07/11/2026",
            total_bankroll=1000.0,
            units_won=1.0,
            share_price=100.0,
            record="1-0-0"
        )
        assert tracker.date == "07/11/2026"

    @pytest.mark.unit
    def test_date_as_empty_string(self):
        """Test date field with empty string."""
        tracker = PerformanceTracker(
            date="",
            total_bankroll=1000.0,
            units_won=1.0,
            share_price=100.0,
            record="1-0-0"
        )
        assert tracker.date == ""


class TestPerformanceTrackerRecordField:
    """Test record field handling."""

    @pytest.mark.unit
    def test_record_with_win_loss_format(self):
        """Test record field with standard win-loss format."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        assert tracker.record == "5-2-0"

    @pytest.mark.unit
    def test_record_with_simple_format(self):
        """Test record field with simple format."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2"
        )
        assert tracker.record == "5-2"

    @pytest.mark.unit
    def test_record_as_empty_string(self):
        """Test record field with empty string."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record=""
        )
        assert tracker.record == ""

    @pytest.mark.unit
    def test_record_with_custom_string(self):
        """Test record field with custom string."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="Perfect Week"
        )
        assert tracker.record == "Perfect Week"


class TestPerformanceTrackerDataclassProperties:
    """Test dataclass properties and behavior."""

    @pytest.mark.unit
    def test_performance_tracker_has_all_attributes(self):
        """Test that PerformanceTracker has all expected attributes."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        assert hasattr(tracker, 'date')
        assert hasattr(tracker, 'total_bankroll')
        assert hasattr(tracker, 'units_won')
        assert hasattr(tracker, 'share_price')
        assert hasattr(tracker, 'record')

    @pytest.mark.unit
    def test_performance_tracker_equality(self):
        """Test that two PerformanceTrackers with same data are equal."""
        tracker1 = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        tracker2 = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        assert tracker1 == tracker2

    @pytest.mark.unit
    def test_performance_tracker_inequality(self):
        """Test that two PerformanceTrackers with different data are not equal."""
        tracker1 = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        tracker2 = PerformanceTracker(
            date="2026-07-10",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        assert tracker1 != tracker2

    @pytest.mark.unit
    def test_performance_tracker_repr(self):
        """Test that PerformanceTracker has a meaningful string representation."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        repr_str = repr(tracker)
        assert 'PerformanceTracker' in repr_str
        assert '2026-07-11' in repr_str
        assert '1000.0' in repr_str

    @pytest.mark.unit
    def test_performance_tracker_is_mutable_by_default(self):
        """Test that PerformanceTracker fields can be modified (default behavior)."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        # Modify a field
        tracker.units_won = 10.0
        assert tracker.units_won == 10.0


class TestPerformanceTrackerEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.unit
    def test_performance_tracker_with_very_small_floats(self):
        """Test PerformanceTracker with very small float values."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=0.01,
            units_won=0.001,
            share_price=0.0001,
            record="0.001-0-0"
        )
        assert tracker.total_bankroll == 0.01
        assert tracker.units_won == 0.001
        assert tracker.share_price == 0.0001

    @pytest.mark.unit
    def test_performance_tracker_with_string_representation(self):
        """Test creating PerformanceTracker and accessing string fields."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        assert isinstance(tracker.date, str)
        assert isinstance(tracker.record, str)
        assert isinstance(tracker.total_bankroll, float)
        assert isinstance(tracker.units_won, float)
        assert isinstance(tracker.share_price, float)

    @pytest.mark.unit
    def test_multiple_performance_trackers_independent(self):
        """Test that multiple PerformanceTrackers are independent."""
        tracker1 = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0"
        )
        tracker2 = PerformanceTracker(
            date="2026-07-12",
            total_bankroll=2000.0,
            units_won=10.0,
            share_price=200.0,
            record="10-1-0"
        )
        # Verify they're independent
        assert tracker1.date != tracker2.date
        assert tracker1.total_bankroll != tracker2.total_bankroll
        assert tracker1.units_won != tracker2.units_won

    @pytest.mark.unit
    def test_performance_tracker_with_unicode_characters(self):
        """Test PerformanceTracker with unicode characters in string fields."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="✓ 5-2-0"
        )
        assert tracker.record == "✓ 5-2-0"

    @pytest.mark.unit
    def test_performance_tracker_with_special_characters(self):
        """Test PerformanceTracker with special characters in string fields."""
        tracker = PerformanceTracker(
            date="2026-07-11",
            total_bankroll=1000.0,
            units_won=5.0,
            share_price=100.0,
            record="5-2-0 (W-L-D)"
        )
        assert tracker.record == "5-2-0 (W-L-D)"
