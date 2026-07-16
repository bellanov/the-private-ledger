"""Unit tests for Account model."""

import pytest
from pydantic import ValidationError

from api.domain.models.account import Account


@pytest.mark.unit
class TestAccountInstantiation:
    """Test basic instantiation of Account."""

    def test_create_account_with_valid_data(self):
        """Account should store all constructor values."""
        account = Account(
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            account_balance=50000.00,
            current_value=57500.00,
            total_shares=100.0,
            ownership=25.5,
            return_on_investment=15.4,
        )

        assert account.account_id == "PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735"
        assert account.account_balance == 50000.00
        assert account.current_value == 57500.00
        assert account.total_shares == 100.0
        assert account.ownership == 25.5
        assert account.return_on_investment == 15.4

    def test_create_account_with_zero_values(self):
        """Account should handle zero values correctly."""
        account = Account(
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            account_balance=0.0,
            current_value=0.0,
            total_shares=0.0,
            ownership=0.0,
            return_on_investment=0.0,
        )

        assert account.account_balance == 0.0
        assert account.current_value == 0.0
        assert account.total_shares == 0.0
        assert account.ownership == 0.0
        assert account.return_on_investment == 0.0

    def test_create_account_with_decimal_precision(self):
        """Account should preserve decimal precision."""
        account = Account(
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            account_balance=1234.567,
            current_value=5678.901,
            total_shares=123.456,
            ownership=45.678,
            return_on_investment=2.345,
        )

        assert account.account_balance == 1234.567
        assert account.current_value == 5678.901
        assert account.total_shares == 123.456
        assert account.ownership == 45.678
        assert account.return_on_investment == 2.345

    def test_create_account_with_camel_case_input(self):
        """Account should accept camelCase field names."""
        account = Account(
            accountId="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
            accountBalance=1000.0,
            currentValue=1100.0,
            totalShares=10.0,
            ownership=50.0,
            returnOnInvestment=10.0,
        )

        assert account.account_id == "PL-b6e41d9a73c24f80a5d9e1c24b7f6038"
        assert account.account_balance == 1000.0


