"""Unit tests for Transaction model."""

import pytest

from api.domain.models.transactions import Transaction


class TestTransactionInstantiation:
    """Test basic instantiation of Transaction."""

    @pytest.mark.unit
    def test_create_transaction_with_valid_data(self):
        """Test creating a Transaction with valid data."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC123",
            amount=1000.00,
            type="deposit",
            shares=10.0,
            note="Venmo",
        )
        assert transaction.date == "2026-07-11"
        assert transaction.account_id == "ACC123"
        assert transaction.amount == 1000.00
        assert transaction.type == "deposit"
        assert transaction.shares == 10.0
        assert transaction.note == "Venmo"

    @pytest.mark.unit
    def test_create_withdrawal_transaction(self):
        """Test creating a withdrawal transaction."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC456",
            amount=500.00,
            type="withdrawal",
            shares=5.0,
            note="Bank Transfer",
        )
        assert transaction.type == "withdrawal"
        assert transaction.amount == 500.00

    @pytest.mark.unit
    def test_create_transaction_with_zero_values(self):
        """Test creating a Transaction with zero values."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC789",
            amount=0.0,
            type="deposit",
            shares=0.0,
            note="",
        )
        assert transaction.amount == 0.0
        assert transaction.shares == 0.0
        assert transaction.note == ""

    @pytest.mark.unit
    def test_create_transaction_with_negative_values(self):
        """Test creating a Transaction with negative values."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC999",
            amount=-1000.00,
            type="withdrawal",
            shares=-5.0,
            note="Reversal",
        )
        assert transaction.amount == -1000.00
        assert transaction.shares == -5.0

    @pytest.mark.unit
    def test_create_transaction_with_large_amounts(self):
        """Test creating a Transaction with large amounts."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC_LARGE",
            amount=999999999.99,
            type="deposit",
            shares=1000000.0,
            note="Large Deposit",
        )
        assert transaction.amount == 999999999.99
        assert transaction.shares == 1000000.0

    @pytest.mark.unit
    def test_create_transaction_with_decimal_precision(self):
        """Test that Transaction preserves decimal precision."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC_DECIMAL",
            amount=1234.567,
            type="deposit",
            shares=123.456,
            note="Precision Test",
        )
        assert transaction.amount == 1234.567
        assert transaction.shares == 123.456


