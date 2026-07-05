"""Randomness.

Overview of *Randomness* in Python.

Python's random module provides tools for generating random numbers and making
random selections.
"""

import random


def demo_random_seed() -> list:
    """Demonstrate that seeds produce reproducible results."""
    random.seed(10)
    return [random.random() for _ in range(4)]


def demo_random_repeatability() -> tuple[float, float]:
    """Demonstrate that same seed produces same sequence."""
    random.seed(10)
    first = random.random()
    random.seed(10)
    second = random.random()
    return first, second


def demo_randrange_single_arg() -> int:
    """Demonstrate random.randrange with single argument."""
    random.seed(42)
    # Choose randomly from range(10) = [0, 1, ..., 9]
    return random.randrange(10)


def demo_randrange_two_args() -> int:
    """Demonstrate random.randrange with two arguments."""
    random.seed(42)
    # Choose randomly from range(3, 6) = [3, 4, 5]
    return random.randrange(3, 6)


def demo_shuffle() -> list:
    """Demonstrate random.shuffle."""
    up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.seed(42)
    random.shuffle(up_to_ten)
    return up_to_ten


def demo_choice() -> str:
    """Demonstrate random.choice."""
    random.seed(42)
    my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
    return my_best_friend


def demo_sample() -> list:
    """Demonstrate random.sample for sampling without replacement."""
    random.seed(42)
    # Choose 3 elements without replacement from range(10)
    return random.sample(range(10), 3)


def main() -> None:
    """Demonstrate randomness concepts."""
    # Test seed produces reproducible results
    sequence1 = demo_random_seed()
    random.seed(10)
    sequence2 = [random.random() for _ in range(4)]
    assert sequence1 == sequence2
    print("✓ Seed produces reproducible results")

    # Test repeatability
    first, second = demo_random_repeatability()
    assert first == second
    print("✓ Same seed produces same sequence")

    # Test randrange with single argument
    result = demo_randrange_single_arg()
    assert 0 <= result < 10
    print("✓ randrange(n) works correctly")

    # Test randrange with two arguments
    result = demo_randrange_two_args()
    assert 3 <= result < 6
    print("✓ randrange(a, b) works correctly")

    # Test shuffle
    shuffled = demo_shuffle()
    assert set(shuffled) == set(range(1, 11))
    assert len(shuffled) == 10
    print("✓ shuffle works correctly")

    # Test choice
    choice = demo_choice()
    assert choice in ["Alice", "Bob", "Charlie"]
    print("✓ choice works correctly")

    # Test sample
    sampled = demo_sample()
    assert len(sampled) == 3
    assert all(0 <= x < 10 for x in sampled)
    assert len(set(sampled)) == 3  # All unique
    print("✓ sample (without replacement) works correctly")

    print("\nAll randomness concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
