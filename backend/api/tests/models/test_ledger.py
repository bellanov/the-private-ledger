"""Unit tests for Ledger model."""

import pytest
from pydantic import ValidationError

from api.domain.models.ledger import Ledger

# Valid UUID format without hyphens (32 hex characters)
VALID_UUID = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_UUID_2 = "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"


@pytest.mark.unit
class TestLedgerInstantiation:
    """Test basic instantiation of Ledger."""

    def test_create_ledger_with_valid_data(self):
        """Ledger should store all constructor values."""
        ledger = Ledger(
            id=VALID_UUID,
            name="My Ledger",
            description="Test ledger",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger.id == VALID_UUID
        assert ledger.name == "My Ledger"
        assert ledger.description == "Test ledger"
        assert ledger.current_share_price == 10.50
        assert ledger.initial_share_price == 10.00

    def test_create_ledger_with_zero_prices(self):
        """Ledger should handle zero values correctly."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Zero Ledger",
            description="Test with zero prices",
            current_share_price=0.0,
            initial_share_price=0.0,
        )

        assert ledger.current_share_price == 0.0
        assert ledger.initial_share_price == 0.0

    def test_create_ledger_with_decimal_precision(self):
        """Ledger should preserve decimal precision."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Precision Ledger",
            description="High precision test",
            current_share_price=12.3456,
            initial_share_price=10.9876,
        )

        assert ledger.current_share_price == 12.3456
        assert ledger.initial_share_price == 10.9876

    def test_create_ledger_with_camel_case_input(self):
        """Ledger should accept camelCase field names."""
        ledger = Ledger(
            id=VALID_UUID,
            name="CamelCase Ledger",
            description="Test camelCase",
            currentSharePrice=11.00,
            initialSharePrice=10.00,
        )

        assert ledger.current_share_price == 11.00
        assert ledger.initial_share_price == 10.00

    def test_create_ledger_with_empty_description(self):
        """Ledger should accept empty description."""
        ledger = Ledger(
            id=VALID_UUID,
            name="No Description",
            description="",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.description == ""


@pytest.mark.unit
class TestLedgerValidation:
    """Test Pydantic validation behavior."""

    def test_ledger_requires_all_fields(self):
        """Ledger should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Ledger(current_share_price=10.00)

        errors = exc_info.value.errors()
        assert (
            len(errors) >= 4
        )  # Missing required fields (id, name, description, initial_share_price)

    def test_ledger_validates_id_pattern(self):
        """Ledger should validate id matches UUID pattern (32 hex chars)."""
        with pytest.raises(ValidationError):
            Ledger(
                id="invalid-id-format",
                name="Test",
                description="Test",
                current_share_price=10.00,
                initial_share_price=10.00,
            )

    def test_ledger_accepts_valid_uuid(self):
        """Ledger should accept valid UUID format."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Valid UUID",
            description="Test",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.id == VALID_UUID

    def test_ledger_validates_name_required(self):
        """Ledger should require name field."""
        with pytest.raises(ValidationError):
            Ledger(
                id=VALID_UUID,
                description="Test",
                current_share_price=10.00,
                initial_share_price=10.00,
            )

    def test_ledger_validates_description_required(self):
        """Ledger should require description field."""
        with pytest.raises(ValidationError):
            Ledger(
                id=VALID_UUID,
                name="Test",
                current_share_price=10.00,
                initial_share_price=10.00,
            )

    def test_ledger_validates_numeric_fields(self):
        """Ledger should validate numeric fields."""
        with pytest.raises(ValidationError):
            Ledger(
                id=VALID_UUID,
                name="Test",
                description="Test",
                current_share_price="not a number",
                initial_share_price=10.00,
            )

    def test_ledger_converts_numeric_strings(self):
        """Ledger should convert numeric strings to floats."""
        ledger = Ledger(
            id=VALID_UUID,
            name="String Numbers",
            description="Test",
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
                id=VALID_UUID,
                name="Test",
                description="Test",
                current_share_price=None,
                initial_share_price=10.00,
            )

    def test_ledger_validates_initial_share_price_type(self):
        """Ledger should validate initial_share_price is numeric."""
        with pytest.raises(ValidationError):
            Ledger(
                id=VALID_UUID,
                name="Test",
                description="Test",
                current_share_price=10.50,
                initial_share_price=None,
            )


@pytest.mark.unit
class TestLedgerEquality:
    """Test model equality behavior."""

    def test_ledger_equality_same_values(self):
        """Ledgers with identical values should be equal."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger1 == ledger2

    def test_ledger_inequality_different_id(self):
        """Ledgers with different IDs should not be equal."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID_2,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger1 != ledger2

    def test_ledger_inequality_different_name(self):
        """Ledgers with different names should not be equal."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Ledger 1",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID,
            name="Ledger 2",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger1 != ledger2

    def test_ledger_inequality_different_current_price(self):
        """Ledgers with different current prices should not be equal."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=11.00,
            initial_share_price=10.00,
        )

        assert ledger1 != ledger2

    def test_ledger_inequality_different_initial_price(self):
        """Ledgers with different initial prices should not be equal."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID,
            name="Test Ledger",
            description="Test",
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
            id=VALID_UUID,
            name="Test Ledger",
            description="Test description",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        data = ledger.model_dump()

        assert data["id"] == VALID_UUID
        assert data["name"] == "Test Ledger"
        assert data["description"] == "Test description"
        assert data["current_share_price"] == 10.50
        assert data["initial_share_price"] == 10.00

    def test_ledger_model_dump_json(self):
        """model_dump_json should return JSON string."""
        ledger = Ledger(
            id=VALID_UUID,
            name="JSON Test",
            description="Test JSON",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        json_str = ledger.model_dump_json()

        assert isinstance(json_str, str)
        assert VALID_UUID in json_str
        assert "JSON Test" in json_str
        assert "10.5" in json_str or "10.50" in json_str

    def test_ledger_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        ledger = Ledger(
            id=VALID_UUID,
            name="CamelCase Test",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        data = ledger.model_dump(by_alias=True)

        assert "id" in data
        assert "currentSharePrice" in data
        assert "initialSharePrice" in data

    def test_ledger_has_all_attributes(self):
        """Ledger should have all expected attributes."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Attribute Test",
            description="Test",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert hasattr(ledger, "id")
        assert hasattr(ledger, "name")
        assert hasattr(ledger, "description")
        assert hasattr(ledger, "current_share_price")
        assert hasattr(ledger, "initial_share_price")


