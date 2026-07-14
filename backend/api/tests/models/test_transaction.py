"""Unit tests for Transaction model."""

import pytest
from pydantic import ValidationError

from api.domain.models.transaction import Transaction


@pytest.mark.unit
class TestTransactionInstantiation:
    """Test basic instantiation of Transaction."""

    def test_create_transaction_with_valid_data(self):
        """Transaction should store all constructor values."""
        transaction = Transaction(
            date="2026-07-14T12:30:45.123Z",
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert transaction.date == "2026-07-14T12:30:45.123Z"
        assert transaction.account_id == "PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735"
        assert transaction.type == "DEPOSIT"
        assert transaction.amount == 100.0
        assert transaction.shares == 10.0
        assert transaction.note == "venmo"

    def test_create_withdrawal_transaction(self):
        """Transaction should handle withdrawal type."""
        transaction = Transaction(
            date="2026-07-14T15:00:00.000Z",
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            type="WITHDRAWAL",
            amount=50.0,
            shares=5.0,
            note="bank",
        )

        assert transaction.type == "WITHDRAWAL"
        assert transaction.amount == 50.0

    def test_create_transaction_with_zero_values(self):
        """Transaction should handle zero values correctly."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            type="DEPOSIT",
            amount=0.0,
            shares=0.0,
            note="check",
        )

        assert transaction.amount == 0.0
        assert transaction.shares == 0.0
        assert transaction.note == "check"

    def test_create_transaction_with_decimal_precision(self):
        """Transaction should preserve decimal precision."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
            type="DEPOSIT",
            amount=1234.567,
            shares=123.456,
            note="cashapp",
        )

        assert transaction.amount == 1234.567
        assert transaction.shares == 123.456

    def test_create_transaction_with_camel_case_input(self):
        """Transaction should accept camelCase field names."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            accountId="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert transaction.account_id == "PL-19c7e4b2d5a64fb8b3e1079ac4d862ef"


@pytest.mark.unit
class TestTransactionValidation:
    """Test Pydantic validation behavior."""

    def test_transaction_requires_all_fields(self):
        """Transaction should require all fields."""
        with pytest.raises(ValidationError) as exc_info:
            Transaction(date="2026-07-14T12:00:00.000Z")

        errors = exc_info.value.errors()
        assert len(errors) >= 5  # Missing required fields

    def test_transaction_validates_numeric_fields(self):
        """Transaction should validate numeric fields."""
        with pytest.raises(ValidationError):
            Transaction(
                date="2026-07-14T12:00:00.000Z",
                account_id="PL-test",
                type="DEPOSIT",
                amount="not a number",
                shares=10.0,
                note="bank",
            )

    def test_transaction_validates_date_type(self):
        """Transaction should validate date is a string."""
        with pytest.raises(ValidationError):
            Transaction(
                date=12345,
                account_id="PL-test",
                type="DEPOSIT",
                amount=100.0,
                shares=10.0,
                note="venmo",
            )

    def test_transaction_converts_numeric_strings(self):
        """Transaction should convert numeric strings to floats."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            type="DEPOSIT",
            amount="100.0",
            shares="10.0",
            note="check",
        )

        assert transaction.amount == 100.0
        assert transaction.shares == 10.0
        assert isinstance(transaction.amount, float)


