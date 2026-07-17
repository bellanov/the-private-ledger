"""Unit tests for Performance.csv data integrity."""

import csv
import re
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "api" / "domain" / "data"
PERFORMANCE_CSV = DATA_DIR / "Performance.csv"
TRANSACTION_CSV = DATA_DIR / "Transaction.csv"


def load_csv(filepath):
    """Load CSV file and return list of dictionaries."""
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.mark.unit
class TestPerformanceCSVIntegrity:
    """Test Performance.csv data integrity."""

    @pytest.fixture
    def performance(self):
        """Load performance data."""
        return load_csv(PERFORMANCE_CSV)

    def test_performance_csv_exists(self):
        """Performance.csv file should exist."""
        assert PERFORMANCE_CSV.exists(), f"Missing {PERFORMANCE_CSV}"

    def test_performance_csv_has_correct_headers(self, performance):
        """Performance.csv should have all required headers."""
        expected_headers = {
            "date",
            "total_bankroll",
            "units_won",
            "share_price",
            "record",
            "return_on_investment",
            "unit_price",
            "shares",
        }
        actual_headers = set(performance[0].keys())
        assert expected_headers == actual_headers

    def test_performance_csv_has_at_least_one_row(self, performance):
        """Performance.csv should have at least one data row."""
        assert len(performance) >= 1

    def test_performance_date_is_iso_format(self, performance):
        """Performance date should be in ISO 8601 format."""
        iso_pattern = r"^\d{4}-\d{2}-\d{2}$"
        for perf in performance:
            date = perf["date"]
            assert re.match(iso_pattern, date), f"Invalid date format: {date}"

    def test_total_bankroll_is_numeric(self, performance):
        """Total bankroll should be numeric."""
        for perf in performance:
            try:
                float(perf["total_bankroll"])
            except ValueError:
                pytest.fail(f"Non-numeric total_bankroll: {perf['total_bankroll']}")

    def test_units_won_is_numeric(self, performance):
        """Units won should be numeric."""
        for perf in performance:
            try:
                float(perf["units_won"])
            except ValueError:
                pytest.fail(f"Non-numeric units_won: {perf['units_won']}")

    def test_share_price_is_numeric(self, performance):
        """Share price should be numeric."""
        for perf in performance:
            try:
                float(perf["share_price"])
            except ValueError:
                pytest.fail(f"Non-numeric share_price: {perf['share_price']}")

    def test_roi_is_numeric(self, performance):
        """Return on investment should be numeric."""
        for perf in performance:
            try:
                float(perf["return_on_investment"])
            except ValueError:
                pytest.fail(
                    f"Non-numeric return_on_investment: {perf['return_on_investment']}"
                )

    def test_unit_price_is_numeric(self, performance):
        """Unit price should be numeric."""
        for perf in performance:
            try:
                float(perf["unit_price"])
            except ValueError:
                pytest.fail(f"Non-numeric unit_price: {perf['unit_price']}")

    def test_shares_is_numeric(self, performance):
        """Shares should be numeric."""
        for perf in performance:
            try:
                float(perf["shares"])
            except ValueError:
                pytest.fail(f"Non-numeric shares: {perf['shares']}")


@pytest.mark.unit
class TestCrossCSVRelationships:
    """Test relationships between all CSVs."""

    @pytest.fixture
    def accounts(self):
        """Load accounts data."""
        account_csv = DATA_DIR / "Account.csv"
        return load_csv(account_csv)

    @pytest.fixture
    def transactions(self):
        """Load transactions data."""
        return load_csv(TRANSACTION_CSV)

    @pytest.fixture
    def performance(self):
        """Load performance data."""
        return load_csv(PERFORMANCE_CSV)

    def test_performance_total_bankroll_matches_account_sum(
        self, accounts, performance
    ):
        """Performance total_bankroll should equal sum of account current_values."""
        account_sum = sum(float(a["current_value"]) for a in accounts)
        perf_bankroll = float(performance[0]["total_bankroll"])
        assert perf_bankroll == account_sum

    def test_performance_shares_matches_account_sum(self, accounts, performance):
        """Performance shares should equal sum of account total_shares."""
        account_shares = sum(float(a["total_shares"]) for a in accounts)
        perf_shares = float(performance[0]["shares"])
        assert perf_shares == account_shares

    def test_performance_share_price_calculation(self, accounts, performance):
        """Performance share_price should equal total_bankroll / shares."""
        account_sum = sum(float(a["current_value"]) for a in accounts)
        account_shares = sum(float(a["total_shares"]) for a in accounts)
        expected_price = account_sum / account_shares
        actual_price = float(performance[0]["share_price"])
        assert actual_price == expected_price

    def test_transaction_total_shares_matches_account_sum(self, accounts, transactions):
        """Transaction total shares should equal account total shares."""
        account_shares = sum(float(a["total_shares"]) for a in accounts)
        transaction_shares = sum(float(t["shares"]) for t in transactions)
        assert transaction_shares == account_shares

    def test_transaction_total_amount_matches_account_sum(self, accounts, transactions):
        """Transaction total amount should equal account total balance."""
        account_balance = sum(float(a["account_balance"]) for a in accounts)
        transaction_amount = sum(float(t["amount"]) for t in transactions)
        assert transaction_amount == account_balance

    def test_transaction_account_ids_match_accounts(self, accounts, transactions):
        """All transaction account_ids should exist in accounts."""
        account_ids = {a["account_id"] for a in accounts}
        transaction_account_ids = {t["account_id"] for t in transactions}
        assert transaction_account_ids.issubset(account_ids)

    def test_each_account_has_exactly_one_transaction(self, accounts, transactions):
        """Each account should have exactly one corresponding transaction."""
        transaction_accounts = [t["account_id"] for t in transactions]
        assert len(transaction_accounts) == len(set(transaction_accounts))