@pytest.mark.unit
class TestLedgerSharePriceRelationships:
    """Test share price relationship validations."""

    def test_current_price_greater_than_initial(self):
        """Current share price can be greater than initial (profit)."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Profit Ledger",
            description="Test",
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price > ledger.initial_share_price

    def test_current_price_less_than_initial(self):
        """Current share price can be less than initial (loss)."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Loss Ledger",
            description="Test",
            current_share_price=8.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price < ledger.initial_share_price

    def test_current_price_equals_initial(self):
        """Current share price can equal initial (break-even)."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Break-even Ledger",
            description="Test",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == ledger.initial_share_price

    def test_price_change_calculation(self):
        """Calculate price change from initial to current."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Price Change Test",
            description="Test",
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        price_change = ledger.current_share_price - ledger.initial_share_price

        assert price_change == 2.00

    def test_percentage_change_calculation(self):
        """Calculate percentage change from initial to current."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Percentage Change Test",
            description="Test",
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
            id=VALID_UUID,
            name="Small Values",
            description="Test",
            current_share_price=0.01,
            initial_share_price=0.01,
        )

        assert ledger.current_share_price == 0.01
        assert ledger.initial_share_price == 0.01

    def test_ledger_with_large_values(self):
        """Ledger should handle large financial values."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Large Values",
            description="Test",
            current_share_price=15000.00,
            initial_share_price=10000.00,
        )

        assert ledger.current_share_price == 15000.00
        assert ledger.initial_share_price == 10000.00

    def test_ledger_with_negative_values(self):
        """Ledger should handle negative values (edge case)."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Negative Values",
            description="Test",
            current_share_price=-5.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == -5.00
        assert ledger.initial_share_price == 10.00

    def test_ledger_with_fractional_cents(self):
        """Ledger should handle fractional cent values."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Fractional Cents",
            description="Test",
            current_share_price=10.123,
            initial_share_price=10.456,
        )

        assert ledger.current_share_price == 10.123
        assert ledger.initial_share_price == 10.456

    def test_multiple_ledgers_are_independent(self):
        """Multiple Ledger instances should not share state."""
        ledger1 = Ledger(
            id=VALID_UUID,
            name="Ledger 1",
            description="Test 1",
            current_share_price=10.50,
            initial_share_price=10.00,
        )
        ledger2 = Ledger(
            id=VALID_UUID_2,
            name="Ledger 2",
            description="Test 2",
            current_share_price=12.00,
            initial_share_price=10.00,
        )

        assert ledger1.id != ledger2.id
        assert ledger1.current_share_price != ledger2.current_share_price

    def test_ledger_with_same_initial_and_current_price(self):
        """Ledger with identical prices represents break-even."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Break-even",
            description="Test",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        price_difference = ledger.current_share_price - ledger.initial_share_price

        assert price_difference == 0.0

    def test_ledger_with_very_high_precision(self):
        """Ledger should handle high precision decimals."""
        ledger = Ledger(
            id=VALID_UUID,
            name="High Precision",
            description="Test",
            current_share_price=10.123456789,
            initial_share_price=10.987654321,
        )

        assert ledger.current_share_price == 10.123456789
        assert ledger.initial_share_price == 10.987654321

    def test_ledger_with_long_name(self):
        """Ledger should accept long names."""
        long_name = "A" * 100
        ledger = Ledger(
            id=VALID_UUID,
            name=long_name,
            description="Test",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.name == long_name

    def test_ledger_with_special_chars_in_description(self):
        """Ledger should accept special characters in description."""
        special_desc = "Test with !@#$%^&*()_+-=[]{}|;':\",./<>?"
        ledger = Ledger(
            id=VALID_UUID,
            name="Special Chars",
            description=special_desc,
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.description == special_desc


@pytest.mark.unit
class TestLedgerTypicalScenarios:
    """Test typical usage scenarios."""

    def test_startup_scenario(self):
        """Ledger at startup with initial share price."""
        ledger = Ledger(
            id=VALID_UUID,
            name="New Ledger",
            description="Starting fresh",
            current_share_price=10.00,
            initial_share_price=10.00,
        )

        assert ledger.current_share_price == ledger.initial_share_price
        assert ledger.name == "New Ledger"

    def test_profitable_scenario(self):
        """Ledger showing profit after successful betting."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Profitable Ledger",
            description="Great performance",
            current_share_price=12.50,
            initial_share_price=10.00,
        )

        price_increase = ledger.current_share_price - ledger.initial_share_price

        assert price_increase == 2.50
        assert ledger.current_share_price > ledger.initial_share_price

    def test_loss_scenario(self):
        """Ledger showing loss after unsuccessful betting."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Loss Ledger",
            description="Need to recover",
            current_share_price=7.50,
            initial_share_price=10.00,
        )

        price_decrease = ledger.initial_share_price - ledger.current_share_price

        assert price_decrease == 2.50
        assert ledger.current_share_price < ledger.initial_share_price

    def test_small_gain_scenario(self):
        """Ledger showing small incremental gain."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Small Gains",
            description="Steady progress",
            current_share_price=10.05,
            initial_share_price=10.00,
        )

        gain = ledger.current_share_price - ledger.initial_share_price

        assert gain == pytest.approx(0.05)
        assert 0 < gain < 1

    def test_volatile_price_scenario(self):
        """Ledger with highly volatile price movement."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Volatile Ledger",
            description="High risk/reward",
            current_share_price=50.00,
            initial_share_price=10.00,
        )

        price_multiple = ledger.current_share_price / ledger.initial_share_price

        assert price_multiple == 5.0
        assert ledger.current_share_price > ledger.initial_share_price * 4

    def test_ledger_with_descriptive_metadata(self):
        """Ledger with meaningful name and description."""
        ledger = Ledger(
            id=VALID_UUID,
            name="Sports Betting Account",
            description="Primary sports betting ledger for Q3 2024",
            current_share_price=10.50,
            initial_share_price=10.00,
        )

        assert ledger.name == "Sports Betting Account"
        assert "2024" in ledger.description
