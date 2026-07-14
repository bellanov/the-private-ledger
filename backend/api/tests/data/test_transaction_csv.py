"""Unit tests for Transaction.csv data integrity."""

import csv
import re
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "api" / "domain" / "data"
TRANSACTION_CSV = DATA_DIR / "Transaction.csv"


def load_csv(filepath):
    """Load CSV file and return list of dictionaries."""
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.mark.unit
class TestTransactionCSVIntegrity:
    """Test Transaction.csv data integrity."""

    @pytest.fixture
    def transactions(self):
        """Load transactions data."""
        return load_csv(TRANSACTION_CSV)

    def test_transaction_csv_exists(self):
        """Transaction.csv file should exist."""
        assert TRANSACTION_CSV.exists(), f"Missing {TRANSACTION_CSV}"

    def test_transaction_csv_has_correct_headers(self, transactions):
        """Transaction.csv should have all required headers."""
        expected_headers = {
            "date",
            "account_id",
            "type",
            "amount",
            "shares",
            "note",
        }
        actual_headers = set(transactions[0].keys())
        assert expected_headers == actual_headers

    def test_transaction_csv_has_10_rows(self, transactions):
        """Transaction.csv should have exactly 10 data rows."""
        assert len(transactions) == 10

    def test_all_dates_are_iso_format(self, transactions):
        """All dates should be in ISO 8601 format."""
        iso_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$"
        for transaction in transactions:
            date = transaction["date"]
            assert re.match(iso_pattern, date), f"Invalid date format: {date}"

    def test_all_amounts_are_numeric(self, transactions):
        """All amount values should be numeric."""
        for transaction in transactions:
            try:
                float(transaction["amount"])
            except ValueError:
                pytest.fail(f"Non-numeric amount: {transaction['amount']}")

    def test_all_shares_are_numeric(self, transactions):
        """All shares values should be numeric."""
        for transaction in transactions:
            try:
                float(transaction["shares"])
            except ValueError:
                pytest.fail(f"Non-numeric shares: {transaction['shares']}")

    def test_all_types_are_deposit(self, transactions):
        """All transaction types should be DEPOSIT."""
        for transaction in transactions:
            assert transaction["type"] == "DEPOSIT"

    def test_total_shares_equals_100(self, transactions):
        """Total shares across all transactions should equal 100."""
        total_shares = sum(float(t["shares"]) for t in transactions)
        assert total_shares == 100.0

    def test_each_transaction_has_10_shares(self, transactions):
        """Each transaction should have exactly 10 shares."""
        for transaction in transactions:
            assert float(transaction["shares"]) == 10.0

    def test_total_amount_equals_1000(self, transactions):
        """Total amount across all transactions should equal 1000."""
        total_amount = sum(float(t["amount"]) for t in transactions)
        assert total_amount == 1000.0

    def test_each_transaction_has_100_amount(self, transactions):
        """Each transaction should have exactly 100 amount."""
        for transaction in transactions:
            assert float(transaction["amount"]) == 100.0
