"""args & kwargs.

Overview of *args & kwargs* and their usage.

*args allows a function to accept a variable number of positional arguments.
**kwargs allows a function to accept a variable number of keyword arguments.
"""


def doubler(f):
    """Create a higher-order function that doubles the output of a function.

    This initial version only works with single-argument functions.
    """

    def g(x):
        return 2 * f(x)

    return g


def doubler_correct(f):
    """Create a higher-order function that works with any function signature.

    Uses *args and **kwargs to accept arbitrary arguments.
    """

    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)

    return g


def f1(x):
    """Simple single-argument function."""
    return x + 1


def f2(x, y):
    """Function with multiple arguments."""
    return x + y


def magic(*args, **kwargs):
    """Demonstrate how *args and **kwargs work."""
    print("unnamed args:", args)
    print("keyword args:", kwargs)


def other_way_magic(x, y, z):
    """Function that will receive unpacked arguments."""
    return x + y + z


def main() -> None:
    """Demonstrate args and kwargs functionality."""
    # Example 1: doubler with single argument function works
    g = doubler(f1)
    assert g(3) == 8, "(3 + 1) * 2 should equal 8"
    assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"
    print("✓ Single-argument doubler works")

    # Example 2: doubler with multi-argument function fails (commented out)
    # This would fail because g only accepts one argument:
    # g = doubler(f2)
    # g(1, 2)  # TypeError: g() takes 1 positional argument but 2 were given

    # Example 3: magic demonstrates *args and **kwargs
    print("\nCalling magic with various arguments:")
    magic(1, 2, key="word", key2="word2")

    # Example 4: doubler_correct works with any function signature
    g2 = doubler_correct(f2)
    assert g2(1, 2) == 6, "doubler_correct should work now"
    print("\n✓ Multi-argument doubler_correct works")

    # Example 5: unpacking a list into function arguments
    args_list = [1, 2, 3]
    result = other_way_magic(*args_list)
    assert result == 6, "unpacking list should work"
    print("✓ Unpacking list as arguments works")

    # Example 6: unpacking a dict into keyword arguments
    kwargs_dict = {"x": 10, "y": 20, "z": 30}
    result = other_way_magic(**kwargs_dict)
    assert result == 60, "unpacking dict should work"
    print("✓ Unpacking dict as keyword arguments works")


if __name__ == "__main__":
    main()
