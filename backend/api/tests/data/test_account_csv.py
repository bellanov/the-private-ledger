"""Unit tests for Account.csv data integrity."""

import csv
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "api" / "domain" / "data"
ACCOUNT_CSV = DATA_DIR / "Account.csv"


def load_csv(filepath):
    """Load CSV file and return list of dictionaries."""
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.mark.unit
class TestAccountCSVIntegrity:
    """Test Account.csv data integrity."""

    @pytest.fixture
    def accounts(self):
        """Load accounts data."""
        return load_csv(ACCOUNT_CSV)

    def test_account_csv_exists(self):
        """Account.csv file should exist."""
        assert ACCOUNT_CSV.exists(), f"Missing {ACCOUNT_CSV}"

    def test_account_csv_has_correct_headers(self, accounts):
        """Account.csv should have all required headers."""
        expected_headers = {
            "account_id",
            "account_balance",
            "total_shares",
            "ledger_id",
            "ownership",
            "current_value",
            "return_on_investment",
        }
        actual_headers = set(accounts[0].keys())
        assert expected_headers == actual_headers

    def test_account_csv_has_10_rows(self, accounts):
        """Account.csv should have exactly 10 data rows."""
        assert len(accounts) == 10

    def test_all_account_ids_are_unique(self, accounts):
        """All account_id values should be unique."""
        account_ids = [a["account_id"] for a in accounts]
        assert len(account_ids) == len(set(account_ids))

    def test_all_account_ids_follow_pattern(self, accounts):
        """All account_id values should match PL-{hex} pattern."""
        for account in accounts:
            account_id = account["account_id"]
            assert account_id.startswith("PL-"), f"Invalid ID format: {account_id}"
            hex_part = account_id[3:]
            assert len(hex_part) == 32, f"Invalid hex length: {account_id}"
            assert all(
                c in "0123456789abcdef" for c in hex_part
            ), f"Invalid hex chars: {account_id}"

    def test_all_balances_are_numeric(self, accounts):
        """All account_balance values should be numeric."""
        for account in accounts:
            try:
                float(account["account_balance"])
            except ValueError:
                pytest.fail(f"Non-numeric balance: {account['account_balance']}")

    def test_all_shares_are_numeric(self, accounts):
        """All total_shares values should be numeric."""
        for account in accounts:
            try:
                float(account["total_shares"])
            except ValueError:
                pytest.fail(f"Non-numeric shares: {account['total_shares']}")

    def test_all_ownership_are_numeric(self, accounts):
        """All ownership values should be numeric."""
        for account in accounts:
            try:
                float(account["ownership"])
            except ValueError:
                pytest.fail(f"Non-numeric ownership: {account['ownership']}")

    def test_all_current_values_are_numeric(self, accounts):
        """All current_value values should be numeric."""
        for account in accounts:
            try:
                float(account["current_value"])
            except ValueError:
                pytest.fail(f"Non-numeric current_value: {account['current_value']}")

    def test_all_roi_are_numeric(self, accounts):
        """All return_on_investment values should be numeric."""
        for account in accounts:
            try:
                float(account["return_on_investment"])
            except ValueError:
                pytest.fail(f"Non-numeric ROI: {account['return_on_investment']}")

    def test_total_shares_equals_100(self, accounts):
        """Total total_shares across all accounts should equal 100."""
        total_shares = sum(float(a["total_shares"]) for a in accounts)
        assert total_shares == 100.0

    def test_each_account_has_10_shares(self, accounts):
        """Each account should have exactly 10 shares."""
        for account in accounts:
            assert float(account["total_shares"]) == 10.0

    def test_ownership_percentage_is_10_percent_each(self, accounts):
        """Each account's ownership should be exactly 10%."""
        for account in accounts:
            assert float(account["ownership"]) == 10.0

    def test_account_balance_equals_current_value(self, accounts):
        """Account balance should equal current value (break-even scenario)."""
        for account in accounts:
            balance = float(account["account_balance"])
            current = float(account["current_value"])
            assert balance == current, f"Mismatch for {account['account_id']}"

    def test_roi_is_zero_for_breakeven(self, accounts):
        """ROI should be 0.00 when balance equals current value."""
        for account in accounts:
            roi = float(account["return_on_investment"])
            assert roi == 0.0