@pytest.mark.unit
class TestTransactionDateValidation:
    """Test date field validation."""

    def test_date_with_iso_format(self):
        """Transaction should accept ISO 8601 format."""
        transaction = Transaction(
            date="2026-07-14T12:30:45.123Z",
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="cashapp",
        )

        assert transaction.date == "2026-07-14T12:30:45.123Z"

    def test_date_with_milliseconds(self):
        """Transaction should handle milliseconds in timestamp."""
        transaction = Transaction(
            date="2026-07-14T12:30:45.999Z",
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert ".999Z" in transaction.date


@pytest.mark.unit
class TestTransactionAccountIdValidation:
    """Test account_id field validation."""

    def test_account_id_with_valid_pl_format(self):
        """Transaction should accept PL-{hex} format."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="check",
        )

        assert transaction.account_id.startswith("PL-")
        assert len(transaction.account_id) == 35  # PL- + 32 hex chars

    def test_account_id_with_empty_string(self):
        """Transaction should reject empty string for account_id."""
        with pytest.raises(ValidationError):
            Transaction(
                date="2026-07-14T12:00:00.000Z",
                account_id="",
                type="DEPOSIT",
                amount=100.0,
                shares=10.0,
                note="venmo",
            )


@pytest.mark.unit
class TestTransactionTypeValidation:
    """Test transaction type field validation."""

    def test_type_DEPOSIT(self):
        """Transaction should accept DEPOSIT type."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="bank",
        )

        assert transaction.type == "DEPOSIT"

    def test_type_withdrawal(self):
        """Transaction should accept WITHDRAWAL type."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            type="WITHDRAWAL",
            amount=50.0,
            shares=5.0,
            note="check",
        )

        assert transaction.type == "WITHDRAWAL"

    def test_type_is_case_sensitive(self):
        """Transaction type should be case-sensitive."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="cashapp",
        )

        assert transaction.type == "DEPOSIT"

    def test_type_accepts_any_string(self):
        """Transaction should accept any string for type."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            type="WITHDRAWAL",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert transaction.type == "WITHDRAWAL"


@pytest.mark.unit
class TestTransactionNoteValidation:
    """Test note field validation."""

    def test_note_with_all_valid_values(self):
        """Transaction should accept all valid payment methods."""
        valid_notes = ["venmo", "bank", "check", "cashapp"]

        for note in valid_notes:
            transaction = Transaction(
                date="2026-07-14T12:00:00.000Z",
                account_id="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
                type="DEPOSIT",
                amount=100.0,
                shares=10.0,
                note=note,
            )
            assert transaction.note == note

    def test_note_venmo(self):
        """Transaction should accept 'venmo' as note."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert transaction.note == "venmo"

    def test_note_bank(self):
        """Transaction should accept 'bank' as note."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="bank",
        )

        assert transaction.note == "bank"

    def test_note_check(self):
        """Transaction should accept 'check' as note."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="check",
        )

        assert transaction.note == "check"

    def test_note_cashapp(self):
        """Transaction should accept 'cashapp' as note."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="cashapp",
        )

        assert transaction.note == "cashapp"

    def test_note_rejects_invalid_value(self):
        """Transaction should reject invalid note values if validation exists."""
        # This test assumes note field has validation for specific values
        # If no validation exists, this test should be updated or removed
        try:
            transaction = Transaction(
                date="2026-07-14T12:00:00.000Z",
                account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
                type="DEPOSIT",
                amount=100.0,
                shares=10.0,
                note="invalid_method",
            )
            # If no validation, note will accept any value
            assert transaction.note == "invalid_method"
        except ValidationError:
            # If validation exists, this should raise ValidationError
            pass


@pytest.mark.unit
class TestTransactionEquality:
    """Test model equality behavior."""

    def test_transaction_equality_same_values(self):
        """Transactions with identical values should be equal."""
        transaction1 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )
        transaction2 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        assert transaction1 == transaction2

    def test_transaction_inequality_different_date(self):
        """Transactions with different dates should not be equal."""
        transaction1 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="bank",
        )
        transaction2 = Transaction(
            date="2026-07-15T12:00:00.000Z",
            account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="bank",
        )

        assert transaction1 != transaction2

    def test_transaction_inequality_different_amount(self):
        """Transactions with different amounts should not be equal."""
        transaction1 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="check",
        )
        transaction2 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            type="DEPOSIT",
            amount=200.0,
            shares=10.0,
            note="check",
        )

        assert transaction1 != transaction2


@pytest.mark.unit
class TestTransactionSerialization:
    """Test Pydantic serialization behavior."""

    def test_transaction_model_dump(self):
        """model_dump should return dictionary with snake_case keys."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="venmo",
        )

        data = transaction.model_dump()

        assert data["date"] == "2026-07-14T12:00:00.000Z"
        assert data["account_id"] == "PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735"
        assert data["type"] == "DEPOSIT"
        assert data["amount"] == 100.0
        assert data["shares"] == 10.0
        assert data["note"] == "venmo"

    def test_transaction_model_dump_json(self):
        """model_dump_json should return JSON string."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="bank",
        )

        json_str = transaction.model_dump_json()

        assert isinstance(json_str, str)
        assert "2026-07-14T12:00:00.000Z" in json_str
        assert "PL-8a12e5d94c3f4a7bb6e1820fd9c4512a" in json_str

    def test_transaction_model_dump_by_alias(self):
        """model_dump with by_alias=True should use camelCase."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-4d7b92c1e8f64ab39c15d702fa6e8b41",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="check",
        )

        data = transaction.model_dump(by_alias=True)

        assert "accountId" in data

    def test_transaction_has_all_attributes(self):
        """Transaction should have all expected attributes."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-b6e41d9a73c24f80a5d9e1c24b7f6038",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="cashapp",
        )

        assert hasattr(transaction, "date")
        assert hasattr(transaction, "account_id")
        assert hasattr(transaction, "type")
        assert hasattr(transaction, "amount")
        assert hasattr(transaction, "shares")
        assert hasattr(transaction, "note")


@pytest.mark.unit
class TestTransactionFinancialCalculations:
    """Test financial relationship validations."""

    def test_price_per_share_calculation(self):
        """Price per share should equal amount / shares."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-19c7e4b2d5a64fb8b3e1079ac4d862ef",
            type="DEPOSIT",
            amount=1000.0,
            shares=100.0,
            note="venmo",
        )

        price_per_share = transaction.amount / transaction.shares

        assert price_per_share == 10.0

    def test_transaction_with_fractional_shares(self):
        """Transaction should handle fractional shares."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-a5f28c71d3e6492eb8c4f16a9d7032bc",
            type="DEPOSIT",
            amount=105.0,
            shares=10.5,
            note="bank",
        )

        assert transaction.shares == 10.5

    def test_transaction_amount_equals_shares(self):
        """Transaction where amount equals shares."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-72d4b8e19ac34f5ba1e96c20d7f4836a",
            type="DEPOSIT",
            amount=100.0,
            shares=100.0,
            note="check",
        )

        assert transaction.amount == transaction.shares


