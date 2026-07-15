"""Unit tests for Ledger model."""

import pytest
from pydantic import ValidationError

from api.domain.models.ledger import Ledger


@pytest.mark.unit
class TestLedgerInstantiation:
    """Test basic instantiation of Ledger."""

    def test_create_ledger_with_valid_data(self):
        """Ledger should store all constructor values."""
        ledger = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == 10.50
        assert ledger.initial_share_price == 10.00

    def test_create_ledger_with_zero_values(self):
        """Ledger should handle zero values correctly."""
        ledger = Ledger(
            current_share_price=0.0,
            initial_share_price=0.0,
        )

        assert ledger.current_share_price == 0.0
        assert ledger.initial_share_price == 0.0

    def test_create_ledger_with_decimal_precision(self):
        """Ledger should preserve decimal precision."""
        ledger = Ledger(
            current_share_price=12.3456,
            initial_share_price=10.9876,
        )

        assert ledger.current_share_price == 12.3456
        assert ledger.initial_share_price == 10.9876

    def test_create_ledger_with_camel_case_input(self):
        """Ledger should accept camelCase field names."""
        ledger = Ledger(
            currentSharePrice=11.00,
            initialSharePrice=10.00,
        )

        assert ledger.current_share_price == 11.00
        assert ledger.initial_share_price == 10.00


