"""Control Flow.

Overview of *Control Flow* and its usage.

Control flow statements like if/elif/else, while, and for loops are fundamental
to any programming language.
"""


def demo_if_statements(x: int) -> str:
    """Demonstrate if/elif/else statements."""
    if x > 2:
        message = "x is greater than 2"
    elif x > 1:
        message = "x is greater than 1"
    else:
        message = "x is 1 or less"
    return message


def demo_ternary(x: int) -> str:
    """Demonstrate ternary (one-line) if-then-else."""
    parity = "even" if x % 2 == 0 else "odd"
    return parity


def demo_while_loop() -> list[int]:
    """Demonstrate while loop."""
    x = 0
    results = []
    while x < 10:
        results.append(x)
        x += 1
    return results


def demo_for_loop() -> list[int]:
    """Demonstrate for loop with range."""
    results = []
    # range(10) is the numbers 0, 1, ..., 9
    for x in range(10):
        results.append(x)
    return results


def demo_continue_break() -> list[int]:
    """Demonstrate continue and break statements."""
    results = []
    for x in range(10):
        if x == 3:
            continue  # go immediately to the next iteration
        if x == 5:
            break  # quit the loop entirely
        results.append(x)
    return results  # will contain 0, 1, 2, 4


def main() -> None:
    """Demonstrate control flow concepts."""
    # Test if statements
    assert demo_if_statements(3) == "x is greater than 2"
    assert demo_if_statements(1.5) == "x is greater than 1"
    assert demo_if_statements(0) == "x is 1 or less"
    print("✓ If/elif/else statements work correctly")

    # Test ternary operator
    assert demo_ternary(4) == "even"
    assert demo_ternary(5) == "odd"
    print("✓ Ternary operator works correctly")

    # Test while loop
    while_result = demo_while_loop()
    assert while_result == list(range(10)), "while loop should produce 0-9"
    print("✓ While loop works correctly")

    # Test for loop
    for_result = demo_for_loop()
    assert for_result == list(range(10)), "for loop should produce 0-9"
    print("✓ For loop works correctly")

    # Test continue and break
    continue_break_result = demo_continue_break()
    assert continue_break_result == [
        0,
        1,
        2,
        4,
    ], "continue/break should skip 3 and stop at 5"
    print("✓ Continue and break work correctly")

    print("\nAll control flow concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
