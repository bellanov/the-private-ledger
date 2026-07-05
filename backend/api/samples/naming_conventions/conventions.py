"""Naming Conventions.

Overview of Python naming conventions, including variable names, function names,
class names, and more.
"""

MAX_CONNECTIONS = 10  # constant


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._transaction_log = []  # "protected" - internal use
        self.__balance = balance  # "private" - name-mangled

    def deposit(self, amount):  # public method
        self.__balance += amount
        self._log("deposit", amount)

    def _log(self, action, amount):  # "protected" helper
        self._transaction_log.append((action, amount))

    def __validate(self, amount):  # "private" helper
        return amount > 0

    @property
    def balance(self):  # public access to private data
        return self.__balance


account = BankAccount("Alice", 100)
print(account.owner)  # ✅ works
print(account._transaction_log)  # ⚠️ works, but frowned upon
print(account._BankAccount__balance)  # ✅ name mangling workaround (don't do this)
print(account.__balance)  # ❌ AttributeError