@pytest.mark.unit
class TestLedgerValidation:
    """Test Pydantic validation behavior."""

    def test_ledger_requires_all_fields(self):
        """Ledger should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Ledger(current_share_price=10.00)

        errors = exc_info.value.errors()
        assert len(errors) >= 1  # Missing required field

    def test_ledger_validates_numeric_fields(self):
        """Ledger should validate numeric fields."""
        with pytest.raises(ValidationError):
            Ledger(
                current_share_price="not a number",
                initial_share_price=10.00,
            )

    def test_ledger_converts_numeric_strings(self):
        """Ledger should convert numeric strings to floats."""
        ledger = Ledger(
            current_share_price="10.50",
            initial_share_price="10.00",
        )

        assert ledger.current_share_price == 10.50
        assert ledger.initial_share_price == 10.00
        assert isinstance(ledger.current_share_price, float)

    def test_ledger_validates_current_share_price_type(self):
        """Ledger should validate current_share_price is numeric."""
        with pytest.raises(ValidationError):
            Ledger(
                current_share_price=None,
                initial_share_price=10.00,
            )

    def test_ledger_validates_initial_share_price_type(self):
        """Ledger should validate initial_share_price is numeric."""
        with pytest.raises(ValidationError):
            Ledger(
                current_share_price=10.50,
                initial_share_price=None,
            )


@pytest.mark.unit
class TestLedgerEquality:
    """Test model equality behavior."""

    def test_ledger_equality_same_values(self):
        """Ledgers with identical values should be equal."""
        ledger1 = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger1 == ledger2

    def test_ledger_inequality_different_current_price(self):
        """Ledgers with different current prices should not be equal."""
        ledger1 = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            current_share_price=11.00,
            initial_share_price=10.00,
        )

        assert ledger1 != ledger2

    def test_ledger_inequality_different_initial_price(self):
        """Ledgers with different initial prices should not be equal."""
        ledger1 = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            current_share_price=10.50,
            initial_share_price=9.50,
        )

        assert ledger1 != ledger2


@pytest.mark.unit
class TestLedgerSerialization:
    """Test Pydantic serialization behavior."""

    def test_ledger_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        ledger = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        data = ledger.model_dump()

        assert data["current_share_price"] == 10.50
        assert data["initial_share_price"] == 10.00

    def test_ledger_model_dump_json(self):
        """model_dump_json should return JSON string."""
        ledger = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        json_str = ledger.model_dump_json()

        assert isinstance(json_str, str)
        assert "10.5" in json_str or "10.50" in json_str
        assert "10.0" in json_str or "10.00" in json_str

    def test_ledger_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        ledger = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        data = ledger.model_dump(by_alias=True)

        assert "currentSharePrice" in data
        assert "initialSharePrice" in data

    def test_ledger_has_all_attributes(self):
        """Ledger should have all expected attributes."""
        ledger = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert hasattr(ledger, "current_share_price")
        assert hasattr(ledger, "initial_share_price")


@pytest.mark.unit
class TestLedgerSharePriceRelationships:
    """Test share price relationship validations."""

    def test_current_price_greater_than_initial(self):
        """Current share price can be greater than initial (profit)."""
        ledger = Ledger(
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price > ledger.initial_share_price

    def test_current_price_less_than_initial(self):
        """Current share price can be less than initial (loss)."""
        ledger = Ledger(
            current_share_price=8.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price < ledger.initial_share_price

    def test_current_price_equals_initial(self):
        """Current share price can equal initial (break-even)."""
        ledger = Ledger(
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == ledger.initial_share_price

    def test_price_change_calculation(self):
        """Calculate price change from initial to current."""
        ledger = Ledger(
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        price_change = ledger.current_share_price - ledger.initial_share_price

        assert price_change == 2.00

    def test_percentage_change_calculation(self):
        """Calculate percentage change from initial to current."""
        ledger = Ledger(
            current_share_price=11.00,
            initial_share_price=10.00,
        )

        percentage_change = (
            (ledger.current_share_price - ledger.initial_share_price)
            / ledger.initial_share_price
            * 100
        )

        assert percentage_change == 10.0


@pytest.mark.unit
class TestLedgerEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_ledger_with_very_small_floats(self):
        """Ledger should handle very small decimal values."""
        ledger = Ledger(
            current_share_price=0.01,
            initial_share_price=0.01,
        )

        assert ledger.current_share_price == 0.01
        assert ledger.initial_share_price == 0.01

    def test_ledger_with_large_values(self):
        """Ledger should handle large financial values."""
        ledger = Ledger(
            current_share_price=15000.00,
            initial_share_price=10000.00,
        )

        assert ledger.current_share_price == 15000.00
        assert ledger.initial_share_price == 10000.00

    def test_ledger_with_negative_values(self):
        """Ledger should handle negative values (edge case)."""
        ledger = Ledger(
            current_share_price=-5.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == -5.00
        assert ledger.initial_share_price == 10.00

    def test_ledger_with_fractional_cents(self):
        """Ledger should handle fractional cent values."""
        ledger = Ledger(
            current_share_price=10.123,
            initial_share_price=10.456,
        )

        assert ledger.current_share_price == 10.123
        assert ledger.initial_share_price == 10.456

    def test_multiple_ledgers_are_independent(self):
        """Multiple Ledger instances should not share state."""
        ledger1 = Ledger(
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        assert ledger1.current_share_price != ledger2.current_share_price

    def test_ledger_with_same_initial_and_current_price(self):
        """Ledger with identical prices represents break-even."""
        ledger = Ledger(
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        price_difference = ledger.current_share_price - ledger.initial_share_price

        assert price_difference == 0.0

    def test_ledger_with_very_high_precision(self):
        """Ledger should handle high precision decimals."""
        ledger = Ledger(
            current_share_price=10.123456789,
            initial_share_price=10.987654321,
        )

        assert ledger.current_share_price == 10.123456789
        assert ledger.initial_share_price == 10.987654321


@pytest.mark.unit
class TestLedgerTypicalScenarios:
    """Test typical usage scenarios."""

    def test_startup_scenario(self):
        """Ledger at startup with initial share price."""
        ledger = Ledger(
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == ledger.initial_share_price

    def test_profitable_scenario(self):
        """Ledger showing profit after successful betting."""
        ledger = Ledger(
            current_share_price=12.50,
            initial_share_price=10.00,
        )

        price_increase = ledger.current_share_price - ledger.initial_share_price

        assert price_increase == 2.50
        assert ledger.current_share_price > ledger.initial_share_price

    def test_loss_scenario(self):
        """Ledger showing loss after unsuccessful betting."""
        ledger = Ledger(
            current_share_price=7.50,
            initial_share_price=10.00,
        )

        price_decrease = ledger.initial_share_price - ledger.current_share_price

        assert price_decrease == 2.50
        assert ledger.current_share_price < ledger.initial_share_price

    def test_small_gain_scenario(self):
        """Ledger showing small incremental gain."""
        ledger = Ledger(
            current_share_price=10.05,
            initial_share_price=10.00,
        )

        gain = ledger.current_share_price - ledger.initial_share_price

        assert gain == pytest.approx(0.05)
        assert 0 < gain < 1

    def test_volatile_price_scenario(self):
        """Ledger with highly volatile price movement."""
        ledger = Ledger(
            current_share_price=50.00,
            initial_share_price=10.00,
        )

        price_multiple = ledger.current_share_price / ledger.initial_share_price

        assert price_multiple == 5.0
        assert ledger.current_share_price > ledger.initial_share_price * 4
