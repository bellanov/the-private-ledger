"""Unit tests for Account model."""

import pytest

from api.domain.models.account import Account


class TestAccountInstantiation:
    """Test basic instantiation of Account."""

    @pytest.mark.unit
    def test_create_account_with_valid_data(self):
        """Test creating an Account with valid data."""
        roi = {"ytd": "15.5%", "total": "45.2%"}
        account = Account(
            account_id="ACC123",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=25.5,
            return_on_investment=roi,
        )
        assert account.account_id == "ACC123"
        assert account.account_balance == 50000.00
        assert account.current_value == 57500.00
        assert account.shares_owned == 100.0
        assert account.ownership == 25.5
        assert account.return_on_investment == roi

    @pytest.mark.unit
    def test_create_account_with_zero_values(self):
        """Test creating an Account with zero values."""
        account = Account(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={},
        )
        assert account.account_balance == 0.0
        assert account.current_value == 0.0
        assert account.shares_owned == 0.0
        assert account.ownership == 0.0
        assert account.return_on_investment == {}

    @pytest.mark.unit
    def test_create_account_with_negative_values(self):
        """Test creating an Account with negative values."""
        account = Account(
            account_id="ACC002",
            account_balance=-5000.00,
            current_value=-2000.00,
            shares_owned=-10.0,
            ownership=-5.5,
            return_on_investment={"total": "-15.2%"},
        )
        assert account.account_balance == -5000.00
        assert account.current_value == -2000.00
        assert account.shares_owned == -10.0
        assert account.ownership == -5.5

    @pytest.mark.unit
    def test_create_account_with_large_numbers(self):
        """Test creating an Account with large numbers."""
        account = Account(
            account_id="ACC_LARGE",
            account_balance=999999999.99,
            current_value=1234567890.50,
            shares_owned=1000000.0,
            ownership=99.99,
            return_on_investment={"ytd": "500%"},
        )
        assert account.account_balance == 999999999.99
        assert account.current_value == 1234567890.50
        assert account.shares_owned == 1000000.0
        assert account.ownership == 99.99

    @pytest.mark.unit
    def test_create_account_with_decimal_precision(self):
        """Test that Account preserves decimal precision."""
        account = Account(
            account_id="ACC_DECIMAL",
            account_balance=1234.567,
            current_value=5678.901,
            shares_owned=123.456,
            ownership=45.678,
            return_on_investment={"monthly": "2.345%"},
        )
        assert account.account_balance == 1234.567
        assert account.current_value == 5678.901
        assert account.shares_owned == 123.456
        assert account.ownership == 45.678


