"""Common Mistakes.

A catalogue of rookie / amateur mistakes that Python beginners frequently make,
shown side-by-side with the correct idiomatic approach.

Each section is self-contained and runnable.
"""

# ─────────────────────────────────────────────
# MISTAKE 1: Mutable default arguments
#
# Default argument values are evaluated ONCE at function definition time,
# not on each call. Using a mutable object (list, dict, set) as a default
# means all callers share the same object.
# ─────────────────────────────────────────────


def append_bad(value, result=[]):  # ❌ shared list across all calls
    result.append(value)
    return result


def append_good(value, result=None):  # ✅ create a fresh list each call
    if result is None:
        result = []
    result.append(value)
    return result


# ─────────────────────────────────────────────
# MISTAKE 2: Using == to compare against None / True / False
#
# None, True, and False are singletons. Use `is` / `is not` to test identity,
# not equality. == can be overridden by __eq__ on custom classes.
# ─────────────────────────────────────────────


def check_none_bad(value):
    if value == None:  # ❌ fragile; custom __eq__ can fool this
        return "nothing"
    return value


def check_none_good(value):
    if value is None:  # ✅ identity check — always correct
        return "nothing"
    return value


# ─────────────────────────────────────────────
# MISTAKE 3: Catching bare Exception (or worse, BaseException)
#
# Catching too broadly swallows keyboard interrupts, system exits, and bugs,
# making programs hard to stop and impossible to debug.
# ─────────────────────────────────────────────


def read_file_bad(path: str):
    try:
        with open(path) as f:
            return f.read()
    except:  # ❌ catches EVERYTHING, including KeyboardInterrupt
        return None


def read_file_good(path: str):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:  # ✅ only the specific error we expect
        return None


# ─────────────────────────────────────────────
# MISTAKE 4: Building strings with + in a loop
#
# str is immutable — each += creates a brand-new string object.
# For N items this is O(N²) in both time and memory.
# Use str.join() or a list accumulator instead.
# ─────────────────────────────────────────────


def build_csv_bad(items: list[str]) -> str:
    result = ""
    for item in items:
        result += item + ","  # ❌ O(N²) — new string on every iteration
    return result.rstrip(",")


def build_csv_good(items: list[str]) -> str:
    return ",".join(items)  # ✅ O(N) — single allocation


# ─────────────────────────────────────────────
# MISTAKE 5: Iterating with range(len(...))
#
# range(len(x)) is a C-style pattern that throws away Python's iteration
# protocol. Use enumerate() when you need the index, or iterate directly.
# ─────────────────────────────────────────────


def print_items_bad(items: list[str]) -> None:
    for i in range(len(items)):  # ❌ manual index, verbose
        print(i, items[i])


def print_items_good(items: list[str]) -> None:
    for i, item in enumerate(items):  # ✅ idiomatic, clear, safe
        print(i, item)


# ─────────────────────────────────────────────
# MISTAKE 6: Not using context managers for resources
#
# Files, sockets, and locks must be closed even when exceptions occur.
# Without `with`, a crash in the middle leaves the resource open.
# ─────────────────────────────────────────────


def write_file_bad(path: str, content: str) -> None:
    f = open(path, "w")  # ❌ file stays open if an exception is raised
    f.write(content)
    f.close()


def write_file_good(path: str, content: str) -> None:
    with open(path, "w") as f:  # ✅ guaranteed close via __exit__
        f.write(content)


# ─────────────────────────────────────────────
# MISTAKE 7: Returning None implicitly on one code path
#
# When a function explicitly returns a value on some paths but falls off
# the end on others, callers get a surprising None with no error.
# ─────────────────────────────────────────────


def get_discount_bad(tier: str) -> float:
    if tier == "gold":
        return 0.20
    elif tier == "silver":
        return 0.10
    # ❌ falls off the end — returns None for any other tier


def get_discount_good(tier: str) -> float:
    discounts = {"gold": 0.20, "silver": 0.10}
    if tier not in discounts:
        raise ValueError(f"Unknown tier: {tier!r}")  # ✅ fail loudly
    return discounts[tier]


# ─────────────────────────────────────────────
# MISTAKE 8: Modifying a list while iterating over it
#
# Removing items from a list mid-iteration skips elements because the
# internal index shifts under you.
# ─────────────────────────────────────────────


def remove_evens_bad(numbers: list[int]) -> list[int]:
    for n in numbers:
        if n % 2 == 0:
            numbers.remove(n)  # ❌ mutates the list being iterated — skips items
    return numbers


def remove_evens_good(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 != 0]  # ✅ build a new list


# ─────────────────────────────────────────────
# MISTAKE 9: Using assert for input validation
#
# assert statements are stripped out when Python runs with optimisations
# enabled (`python -O`). Never use them to guard production logic.
# ─────────────────────────────────────────────


def set_age_bad(age: int) -> None:
    assert age >= 0, "Age cannot be negative"  # ❌ disabled with -O flag


def set_age_good(age: int) -> None:
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")  # ✅ always enforced


# ─────────────────────────────────────────────
# MISTAKE 10: Shadowing built-in names
#
# Naming a variable list, dict, id, type, input, etc. silently replaces
# the built-in for the rest of that scope, causing confusing errors later.
# ─────────────────────────────────────────────


def shadow_bad():
    list = [1, 2, 3]  # ❌ shadows the built-in list type
    # list([1, 2])                     # would now raise TypeError
    return list


def shadow_good():
    numbers = [1, 2, 3]  # ✅ descriptive name, no shadowing
    return numbers


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────


def main() -> None:
    # Mistake 1 — mutable default
    print("=== Mutable Default Argument ===")
    print(append_bad(1))  # [1]
    print(append_bad(2))  # [1, 2]  ← shared state bug!
    print(append_good(1))  # [1]
    print(append_good(2))  # [2]     ← fresh list each time

    # Mistake 4 — string concatenation
    print("\n=== String Building ===")
    words = ["apple", "banana", "cherry"]
    print(build_csv_bad(words))
    print(build_csv_good(words))

    # Mistake 5 — range(len(...))
    print("\n=== Iteration ===")
    print_items_bad(["a", "b", "c"])
    print_items_good(["a", "b", "c"])

    # Mistake 8 — mutating while iterating
    print("\n=== List Mutation During Iteration ===")
    data_bad = [1, 2, 3, 4, 5, 6]
    data_good = [1, 2, 3, 4, 5, 6]
    print("Bad (skips items):", remove_evens_bad(data_bad))
    print("Good:             ", remove_evens_good(data_good))

    # Mistake 10 — shadowing
    print("\n=== Shadowing Built-ins ===")
    print(shadow_bad())
    print(shadow_good())


if __name__ == "__main__":
    main()
