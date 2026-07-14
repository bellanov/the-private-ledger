"""Unit tests for Account model."""

from dataclasses import asdict

import pytest

from api.domain.models.account import Account


@pytest.mark.unit
class TestAccountInstantiation:
    """Test basic instantiation of Account."""

    def test_create_account_with_valid_data(self):
        """Account should store all constructor values."""
        account = Account(
            account_id="ACC123",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=25.5,
            return_on_investment=15.4,
        )

        assert account.account_id == "ACC123"
        assert account.account_balance == 50000.00
        assert account.current_value == 57500.00
        assert account.shares_owned == 100.0
        assert account.ownership == 25.5
        assert account.return_on_investment == 15.4

    def test_create_account_with_zero_values(self):
        """Account should handle zero values correctly."""
        account = Account(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment=0,
        )

        assert account.account_balance == 0.0
        assert account.current_value == 0.0
        assert account.shares_owned == 0.0
        assert account.ownership == 0.0
        assert account.return_on_investment == 0

    def test_create_account_with_decimal_precision(self):
        """Account should preserve decimal precision."""
        account = Account(
            account_id="ACC_DECIMAL",
            account_balance=1234.567,
            current_value=5678.901,
            shares_owned=123.456,
            ownership=45.678,
            return_on_investment=2.345,
        )

        assert account.account_balance == 1234.567
        assert account.current_value == 5678.901
        assert account.shares_owned == 123.456
        assert account.ownership == 45.678


@pytest.mark.unit
class TestAccountEquality:
    """Test dataclass equality behavior."""

    def test_account_equality_same_values(self):
        """Accounts with identical values should be equal."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=15.5,
        )
        account2 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=15.5,
        )

        assert account1 == account2

    def test_account_inequality_different_balance(self):
        """Accounts with different balances should not be equal."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )
        account2 = Account(
            account_id="ACC001",
            account_balance=2000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )

        assert account1 != account2

    def test_account_inequality_different_id(self):
        """Accounts with different IDs should not be equal."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )
        account2 = Account(
            account_id="ACC002",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )

        assert account1 != account2


@pytest.mark.unit
class TestAccountReturnOnInvestment:
    """Test return_on_investment field."""

    def test_roi_with_negative_percentages(self):
        """ROI should handle negative return values."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=900.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=-5.2,
        )

        assert account.return_on_investment == -5.2


@pytest.mark.unit
class TestAccountDataclass:
    """Test dataclass-specific behavior."""

    def test_account_has_all_attributes(self):
        """Account should have all expected attributes."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )

        assert hasattr(account, "account_id")
        assert hasattr(account, "account_balance")
        assert hasattr(account, "current_value")
        assert hasattr(account, "shares_owned")
        assert hasattr(account, "ownership")
        assert hasattr(account, "return_on_investment")

    def test_account_repr_contains_class_name(self):
        """repr should include class name."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )

        repr_str = repr(account)

        assert "Account" in repr_str
        assert "ACC001" in repr_str

    def test_account_fields_are_mutable(self):
        """Default dataclass should allow field modification."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=0,
        )

        account.account_balance = 2000.0
        account.shares_owned = 20.0

        assert account.account_balance == 2000.0
        assert account.shares_owned == 20.0


@pytest.mark.unit
class TestAccountFinancialCalculations:
    """Test financial relationship validations."""

    def test_profit_scenario(self):
        """Current value should exceed balance for profit."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment=15.0,
        )

        gain = account.current_value - account.account_balance

        assert gain == 7500.00
        assert account.current_value > account.account_balance

    def test_loss_scenario(self):
        """Current value should be less than balance for loss."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=40000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment=-20.0,
        )

        loss = account.current_value - account.account_balance

        assert loss == -10000.00
        assert account.current_value < account.account_balance

    def test_break_even_scenario(self):
        """Current value equal to balance means no gain/loss."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=50000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment=0.0,
        )

        gain = account.current_value - account.account_balance

        assert gain == 0.0
        assert account.current_value == account.account_balance

    def test_price_per_share_calculation(self):
        """Price per share should equal current_value / shares_owned."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=50000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment=0,
        )

        price_per_share = account.current_value / account.shares_owned

        assert price_per_share == 500.0


@pytest.mark.unit
class TestAccountEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_account_with_very_small_floats(self):
        """Account should handle very small decimal values."""
        account = Account(
            account_id="ACC001",
            account_balance=0.01,
            current_value=0.02,
            shares_owned=0.001,
            ownership=0.001,
            return_on_investment=0,
        )

        assert account.account_balance == 0.01
        assert account.current_value == 0.02
        assert account.shares_owned == 0.001

    def test_account_with_large_values(self):
        """Account should handle large financial values."""
        account = Account(
            account_id="ACC_WHALE",
            account_balance=1_000_000.00,
            current_value=1_500_000.00,
            shares_owned=10000.0,
            ownership=100.0,
            return_on_investment=50.0,
        )

        assert account.account_balance == 1_000_000.00
        assert account.current_value == 1_500_000.00

    def test_account_with_fractional_ownership(self):
        """Account should handle fractional ownership percentages."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.5,
            ownership=33.333,
            return_on_investment=0,
        )

        assert account.shares_owned == 10.5
        assert account.ownership == 33.333

    def test_account_with_100_percent_ownership(self):
        """Account should handle 100% ownership."""
        account = Account(
            account_id="ACC_FULL",
            account_balance=50000.00,
            current_value=55000.00,
            shares_owned=100.0,
            ownership=100.0,
            return_on_investment=10,
        )

        assert account.ownership == 100.0

    def test_multiple_accounts_are_independent(self):
        """Multiple Account instances should not share state."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=25.0,
            return_on_investment=10.0,
        )
        account2 = Account(
            account_id="ACC002",
            account_balance=2000.0,
            current_value=2200.0,
            shares_owned=20.0,
            ownership=75.0,
            return_on_investment=20.0,
        )

        assert account1.account_id != account2.account_id
        assert account1.account_balance != account2.account_balance
        assert account1.return_on_investment != account2.return_on_investment

        # Modifying one should not affect the other
        account1.account_balance = 5000.0
        assert account2.account_balance == 2000.0
