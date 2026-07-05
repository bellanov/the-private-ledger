"""Truthiness.

Overview of *Truthiness* in Python.

Truthiness refers to how Python evaluates the truth value of objects in boolean
contexts, beyond just True and False.
"""


def demo_boolean_basics() -> tuple[bool, bool]:
    """Demonstrate basic boolean comparisons."""
    one_is_less_than_two = 1 < 2  # equals True
    true_equals_false = True == False  # equals False
    return one_is_less_than_two, true_equals_false


def demo_none_checking(x) -> tuple[bool, bool]:
    """Demonstrate correct way to check for None."""
    # Use 'is' to check for None, not '=='
    is_check = x is None
    return is_check, is_check


def demo_falsy_values() -> dict:
    """Demonstrate which values are falsy in Python."""
    falsy_values = {
        "False": False,
        "None": None,
        "empty list": [],
        "empty dict": {},
        "empty string": "",
        "empty set": set(),
        "zero int": 0,
        "zero float": 0.0,
    }

    # Check which are falsy
    truthiness = {name: bool(value) for name, value in falsy_values.items()}
    return truthiness


def demo_truthy_values() -> tuple[bool, bool, bool, bool]:
    """Demonstrate what values are truthy."""
    return bool([1]), bool({"a": 1}), bool("hello"), bool(1)


def demo_short_circuit_with_and(s: str) -> str:
    """Demonstrate short-circuit evaluation with 'and'."""
    # This gets the first char if s is truthy, otherwise returns empty string
    first_char = s and s[0]
    return first_char


def demo_default_value_with_or(x) -> int:
    """Demonstrate using 'or' to provide default values."""
    # If x is None or falsy, use 0 instead
    safe_x = x or 0
    return safe_x


def demo_all_function() -> tuple[bool, bool, bool, bool]:
    """Demonstrate the all() function."""
    check1 = all([True, 1, {3}])  # True, all are truthy
    check2 = all([True, 1, {}])  # False, {} is falsy
    check3 = all([])  # True, no falsy elements in the list
    check4 = all([True, True, True])  # True
    return check1, check2, check3, check4


def demo_any_function() -> tuple[bool, bool, bool, bool]:
    """Demonstrate the any() function."""
    check1 = any([True, 1, {}])  # True, True is truthy
    check2 = any([False, 0, {}])  # False, all are falsy
    check3 = any([])  # False, no truthy elements in the list
    check4 = any([False, False, True])  # True
    return check1, check2, check3, check4


def main() -> None:
    """Demonstrate truthiness concepts."""
    # Test basic booleans
    less_than, equals = demo_boolean_basics()
    assert less_than is True
    assert equals is False
    print("✓ Boolean basics work correctly")

    # Test None checking
    is_check, _ = demo_none_checking(None)
    assert is_check is True
    print("✓ None checking works correctly")

    # Test falsy values
    truthiness = demo_falsy_values()
    assert truthiness["False"] is False
    assert truthiness["None"] is False
    assert truthiness["empty list"] is False
    assert truthiness["empty dict"] is False
    assert truthiness["empty string"] is False
    assert truthiness["empty set"] is False
    assert truthiness["zero int"] is False
    assert truthiness["zero float"] is False
    print("✓ Falsy values work correctly")

    # Test truthy values
    t1, t2, t3, t4 = demo_truthy_values()
    assert t1 is True
    assert t2 is True
    assert t3 is True
    assert t4 is True
    print("✓ Truthy values work correctly")

    # Test short-circuit 'and'
    assert demo_short_circuit_with_and("hello") == "h"
    assert demo_short_circuit_with_and("") == ""
    print("✓ Short-circuit 'and' works correctly")

    # Test default value with 'or'
    assert demo_default_value_with_or(None) == 0
    assert demo_default_value_with_or(0) == 0
    assert demo_default_value_with_or(5) == 5
    print("✓ Default value with 'or' works correctly")

    # Test all()
    a1, a2, a3, a4 = demo_all_function()
    assert a1 is True
    assert a2 is False
    assert a3 is True
    assert a4 is True
    print("✓ all() function works correctly")

    # Test any()
    ay1, ay2, ay3, ay4 = demo_any_function()
    assert ay1 is True
    assert ay2 is False
    assert ay3 is False
    assert ay4 is True
    print("✓ any() function works correctly")

    print("\nAll truthiness concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
