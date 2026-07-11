"""Unit tests for MasterTrackingSheet model."""

import pytest
from api.domain.models.master_tracking_sheet import MasterTrackingSheet


class TestMasterTrackingSheetInstantiation:
    """Test basic instantiation of MasterTrackingSheet."""

    @pytest.mark.unit
    def test_create_master_tracking_sheet_with_valid_data(self):
        """Test creating a MasterTrackingSheet with valid data."""
        roi = {"ytd": "15.5%", "total": "45.2%"}
        sheet = MasterTrackingSheet(
            account_id="ACC123",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=25.5,
            return_on_investment=roi
        )
        assert sheet.account_id == "ACC123"
        assert sheet.account_balance == 50000.00
        assert sheet.current_value == 57500.00
        assert sheet.shares_owned == 100.0
        assert sheet.ownership == 25.5
        assert sheet.return_on_investment == roi

    @pytest.mark.unit
    def test_create_master_tracking_sheet_with_zero_values(self):
        """Test creating a MasterTrackingSheet with zero values."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={}
        )
        assert sheet.account_balance == 0.0
        assert sheet.current_value == 0.0
        assert sheet.shares_owned == 0.0
        assert sheet.ownership == 0.0
        assert sheet.return_on_investment == {}

    @pytest.mark.unit
    def test_create_master_tracking_sheet_with_negative_values(self):
        """Test creating a MasterTrackingSheet with negative values."""
        sheet = MasterTrackingSheet(
            account_id="ACC002",
            account_balance=-5000.00,
            current_value=-2000.00,
            shares_owned=-10.0,
            ownership=-5.5,
            return_on_investment={"total": "-15.2%"}
        )
        assert sheet.account_balance == -5000.00
        assert sheet.current_value == -2000.00
        assert sheet.shares_owned == -10.0
        assert sheet.ownership == -5.5

    @pytest.mark.unit
    def test_create_master_tracking_sheet_with_large_numbers(self):
        """Test creating a MasterTrackingSheet with large numbers."""
        sheet = MasterTrackingSheet(
            account_id="ACC_LARGE",
            account_balance=999999999.99,
            current_value=1234567890.50,
            shares_owned=1000000.0,
            ownership=99.99,
            return_on_investment={"ytd": "500%"}
        )
        assert sheet.account_balance == 999999999.99
        assert sheet.current_value == 1234567890.50
        assert sheet.shares_owned == 1000000.0
        assert sheet.ownership == 99.99

    @pytest.mark.unit
    def test_create_master_tracking_sheet_with_decimal_precision(self):
        """Test that MasterTrackingSheet preserves decimal precision."""
        sheet = MasterTrackingSheet(
            account_id="ACC_DECIMAL",
            account_balance=1234.567,
            current_value=5678.901,
            shares_owned=123.456,
            ownership=45.678,
            return_on_investment={"monthly": "2.345%"}
        )
        assert sheet.account_balance == 1234.567
        assert sheet.current_value == 5678.901
        assert sheet.shares_owned == 123.456
        assert sheet.ownership == 45.678


class TestMasterTrackingSheetAccountId:
    """Test account_id field handling."""

    @pytest.mark.unit
    def test_account_id_alphanumeric(self):
        """Test account_id with alphanumeric format."""
        sheet = MasterTrackingSheet(
            account_id="ACC123",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.account_id == "ACC123"

    @pytest.mark.unit
    def test_account_id_numeric_only(self):
        """Test account_id with numeric format."""
        sheet = MasterTrackingSheet(
            account_id="123456789",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.account_id == "123456789"

    @pytest.mark.unit
    def test_account_id_with_special_characters(self):
        """Test account_id with special characters."""
        sheet = MasterTrackingSheet(
            account_id="ACC-123-XYZ",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.account_id == "ACC-123-XYZ"

    @pytest.mark.unit
    def test_account_id_empty_string(self):
        """Test account_id with empty string."""
        sheet = MasterTrackingSheet(
            account_id="",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.account_id == ""


class TestMasterTrackingSheetReturnOnInvestment:
    """Test return_on_investment dictionary field."""

    @pytest.mark.unit
    def test_roi_empty_dictionary(self):
        """Test return_on_investment with empty dictionary."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.return_on_investment == {}
        assert len(sheet.return_on_investment) == 0

    @pytest.mark.unit
    def test_roi_single_entry(self):
        """Test return_on_investment with single entry."""
        roi = {"ytd": "15.5%"}
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment == roi
        assert sheet.return_on_investment["ytd"] == "15.5%"

    @pytest.mark.unit
    def test_roi_multiple_entries(self):
        """Test return_on_investment with multiple entries."""
        roi = {
            "ytd": "15.5%",
            "total": "45.2%",
            "monthly": "2.1%",
            "weekly": "0.5%"
        }
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment == roi
        assert len(sheet.return_on_investment) == 4
        assert sheet.return_on_investment["ytd"] == "15.5%"
        assert sheet.return_on_investment["total"] == "45.2%"

    @pytest.mark.unit
    def test_roi_with_negative_percentages(self):
        """Test return_on_investment with negative percentages."""
        roi = {"ytd": "-5.2%", "total": "-12.5%"}
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment["ytd"] == "-5.2%"
        assert sheet.return_on_investment["total"] == "-12.5%"

    @pytest.mark.unit
    def test_roi_with_decimal_percentages(self):
        """Test return_on_investment with decimal percentages."""
        roi = {"ytd": "15.567%", "total": "45.234%"}
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment["ytd"] == "15.567%"
        assert sheet.return_on_investment["total"] == "45.234%"

    @pytest.mark.unit
    def test_roi_with_large_percentages(self):
        """Test return_on_investment with large percentages."""
        roi = {"ytd": "500%", "total": "1250%"}
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment["ytd"] == "500%"
        assert sheet.return_on_investment["total"] == "1250%"

    @pytest.mark.unit
    def test_roi_with_custom_keys(self):
        """Test return_on_investment with custom keys."""
        roi = {
            "1_year": "25.5%",
            "3_year": "75.2%",
            "5_year": "120.5%",
            "inception": "250.0%"
        }
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet.return_on_investment["1_year"] == "25.5%"
        assert sheet.return_on_investment["inception"] == "250.0%"