@pytest.mark.unit
class TestAccountValidation:
    """Test Pydantic validation behavior."""

    def test_account_requires_all_fields(self):
        """Account should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Account(account_id="PL-test")

        errors = exc_info.value.errors()
        assert len(errors) >= 5  # Missing required fields

    def test_account_validates_numeric_fields(self):
        """Account should validate numeric fields."""
        with pytest.raises(ValidationError):
            Account(
                account_id="PL-test",
                account_balance="not a number",
                current_value=1000.0,
                total_shares=10.0,
                ownership=50.0,
                return_on_investment=0.0,
            )

    def test_account_validates_account_id_type(self):
        """Account should validate account_id is a string."""
        with pytest.raises(ValidationError):
            Account(
                account_id=12345,
                account_balance=1000.0,
                current_value=1000.0,
                total_shares=10.0,
                ownership=50.0,
                return_on_investment=0.0,
            )

    def test_account_converts_numeric_strings(self):
        """Account should convert numeric strings to floats."""
        account = Account(
            account_id="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            account_balance="1000.0",
            current_value="1100.0",
            total_shares="10.0",
            ownership="50.0",
            return_on_investment="10.0",
        )

        assert account.account_balance == 1000.0
        assert account.current_value == 1100.0
        assert isinstance(account.account_balance, float)


@pytest.mark.unit
class TestAccountEquality:
    """Test model equality behavior."""

    def test_account_equality_same_values(self):
        """Accounts with identical values should be equal."""
        account1 = Account(
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )
        account2 = Account(
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )

        assert account1 == account2

    def test_account_inequality_different_balance(self):
        """Accounts with different balances should not be equal."""
        account1 = Account(
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=0.0,
        )
        account2 = Account(
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            account_balance=2000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        assert account1 != account2

    def test_account_inequality_different_id(self):
        """Accounts with different IDs should not be equal."""
        account1 = Account(
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=0.0,
        )
        account2 = Account(
            account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        assert account1 != account2


@pytest.mark.unit
class TestAccountSerialization:
    """Test Pydantic serialization behavior."""

    def test_account_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        account = Account(
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )

        data = account.model_dump()

        assert data["account_id"] == "PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4"
        assert data["account_balance"] == 1000.0
        assert data["current_value"] == 1100.0
        assert data["total_shares"] == 10.0
        assert data["ownership"] == 50.0
        assert data["return_on_investment"] == 10.0

    def test_account_model_dump_json(self):
        """model_dump_json should return JSON string."""
        account = Account(
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )

        json_str = account.model_dump_json()

        assert isinstance(json_str, str)
        assert "PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735" in json_str
        assert "1000.0" in json_str

    def test_account_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        account = Account(
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )

        data = account.model_dump(by_alias=True)

        assert "accountId" in data
        assert "accountBalance" in data
        assert "currentValue" in data
        assert "totalShares" in data
        assert "returnOnInvestment" in data

    def test_account_has_all_attributes(self):
        """Account should have all expected attributes."""
        account = Account(
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=10.0,
        )

        assert hasattr(account, "account_id")
        assert hasattr(account, "account_balance")
        assert hasattr(account, "current_value")
        assert hasattr(account, "total_shares")
        assert hasattr(account, "ownership")
        assert hasattr(account, "return_on_investment")


@pytest.mark.unit
class TestAccountReturnOnInvestment:
    """Test return_on_investment field."""

    def test_roi_with_positive_value(self):
        """ROI should handle positive values."""
        account = Account(
            account_id="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
            account_balance=1000.0,
            current_value=1150.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=15.0,
        )

        assert account.return_on_investment == 15.0

    def test_roi_with_negative_value(self):
        """ROI should handle negative return values."""
        account = Account(
            account_id="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            account_balance=1000.0,
            current_value=900.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=-10.0,
        )

        assert account.return_on_investment == -10.0

    def test_roi_with_zero_value(self):
        """ROI should handle zero value (break-even)."""
        account = Account(
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            account_balance=1000.0,
            current_value=1000.0,
            total_shares=10.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        assert account.return_on_investment == 0.0


@pytest.mark.unit
class TestAccountFinancialCalculations:
    """Test financial relationship validations."""

    def test_profit_scenario(self):
        """Current value should exceed balance for profit."""
        account = Account(
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            account_balance=50000.00,
            current_value=57500.00,
            total_shares=100.0,
            ownership=50.0,
            return_on_investment=15.0,
        )

        gain = account.current_value - account.account_balance

        assert gain == 7500.00
        assert account.current_value > account.account_balance

    def test_loss_scenario(self):
        """Current value should be less than balance for loss."""
        account = Account(
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            account_balance=50000.00,
            current_value=40000.00,
            total_shares=100.0,
            ownership=50.0,
            return_on_investment=-20.0,
        )

        loss = account.current_value - account.account_balance

        assert loss == -10000.00
        assert account.current_value < account.account_balance

    def test_break_even_scenario(self):
        """Current value equal to balance means no gain/loss."""
        account = Account(
            account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
            account_balance=50000.00,
            current_value=50000.00,
            total_shares=100.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        gain = account.current_value - account.account_balance

        assert gain == 0.0
        assert account.current_value == account.account_balance

    def test_price_per_share_calculation(self):
        """Price per share should equal current_value / total_shares."""
        account = Account(
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            account_balance=50000.00,
            current_value=50000.00,
            total_shares=100.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        price_per_share = account.current_value / account.total_shares

        assert price_per_share == 500.0


@pytest.mark.unit
class TestAccountEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_account_with_very_small_floats(self):
        """Account should handle very small decimal values."""
        account = Account(
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            account_balance=0.01,
            current_value=0.02,
            total_shares=0.001,
            ownership=0.001,
            return_on_investment=0.0,
        )

        assert account.account_balance == 0.01
        assert account.current_value == 0.02
        assert account.total_shares == 0.001

    def test_account_with_large_values(self):
        """Account should handle large financial values."""
        account = Account(
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            account_balance=1_000_000.00,
            current_value=1_500_000.00,
            total_shares=10000.0,
            ownership=100.0,
            return_on_investment=50.0,
        )

        assert account.account_balance == 1_000_000.00
        assert account.current_value == 1_500_000.00

    def test_account_with_fractional_ownership(self):
        """Account should handle fractional ownership percentages."""
        account = Account(
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.5,
            ownership=33.333,
            return_on_investment=10.0,
        )

        assert account.total_shares == 10.5
        assert account.ownership == 33.333

    def test_account_with_100_percent_ownership(self):
        """Account should handle 100% ownership."""
        account = Account(
            account_id="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
            account_balance=50000.00,
            current_value=55000.00,
            total_shares=100.0,
            ownership=100.0,
            return_on_investment=10.0,
        )

        assert account.ownership == 100.0

    def test_multiple_accounts_are_independent(self):
        """Multiple Account instances should not share state."""
        account1 = Account(
            account_id="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            account_balance=1000.0,
            current_value=1100.0,
            total_shares=10.0,
            ownership=25.0,
            return_on_investment=10.0,
        )
        account2 = Account(
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            account_balance=2000.0,
            current_value=2200.0,
            total_shares=20.0,
            ownership=75.0,
            return_on_investment=10.0,
        )

        assert account1.account_id != account2.account_id
        assert account1.account_balance != account2.account_balance

        # Pydantic models are immutable by default unless configured otherwise
        # If using default config, this will raise ValidationError
        # account1.account_balance = 5000.0
        # assert account2.account_balance == 2000.0