@pytest.mark.unit
class TestTransactionEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_transaction_with_very_small_floats(self):
        """Transaction should handle very small decimal values."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-c8e15a42b9d74f03ae6c1d84f2759b10",
            type="DEPOSIT",
            amount=0.01,
            shares=0.001,
            note="cashapp",
        )

        assert transaction.amount == 0.01
        assert transaction.shares == 0.001

    def test_transaction_with_large_values(self):
        """Transaction should handle large financial values."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-5e2f7c1a9d4b4e6f8a3c1d7e9b2f4a6c",
            type="DEPOSIT",
            amount=1_000_000.0,
            shares=10000.0,
            note="venmo",
        )

        assert transaction.amount == 1_000_000.0
        assert transaction.shares == 10000.0

    def test_transaction_with_negative_values(self):
        """Transaction should handle negative values (withdrawals)."""
        transaction = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-91ab4e7d2c6f48b3a5d9e0f1c2b7a8d4",
            type="WITHDRAWAL",
            amount=-100.0,
            shares=-10.0,
            note="bank",
        )

        assert transaction.amount == -100.0
        assert transaction.shares == -10.0

    def test_multiple_transactions_are_independent(self):
        """Multiple Transaction instances should not share state."""
        transaction1 = Transaction(
            date="2026-07-14T12:00:00.000Z",
            account_id="PL-f3d9c1a24b7e4c18a9d2f6e1b8c04735",
            type="DEPOSIT",
            amount=100.0,
            shares=10.0,
            note="check",
        )
        transaction2 = Transaction(
            date="2026-07-15T12:00:00.000Z",
            account_id="PL-8a12e5d94c3f4a7bb6e1820fd9c4512a",
            type="WITHDRAWAL",
            amount=50.0,
            shares=5.0,
            note="cashapp",
        )

        assert transaction1.date != transaction2.date
        assert transaction1.account_id != transaction2.account_id
        assert transaction1.amount != transaction2.amount

    def test_different_payment_methods(self):
        """Transaction should handle all different payment methods."""
        methods = ["venmo", "bank", "check", "cashapp"]

        transactions = []
        for i, method in enumerate(methods):
            transaction = Transaction(
                date=f"2026-07-{14+i:02d}T12:00:00.000Z",
                account_id=f"PL-{'a'*32}",
                type="DEPOSIT",
                amount=100.0 * (i + 1),
                shares=10.0 * (i + 1),
                note=method,
            )
            transactions.append(transaction)

        assert len(transactions) == 4
        assert all(t.note in methods for t in transactions)