class TestAccountAccountId:
    """Test account_id field handling."""

    @pytest.mark.unit
    def test_account_id_alphanumeric(self):
        """Test account_id with alphanumeric format."""
        account = Account(
            account_id="ACC123",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.account_id == "ACC123"

    @pytest.mark.unit
    def test_account_id_numeric_only(self):
        """Test account_id with numeric format."""
        account = Account(
            account_id="123456789",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.account_id == "123456789"

    @pytest.mark.unit
    def test_account_id_with_special_characters(self):
        """Test account_id with special characters."""
        account = Account(
            account_id="ACC-123-XYZ",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.account_id == "ACC-123-XYZ"

    @pytest.mark.unit
    def test_account_id_empty_string(self):
        """Test account_id with empty string."""
        account = Account(
            account_id="",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.account_id == ""


class TestAccountReturnOnInvestment:
    """Test return_on_investment dictionary field."""

    @pytest.mark.unit
    def test_roi_empty_dictionary(self):
        """Test return_on_investment with empty dictionary."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.return_on_investment == {}
        assert len(account.return_on_investment) == 0

    @pytest.mark.unit
    def test_roi_single_entry(self):
        """Test return_on_investment with single entry."""
        roi = {"ytd": "15.5%"}
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment == roi
        assert account.return_on_investment["ytd"] == "15.5%"

    @pytest.mark.unit
    def test_roi_multiple_entries(self):
        """Test return_on_investment with multiple entries."""
        roi = {"ytd": "15.5%", "total": "45.2%", "monthly": "2.1%", "weekly": "0.5%"}
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment == roi
        assert len(account.return_on_investment) == 4
        assert account.return_on_investment["ytd"] == "15.5%"
        assert account.return_on_investment["total"] == "45.2%"

    @pytest.mark.unit
    def test_roi_with_negative_percentages(self):
        """Test return_on_investment with negative percentages."""
        roi = {"ytd": "-5.2%", "total": "-12.5%"}
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment["ytd"] == "-5.2%"
        assert account.return_on_investment["total"] == "-12.5%"

    @pytest.mark.unit
    def test_roi_with_decimal_percentages(self):
        """Test return_on_investment with decimal percentages."""
        roi = {"ytd": "15.567%", "total": "45.234%"}
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment["ytd"] == "15.567%"
        assert account.return_on_investment["total"] == "45.234%"

    @pytest.mark.unit
    def test_roi_with_large_percentages(self):
        """Test return_on_investment with large percentages."""
        roi = {"ytd": "500%", "total": "1250%"}
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment["ytd"] == "500%"
        assert account.return_on_investment["total"] == "1250%"

    @pytest.mark.unit
    def test_roi_with_custom_keys(self):
        """Test return_on_investment with custom keys."""
        roi = {
            "1_year": "25.5%",
            "3_year": "75.2%",
            "5_year": "120.5%",
            "inception": "250.0%",
        }
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account.return_on_investment["1_year"] == "25.5%"
        assert account.return_on_investment["inception"] == "250.0%"


class TestAccountDataclassProperties:
    """Test dataclass properties and behavior."""

    @pytest.mark.unit
    def test_account_has_all_attributes(self):
        """Test that Account has all expected attributes."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert hasattr(account, "account_id")
        assert hasattr(account, "account_balance")
        assert hasattr(account, "current_value")
        assert hasattr(account, "shares_owned")
        assert hasattr(account, "ownership")
        assert hasattr(account, "return_on_investment")

    @pytest.mark.unit
    def test_account_equality(self):
        """Test that two Accounts with same data are equal."""
        roi = {"ytd": "15.5%"}
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        account2 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account1 == account2

    @pytest.mark.unit
    def test_account_inequality_different_balance(self):
        """Test that two Accounts with different balances are not equal."""
        roi = {"ytd": "15.5%"}
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        account2 = Account(
            account_id="ACC001",
            account_balance=2000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi,
        )
        assert account1 != account2

    @pytest.mark.unit
    def test_account_inequality_different_roi(self):
        """Test that two Accounts with different ROI are not equal."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "15.5%"},
        )
        account2 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "20.5%"},
        )
        assert account1 != account2

    @pytest.mark.unit
    def test_account_repr(self):
        """Test that Account has a meaningful string representation."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        repr_str = repr(account)
        assert "Account" in repr_str
        assert "ACC001" in repr_str

    @pytest.mark.unit
    def test_account_is_mutable_by_default(self):
        """Test that Account fields can be modified."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        # Modify fields
        account.account_balance = 2000.0
        account.shares_owned = 20.0
        account.return_on_investment = {"ytd": "15.5%"}
        assert account.account_balance == 2000.0
        assert account.shares_owned == 20.0
        assert account.return_on_investment == {"ytd": "15.5%"}


class TestAccountFinancialCalculations:
    """Test financial calculations and relationships."""

    @pytest.mark.unit
    def test_current_value_vs_balance(self):
        """Test relationship between current_value and account_balance."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={},
        )
        gain = account.current_value - account.account_balance
        assert gain == 7500.00
        assert account.current_value > account.account_balance

    @pytest.mark.unit
    def test_price_per_share(self):
        """Test calculating price per share."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=50000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={},
        )
        price_per_share = account.current_value / account.shares_owned
        assert price_per_share == 500.0

    @pytest.mark.unit
    def test_ownership_percentage_validation(self):
        """Test ownership percentage values."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=25.5,
            return_on_investment={},
        )
        assert 0 <= account.ownership <= 100
        assert account.ownership == 25.5

    @pytest.mark.unit
    def test_zero_shares_scenario(self):
        """Test scenario with zero shares."""
        account = Account(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={},
        )
        assert account.shares_owned == 0.0
        assert account.account_balance == 0.0

    @pytest.mark.unit
    def test_loss_scenario(self):
        """Test scenario with investment loss."""
        account = Account(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=40000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={"ytd": "-20%"},
        )
        loss = account.current_value - account.account_balance
        assert loss == -10000.00
        assert account.current_value < account.account_balance


class TestAccountEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.unit
    def test_account_with_very_small_floats(self):
        """Test Account with very small float values."""
        account = Account(
            account_id="ACC001",
            account_balance=0.01,
            current_value=0.02,
            shares_owned=0.001,
            ownership=0.001,
            return_on_investment={},
        )
        assert account.account_balance == 0.01
        assert account.current_value == 0.02
        assert account.shares_owned == 0.001

    @pytest.mark.unit
    def test_account_with_type_validation(self):
        """Test that Account preserves field types."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "15.5%"},
        )
        assert isinstance(account.account_id, str)
        assert isinstance(account.account_balance, float)
        assert isinstance(account.current_value, float)
        assert isinstance(account.shares_owned, float)
        assert isinstance(account.ownership, float)
        assert isinstance(account.return_on_investment, dict)

    @pytest.mark.unit
    def test_multiple_accounts_independent(self):
        """Test that multiple Accounts are independent."""
        account1 = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=25.0,
            return_on_investment={"ytd": "10%"},
        )
        account2 = Account(
            account_id="ACC002",
            account_balance=2000.0,
            current_value=2200.0,
            shares_owned=20.0,
            ownership=75.0,
            return_on_investment={"ytd": "20%"},
        )
        # Verify they're independent
        assert account1.account_id != account2.account_id
        assert account1.account_balance != account2.account_balance
        assert account1.ownership != account2.ownership
        assert account1.return_on_investment != account2.return_on_investment

    @pytest.mark.unit
    def test_account_with_matching_values(self):
        """Test Account where balance equals current_value."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1000.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "0%"},
        )
        assert account.account_balance == account.current_value

    @pytest.mark.unit
    def test_account_with_fractional_ownership(self):
        """Test Account with fractional ownership."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.5,
            ownership=33.333,
            return_on_investment={},
        )
        assert account.shares_owned == 10.5
        assert account.ownership == 33.333

    @pytest.mark.unit
    def test_account_with_long_account_id(self):
        """Test Account with a long account_id."""
        long_id = "ACC" + "0" * 100
        account = Account(
            account_id=long_id,
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        assert account.account_id == long_id
        assert len(account.account_id) == 103

    @pytest.mark.unit
    def test_roi_modification(self):
        """Test modifying return_on_investment dictionary."""
        account = Account(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={},
        )
        # Add entries to the dictionary
        account.return_on_investment["ytd"] = "15.5%"
        account.return_on_investment["total"] = "45.2%"
        assert account.return_on_investment["ytd"] == "15.5%"
        assert len(account.return_on_investment) == 2

    @pytest.mark.unit
    def test_all_fields_zero_except_account_id(self):
        """Test Account with all numeric fields zero."""
        account = Account(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={},
        )
        assert account.account_balance == 0.0
        assert account.current_value == 0.0
        assert account.shares_owned == 0.0
        assert account.ownership == 0.0
