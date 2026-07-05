"""Ports and Adapters Pattern (Hexagonal Architecture).

The Ports and Adapters pattern isolates core business logic from external
dependencies (databases, APIs, UI, etc.) by defining abstract interfaces (ports)
and concrete implementations (adapters).

Benefits:
  - Testability: swap real dependencies for test doubles
  - Flexibility: change implementations without touching business logic
  - Maintainability: clear boundaries between layers

Three progressively Pythonic approaches are shown:
  1. ABC-based     — classical OOP with explicit contracts
  2. Protocol      — structural subtyping (duck typing)
  3. Dataclass+ABC — combining modern Python features
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Protocol

# ─────────────────────────────────────────────
# EXAMPLE 1: User Repository Pattern
#
# Shows: Core domain → Port → Multiple Adapters
# Use case: Storing/retrieving users from various backends
# ─────────────────────────────────────────────


@dataclass
class User:
    """Domain model — independent of persistence layer."""

    id: str
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)


# PORT: Abstract interface for user storage
class UserRepository(ABC):
    """Port defining the contract for user persistence."""

    @abstractmethod
    def save(self, user: User) -> None:
        """Save a user."""

    @abstractmethod
    def find_by_id(self, user_id: str) -> User | None:
        """Retrieve a user by ID."""

    @abstractmethod
    def find_all(self) -> list[User]:
        """Retrieve all users."""

    @abstractmethod
    def delete(self, user_id: str) -> None:
        """Delete a user by ID."""


# ADAPTER 1: In-memory implementation (useful for testing)
class InMemoryUserRepository(UserRepository):
    """Adapter: stores users in memory (dict)."""

    def __init__(self) -> None:
        self._storage: dict[str, User] = {}

    def save(self, user: User) -> None:
        self._storage[user.id] = user

    def find_by_id(self, user_id: str) -> User | None:
        return self._storage.get(user_id)

    def find_all(self) -> list[User]:
        return list(self._storage.values())

    def delete(self, user_id: str) -> None:
        self._storage.pop(user_id, None)


# ADAPTER 2: File-based implementation
class FileUserRepository(UserRepository):
    """Adapter: persists users to a simple text file."""

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
        self._users: dict[str, User] = {}
        self._load()

    def _load(self) -> None:
        """Load users from file on init."""
        try:
            with open(self._filepath, encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        user = User(
                            id=parts[0],
                            name=parts[1],
                            email=parts[2],
                            created_at=datetime.fromisoformat(parts[3]),
                        )
                        self._users[user.id] = user
        except FileNotFoundError:
            pass

    def _persist(self) -> None:
        """Write all users to file."""
        with open(self._filepath, "w", encoding="utf-8") as f:
            for user in self._users.values():
                f.write(
                    f"{user.id}|{user.name}|{user.email}|"
                    f"{user.created_at.isoformat()}\n"
                )

    def save(self, user: User) -> None:
        self._users[user.id] = user
        self._persist()

    def find_by_id(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def find_all(self) -> list[User]:
        return list(self._users.values())

    def delete(self, user_id: str) -> None:
        self._users.pop(user_id, None)
        self._persist()


# CORE BUSINESS LOGIC: depends only on the port, not adapters
class UserService:
    """Core application logic — depends on port, not concrete adapter."""

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def register_user(self, user_id: str, name: str, email: str) -> User:
        """Business logic: create and save a user."""
        user = User(id=user_id, name=name, email=email)
        self._repository.save(user)
        return user

    def get_user(self, user_id: str) -> User | None:
        """Retrieve a user."""
        return self._repository.find_by_id(user_id)

    def list_all_users(self) -> list[User]:
        """List all users."""
        return self._repository.find_all()

    def remove_user(self, user_id: str) -> None:
        """Remove a user."""
        self._repository.delete(user_id)


# ─────────────────────────────────────────────
# EXAMPLE 2: Notification Service (Protocol-based)
#
# Shows: Protocol for duck typing without inheritance
# Use case: Send notifications via different channels
# ─────────────────────────────────────────────


@dataclass
class Notification:
    """Domain model for a notification."""

    recipient: str
    subject: str
    message: str


# PORT: Protocol instead of ABC
class NotificationPort(Protocol):
    """Port: any class with a send() method qualifies."""

    def send(self, notification: Notification) -> bool:
        """Send a notification. Return True on success."""


# ADAPTER 1: Email notification
class EmailNotificationAdapter:
    """Adapter: sends notifications via email (simulated)."""

    def send(self, notification: Notification) -> bool:
        print(f"[EMAIL] To: {notification.recipient}")
        print(f"[EMAIL] Subject: {notification.subject}")
        print(f"[EMAIL] Message: {notification.message}")
        return True


# ADAPTER 2: SMS notification
class SmsNotificationAdapter:
    """Adapter: sends notifications via SMS (simulated)."""

    def send(self, notification: Notification) -> bool:
        print(f"[SMS] To: {notification.recipient}")
        print(f"[SMS] {notification.message}")
        return True


# ADAPTER 3: Console notification (for testing/debugging)
class ConsoleNotificationAdapter:
    """Adapter: prints notification to console."""

    def send(self, notification: Notification) -> bool:
        print(f"[CONSOLE] {notification.subject}: {notification.message}")
        print(f"[CONSOLE] (recipient: {notification.recipient})")
        return True


# CORE BUSINESS LOGIC
class NotificationService:
    """Core logic: sends notifications via any adapter."""

    def __init__(self, adapter: NotificationPort) -> None:
        self._adapter = adapter

    def notify(self, recipient: str, subject: str, message: str) -> bool:
        """Send notification using the configured adapter."""
        notification = Notification(recipient, subject, message)
        return self._adapter.send(notification)


# ─────────────────────────────────────────────
# EXAMPLE 3: Payment Gateway (Multiple Adapters)
#
# Shows: Swappable payment processors
# Use case: Process payments through different gateways
# ─────────────────────────────────────────────


@dataclass
class PaymentRequest:
    """Domain model for payment."""

    amount: float
    currency: str
    customer_id: str


@dataclass
class PaymentResult:
    """Domain model for payment result."""

    success: bool
    transaction_id: str | None
    message: str


# PORT
class PaymentGateway(ABC):
    """Port for payment processing."""

    @abstractmethod
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """Process a payment and return result."""


# ADAPTER 1: Stripe
class StripePaymentAdapter(PaymentGateway):
    """Adapter: Stripe payment gateway (simulated)."""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[STRIPE] Processing ${request.amount} {request.currency}")
        return PaymentResult(
            success=True,
            transaction_id="stripe_txn_12345",
            message="Payment processed via Stripe",
        )


# ADAPTER 2: PayPal
class PayPalPaymentAdapter(PaymentGateway):
    """Adapter: PayPal payment gateway (simulated)."""

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[PAYPAL] Processing ${request.amount} {request.currency}")
        return PaymentResult(
            success=True,
            transaction_id="paypal_txn_67890",
            message="Payment processed via PayPal",
        )


# ADAPTER 3: Mock (for testing)
class MockPaymentAdapter(PaymentGateway):
    """Adapter: Mock payment gateway for testing."""

    def __init__(self, should_succeed: bool = True) -> None:
        self._should_succeed = should_succeed

    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        print(f"[MOCK] Processing ${request.amount} {request.currency}")
        if self._should_succeed:
            return PaymentResult(
                success=True,
                transaction_id="mock_txn_test",
                message="Mock payment successful",
            )
        return PaymentResult(
            success=False,
            transaction_id=None,
            message="Mock payment failed",
        )


# CORE BUSINESS LOGIC
class PaymentService:
    """Core logic: process payments via any gateway."""

    def __init__(self, gateway: PaymentGateway) -> None:
        self._gateway = gateway

    def charge_customer(
        self, customer_id: str, amount: float, currency: str = "USD"
    ) -> PaymentResult:
        """Charge a customer using the configured gateway."""
        request = PaymentRequest(amount, currency, customer_id)
        return self._gateway.process_payment(request)


# ─────────────────────────────────────────────
# EXAMPLE 4: Logger Port (Callable approach)
#
# Shows: Simple port using type alias
# Use case: Log to different destinations
# ─────────────────────────────────────────────

from collections.abc import Callable

LoggerPort = Callable[[str], None]


def console_logger(message: str) -> None:
    """Adapter: log to console."""
    print(f"[CONSOLE LOG] {message}")


def file_logger(filepath: str) -> LoggerPort:
    """Adapter factory: log to file."""

    def log(message: str) -> None:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat()}] {message}\n")

    return log


def null_logger(message: str) -> None:
    """Adapter: silent logger (for production where logging is disabled)."""


class Application:
    """Application using logger port."""

    def __init__(self, logger: LoggerPort = console_logger) -> None:
        self._logger = logger

    def run(self) -> None:
        self._logger("Application started")
        self._logger("Performing some operation...")
        self._logger("Application finished")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    print("=" * 70)
    print("EXAMPLE 1: User Repository Pattern")
    print("=" * 70)

    # Use in-memory adapter
    repo = InMemoryUserRepository()
    service = UserService(repo)

    alice = service.register_user("1", "Alice", "alice@example.com")
    bob = service.register_user("2", "Bob", "bob@example.com")

    print(f"\nRegistered: {alice.name} ({alice.email})")
    print(f"Registered: {bob.name} ({bob.email})")

    print("\nAll users:")
    for user in service.list_all_users():
        print(f"  - {user.name} ({user.email})")

    # Swap to file adapter (same service, different storage)
    print("\n--- Switching to File-based Repository ---")
    file_repo = FileUserRepository("/tmp/users.txt")
    file_service = UserService(file_repo)
    file_service.register_user("3", "Charlie", "charlie@example.com")

    print("\nUsers in file repository:")
    for user in file_service.list_all_users():
        print(f"  - {user.name} ({user.email})")

    print("\n" + "=" * 70)
    print("EXAMPLE 2: Notification Service (Protocol-based)")
    print("=" * 70)

    # Email adapter
    email_service = NotificationService(EmailNotificationAdapter())
    email_service.notify(
        "user@example.com",
        "Welcome!",
        "Thank you for signing up.",
    )

    print()

    # SMS adapter
    sms_service = NotificationService(SmsNotificationAdapter())
    sms_service.notify("+1234567890", "Alert", "Your order has shipped!")

    print()

    # Console adapter
    console_service = NotificationService(ConsoleNotificationAdapter())
    console_service.notify("admin", "System Status", "All systems operational")

    print("\n" + "=" * 70)
    print("EXAMPLE 3: Payment Gateway")
    print("=" * 70)

    # Stripe adapter
    stripe_service = PaymentService(StripePaymentAdapter())
    result = stripe_service.charge_customer("cust_001", 99.99)
    print(f"Result: {result.message} (txn: {result.transaction_id})\n")

    # PayPal adapter
    paypal_service = PaymentService(PayPalPaymentAdapter())
    result = paypal_service.charge_customer("cust_002", 149.99)
    print(f"Result: {result.message} (txn: {result.transaction_id})\n")

    # Mock adapter (for testing)
    mock_service = PaymentService(MockPaymentAdapter(should_succeed=True))
    result = mock_service.charge_customer("cust_test", 1.00)
    print(f"Result: {result.message} (txn: {result.transaction_id})")

    print("\n" + "=" * 70)
    print("EXAMPLE 4: Logger Port (Callable approach)")
    print("=" * 70)

    # Console logger
    app1 = Application(console_logger)
    app1.run()

    print("\n--- Using File Logger ---")
    # File logger
    app2 = Application(file_logger("/tmp/app.log"))
    app2.run()
    print("(logs written to /tmp/app.log)")

    print("\n--- Using Null Logger ---")
    # Null logger
    app3 = Application(null_logger)
    app3.run()
    print("(no logs produced)")


if __name__ == "__main__":
    main()