class TestTransactionDateField:
    """Test date field handling."""

    @pytest.mark.unit
    def test_date_as_iso_format(self):
        """Test date field with ISO format."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.date == "2026-07-11"

    @pytest.mark.unit
    def test_date_as_different_format(self):
        """Test date field with different format."""
        transaction = Transaction(
            date="07/11/2026",
            account_id="ACC002",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.date == "07/11/2026"

    @pytest.mark.unit
    def test_date_as_empty_string(self):
        """Test date field with empty string."""
        transaction = Transaction(
            date="",
            account_id="ACC003",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.date == ""

    @pytest.mark.unit
    def test_date_with_timestamp(self):
        """Test date field with timestamp."""
        transaction = Transaction(
            date="2026-07-11T14:30:00Z",
            account_id="ACC004",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.date == "2026-07-11T14:30:00Z"


class TestTransactionAccountId:
    """Test account_id field handling."""

    @pytest.mark.unit
    def test_account_id_alphanumeric(self):
        """Test account_id with alphanumeric format."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC123",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.account_id == "ACC123"

    @pytest.mark.unit
    def test_account_id_numeric_only(self):
        """Test account_id with numeric format."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="123456789",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.account_id == "123456789"

    @pytest.mark.unit
    def test_account_id_with_special_characters(self):
        """Test account_id with special characters."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC-123-XYZ",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.account_id == "ACC-123-XYZ"

    @pytest.mark.unit
    def test_account_id_empty_string(self):
        """Test account_id with empty string."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction.account_id == ""


class TestTransactionTypeField:
    """Test transaction type field."""

    @pytest.mark.unit
    def test_transaction_type_deposit(self):
        """Test transaction type as deposit."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=500.0,
            type="deposit",
            shares=5.0,
            note="Venmo",
        )
        assert transaction.type == "deposit"

    @pytest.mark.unit
    def test_transaction_type_withdrawal(self):
        """Test transaction type as withdrawal."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=500.0,
            type="withdrawal",
            shares=5.0,
            note="Bank Transfer",
        )
        assert transaction.type == "withdrawal"

    @pytest.mark.unit
    def test_transaction_type_custom(self):
        """Test transaction type with custom value."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=500.0,
            type="transfer",
            shares=5.0,
            note="Internal Transfer",
        )
        assert transaction.type == "transfer"

    @pytest.mark.unit
    def test_transaction_type_case_sensitive(self):
        """Test that transaction type is case-sensitive."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=500.0,
            type="DEPOSIT",
            shares=5.0,
            note="Test",
        )
        assert transaction.type == "DEPOSIT"


class TestTransactionNoteField:
    """Test note field handling."""

    @pytest.mark.unit
    def test_note_as_venmo(self):
        """Test note field with Venmo."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Venmo",
        )
        assert transaction.note == "Venmo"

    @pytest.mark.unit
    def test_note_as_bank_transfer(self):
        """Test note field with Bank Transfer."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Bank Transfer",
        )
        assert transaction.note == "Bank Transfer"

    @pytest.mark.unit
    def test_note_with_descriptive_text(self):
        """Test note field with descriptive text."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Payment for services rendered",
        )
        assert transaction.note == "Payment for services rendered"

    @pytest.mark.unit
    def test_note_as_empty_string(self):
        """Test note field as empty string."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="",
        )
        assert transaction.note == ""

    @pytest.mark.unit
    def test_note_with_special_characters(self):
        """Test note field with special characters."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Payment #123 - Check: ABC-XYZ",
        )
        assert transaction.note == "Payment #123 - Check: ABC-XYZ"

    @pytest.mark.unit
    def test_note_with_unicode_characters(self):
        """Test note field with unicode characters."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="✓ Verified Payment €100",
        )
        assert transaction.note == "✓ Verified Payment €100"


class TestTransactionDataclassProperties:
    """Test dataclass properties and behavior."""

    @pytest.mark.unit
    def test_transaction_has_all_attributes(self):
        """Test that Transaction has all expected attributes."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert hasattr(transaction, "date")
        assert hasattr(transaction, "account_id")
        assert hasattr(transaction, "amount")
        assert hasattr(transaction, "type")
        assert hasattr(transaction, "shares")
        assert hasattr(transaction, "note")

    @pytest.mark.unit
    def test_transaction_equality(self):
        """Test that two Transactions with same data are equal."""
        transaction1 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        transaction2 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction1 == transaction2

    @pytest.mark.unit
    def test_transaction_inequality_different_date(self):
        """Test that two Transactions with different dates are not equal."""
        transaction1 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        transaction2 = Transaction(
            date="2026-07-10",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction1 != transaction2

    @pytest.mark.unit
    def test_transaction_inequality_different_amount(self):
        """Test that two Transactions with different amounts are not equal."""
        transaction1 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        transaction2 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=200.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert transaction1 != transaction2

    @pytest.mark.unit
    def test_transaction_repr(self):
        """Test that Transaction has a meaningful string representation."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        repr_str = repr(transaction)
        assert "Transaction" in repr_str
        assert "2026-07-11" in repr_str
        assert "ACC001" in repr_str

    @pytest.mark.unit
    def test_transaction_is_mutable_by_default(self):
        """Test that Transaction fields can be modified."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        # Modify fields
        transaction.amount = 200.0
        transaction.note = "Modified"
        assert transaction.amount == 200.0
        assert transaction.note == "Modified"


class TestTransactionEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.unit
    def test_transaction_with_very_small_floats(self):
        """Test Transaction with very small float values."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=0.01,
            type="deposit",
            shares=0.001,
            note="Small",
        )
        assert transaction.amount == 0.01
        assert transaction.shares == 0.001

    @pytest.mark.unit
    def test_transaction_with_type_validation(self):
        """Test that Transaction preserves field types."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test",
        )
        assert isinstance(transaction.date, str)
        assert isinstance(transaction.account_id, str)
        assert isinstance(transaction.amount, float)
        assert isinstance(transaction.type, str)
        assert isinstance(transaction.shares, float)
        assert isinstance(transaction.note, str)

    @pytest.mark.unit
    def test_multiple_transactions_independent(self):
        """Test that multiple Transactions are independent."""
        transaction1 = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="Test1",
        )
        transaction2 = Transaction(
            date="2026-07-12",
            account_id="ACC002",
            amount=200.0,
            type="withdrawal",
            shares=2.0,
            note="Test2",
        )
        # Verify they're independent
        assert transaction1.date != transaction2.date
        assert transaction1.account_id != transaction2.account_id
        assert transaction1.amount != transaction2.amount
        assert transaction1.type != transaction2.type

    @pytest.mark.unit
    def test_transaction_with_fractional_shares(self):
        """Test Transaction with fractional shares."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=150.50,
            type="deposit",
            shares=1.5,
            note="Fractional",
        )
        assert transaction.shares == 1.5

    @pytest.mark.unit
    def test_transaction_with_long_note(self):
        """Test Transaction with a long note."""
        long_note = "A" * 1000
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note=long_note,
        )
        assert transaction.note == long_note
        assert len(transaction.note) == 1000

    @pytest.mark.unit
    def test_transaction_with_whitespace_in_strings(self):
        """Test Transaction with whitespace in string fields."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="  ACC  001  ",
            amount=100.0,
            type="deposit",
            shares=1.0,
            note="  Test Note  ",
        )
        assert transaction.account_id == "  ACC  001  "
        assert transaction.note == "  Test Note  "


class TestTransactionAmountAndShares:
    """Test amount and shares financial calculations."""

    @pytest.mark.unit
    def test_transaction_price_per_share(self):
        """Test calculating price per share."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=1000.0,
            type="deposit",
            shares=10.0,
            note="Purchase",
        )
        price_per_share = transaction.amount / transaction.shares
        assert price_per_share == 100.0

    @pytest.mark.unit
    def test_transaction_with_matching_amount_and_shares(self):
        """Test transaction where amount equals shares."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=100.0,
            note="Equal",
        )
        assert transaction.amount == transaction.shares

    @pytest.mark.unit
    def test_transaction_with_zero_shares(self):
        """Test transaction with zero shares."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=100.0,
            type="deposit",
            shares=0.0,
            note="No Shares",
        )
        assert transaction.shares == 0.0

    @pytest.mark.unit
    def test_transaction_with_zero_amount(self):
        """Test transaction with zero amount."""
        transaction = Transaction(
            date="2026-07-11",
            account_id="ACC001",
            amount=0.0,
            type="deposit",
            shares=10.0,
            note="No Amount",
        )
        assert transaction.amount == 0.0
