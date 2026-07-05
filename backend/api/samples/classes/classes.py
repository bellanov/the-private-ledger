"""Classes.

Overview of Classes / Object-Oriented Programming (OOP) and their usage.

Like many languages, Python allows you to define Classes that encapsulate data and
the functions that operate on them. They can be used sometimes to make code
cleaner and simpler.
"""


class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count: int = 0) -> None:
        """Initialize the clicker with an optional starting count."""
        self.count = count

    def click(self, num_times: int = 1) -> None:
        """Increment the click count by a specified number of times."""
        self.count += num_times

    def read(self) -> int:
        """Return the current click count."""
        return self.count

    def reset(self) -> None:
        """Reset the click count to zero."""
        self.count = 0


# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass


def main() -> None:
    clicker = CountingClicker()
    clicker.click()
    clicker.click(2)
    print(clicker.read())  # Output: 3
    assert clicker.read() == 3, "after three clicks, clicker should have count 3"
    clicker.reset()
    print(clicker.read())  # Output: 0
    assert clicker.read() == 0, "after reset, clicker should be back to 0"

    clicker2 = NoResetClicker()
    print(clicker2.read())  # Output: 0
    assert clicker2.read() == 0
    clicker2.click()
    print(clicker2.read())  # Output: 1
    assert clicker2.read() == 1
    clicker2.reset()
    print(clicker2.read())  # Output: 1
    assert clicker2.read() == 1, "reset shouldn't do anything"


if __name__ == "__main__":
    main()