class TestMasterTrackingSheetDataclassProperties:
    """Test dataclass properties and behavior."""

    @pytest.mark.unit
    def test_tracking_sheet_has_all_attributes(self):
        """Test that MasterTrackingSheet has all expected attributes."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert hasattr(sheet, 'account_id')
        assert hasattr(sheet, 'account_balance')
        assert hasattr(sheet, 'current_value')
        assert hasattr(sheet, 'shares_owned')
        assert hasattr(sheet, 'ownership')
        assert hasattr(sheet, 'return_on_investment')

    @pytest.mark.unit
    def test_tracking_sheet_equality(self):
        """Test that two MasterTrackingSheets with same data are equal."""
        roi = {"ytd": "15.5%"}
        sheet1 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        sheet2 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet1 == sheet2

    @pytest.mark.unit
    def test_tracking_sheet_inequality_different_balance(self):
        """Test that two MasterTrackingSheets with different balances are not equal."""
        roi = {"ytd": "15.5%"}
        sheet1 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        sheet2 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=2000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment=roi
        )
        assert sheet1 != sheet2

    @pytest.mark.unit
    def test_tracking_sheet_inequality_different_roi(self):
        """Test that two MasterTrackingSheets with different ROI are not equal."""
        sheet1 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "15.5%"}
        )
        sheet2 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "20.5%"}
        )
        assert sheet1 != sheet2

    @pytest.mark.unit
    def test_tracking_sheet_repr(self):
        """Test that MasterTrackingSheet has a meaningful string representation."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        repr_str = repr(sheet)
        assert 'MasterTrackingSheet' in repr_str
        assert 'ACC001' in repr_str

    @pytest.mark.unit
    def test_tracking_sheet_is_mutable_by_default(self):
        """Test that MasterTrackingSheet fields can be modified."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        # Modify fields
        sheet.account_balance = 2000.0
        sheet.shares_owned = 20.0
        sheet.return_on_investment = {"ytd": "15.5%"}
        assert sheet.account_balance == 2000.0
        assert sheet.shares_owned == 20.0
        assert sheet.return_on_investment == {"ytd": "15.5%"}


class TestMasterTrackingSheetFinancialCalculations:
    """Test financial calculations and relationships."""

    @pytest.mark.unit
    def test_current_value_vs_balance(self):
        """Test relationship between current_value and account_balance."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={}
        )
        gain = sheet.current_value - sheet.account_balance
        assert gain == 7500.00
        assert sheet.current_value > sheet.account_balance

    @pytest.mark.unit
    def test_price_per_share(self):
        """Test calculating price per share."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=50000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={}
        )
        price_per_share = sheet.current_value / sheet.shares_owned
        assert price_per_share == 500.0

    @pytest.mark.unit
    def test_ownership_percentage_validation(self):
        """Test ownership percentage values."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=57500.00,
            shares_owned=100.0,
            ownership=25.5,
            return_on_investment={}
        )
        assert 0 <= sheet.ownership <= 100
        assert sheet.ownership == 25.5

    @pytest.mark.unit
    def test_zero_shares_scenario(self):
        """Test scenario with zero shares."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={}
        )
        assert sheet.shares_owned == 0.0
        assert sheet.account_balance == 0.0

    @pytest.mark.unit
    def test_loss_scenario(self):
        """Test scenario with investment loss."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=50000.00,
            current_value=40000.00,
            shares_owned=100.0,
            ownership=50.0,
            return_on_investment={"ytd": "-20%"}
        )
        loss = sheet.current_value - sheet.account_balance
        assert loss == -10000.00
        assert sheet.current_value < sheet.account_balance


class TestMasterTrackingSheetEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.unit
    def test_tracking_sheet_with_very_small_floats(self):
        """Test MasterTrackingSheet with very small float values."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=0.01,
            current_value=0.02,
            shares_owned=0.001,
            ownership=0.001,
            return_on_investment={}
        )
        assert sheet.account_balance == 0.01
        assert sheet.current_value == 0.02
        assert sheet.shares_owned == 0.001

    @pytest.mark.unit
    def test_tracking_sheet_with_type_validation(self):
        """Test that MasterTrackingSheet preserves field types."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "15.5%"}
        )
        assert isinstance(sheet.account_id, str)
        assert isinstance(sheet.account_balance, float)
        assert isinstance(sheet.current_value, float)
        assert isinstance(sheet.shares_owned, float)
        assert isinstance(sheet.ownership, float)
        assert isinstance(sheet.return_on_investment, dict)

    @pytest.mark.unit
    def test_multiple_tracking_sheets_independent(self):
        """Test that multiple MasterTrackingSheets are independent."""
        sheet1 = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=25.0,
            return_on_investment={"ytd": "10%"}
        )
        sheet2 = MasterTrackingSheet(
            account_id="ACC002",
            account_balance=2000.0,
            current_value=2200.0,
            shares_owned=20.0,
            ownership=75.0,
            return_on_investment={"ytd": "20%"}
        )
        # Verify they're independent
        assert sheet1.account_id != sheet2.account_id
        assert sheet1.account_balance != sheet2.account_balance
        assert sheet1.ownership != sheet2.ownership
        assert sheet1.return_on_investment != sheet2.return_on_investment

    @pytest.mark.unit
    def test_tracking_sheet_with_matching_values(self):
        """Test MasterTrackingSheet where balance equals current_value."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1000.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={"ytd": "0%"}
        )
        assert sheet.account_balance == sheet.current_value

    @pytest.mark.unit
    def test_tracking_sheet_with_fractional_ownership(self):
        """Test MasterTrackingSheet with fractional ownership."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.5,
            ownership=33.333,
            return_on_investment={}
        )
        assert sheet.shares_owned == 10.5
        assert sheet.ownership == 33.333

    @pytest.mark.unit
    def test_tracking_sheet_with_long_account_id(self):
        """Test MasterTrackingSheet with a long account_id."""
        long_id = "ACC" + "0" * 100
        sheet = MasterTrackingSheet(
            account_id=long_id,
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        assert sheet.account_id == long_id
        assert len(sheet.account_id) == 103

    @pytest.mark.unit
    def test_roi_modification(self):
        """Test modifying return_on_investment dictionary."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=1000.0,
            current_value=1100.0,
            shares_owned=10.0,
            ownership=50.0,
            return_on_investment={}
        )
        # Add entries to the dictionary
        sheet.return_on_investment["ytd"] = "15.5%"
        sheet.return_on_investment["total"] = "45.2%"
        assert sheet.return_on_investment["ytd"] == "15.5%"
        assert len(sheet.return_on_investment) == 2

    @pytest.mark.unit
    def test_all_fields_zero_except_account_id(self):
        """Test MasterTrackingSheet with all numeric fields zero."""
        sheet = MasterTrackingSheet(
            account_id="ACC001",
            account_balance=0.0,
            current_value=0.0,
            shares_owned=0.0,
            ownership=0.0,
            return_on_investment={}
        )
        assert sheet.account_balance == 0.0
        assert sheet.current_value == 0.0
        assert sheet.shares_owned == 0.0
        assert sheet.ownership == 0.0
