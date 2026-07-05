"""Dictionaries.

Overview of *Dictionaries* and their usage.

Dictionaries are a fundamental data structure that associates values with keys,
allowing for quick retrieval of values.
"""


def demo_dict_creation() -> tuple[dict, dict, dict]:
    """Demonstrate creating dictionaries."""
    empty_dict = {}  # Pythonic
    empty_dict2 = dict()  # less Pythonic
    grades = {"Joel": 80, "Tim": 95}  # dictionary literal

    return empty_dict, empty_dict2, grades


def demo_dict_access() -> int:
    """Demonstrate accessing dictionary values."""
    grades = {"Joel": 80, "Tim": 95}
    joels_grade = grades["Joel"]  # equals 80

    return joels_grade


def demo_dict_key_error(grades: dict) -> str:
    """Demonstrate KeyError handling."""
    try:
        kates_grade = grades["Kate"]
        return f"Kate's grade is {kates_grade}"
    except KeyError:
        return "no grade for Kate!"


def demo_dict_membership() -> tuple[bool, bool]:
    """Demonstrate checking for key existence."""
    grades = {"Joel": 80, "Tim": 95}
    joel_has_grade = "Joel" in grades  # True
    kate_has_grade = "Kate" in grades  # False

    return joel_has_grade, kate_has_grade


def demo_dict_get() -> tuple[int, int, None]:
    """Demonstrate the get method with default values."""
    grades = {"Joel": 80, "Tim": 95}
    joels_grade = grades.get("Joel", 0)  # equals 80
    kates_grade = grades.get("Kate", 0)  # equals 0
    no_ones_grade = grades.get("No One")  # default is None

    return joels_grade, kates_grade, no_ones_grade


def demo_dict_assignment() -> tuple[int, dict]:
    """Demonstrate assigning and modifying dictionary values."""
    grades = {"Joel": 80, "Tim": 95}
    grades["Tim"] = 99  # replaces the old value
    grades["Kate"] = 100  # adds a third entry
    num_students = len(grades)  # equals 3

    return num_students, grades


def demo_dict_structured_data() -> dict:
    """Demonstrate using dictionaries to represent structured data."""
    tweet = {
        "user": "joelgrus",
        "text": "Data Science is Awesome",
        "retweet_count": 100,
        "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"],
    }

    return tweet


def demo_dict_iteration() -> tuple[list, list, list]:
    """Demonstrate iterating over dictionary keys, values, and items."""
    tweet = {
        "user": "joelgrus",
        "text": "Data Science is Awesome",
        "retweet_count": 100,
        "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"],
    }

    tweet_keys = list(tweet.keys())  # iterable for the keys
    tweet_values = list(tweet.values())  # iterable for the values
    tweet_items = list(tweet.items())  # iterable for the (key, value) tuples

    return tweet_keys, tweet_values, tweet_items


def demo_dict_membership_check() -> tuple[bool, bool, bool]:
    """Demonstrate checking membership in different dict views."""
    tweet = {
        "user": "joelgrus",
        "text": "Data Science is Awesome",
        "retweet_count": 100,
        "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"],
    }

    check1 = "user" in tweet.keys()  # True, but not Pythonic
    check2 = "user" in tweet  # Pythonic way of checking for keys
    check3 = "joelgrus" in tweet.values()  # checking values

    return check1, check2, check3


def main() -> None:
    """Demonstrate dictionary concepts."""
    # Test dict creation
    empty1, empty2, grades = demo_dict_creation()
    assert isinstance(empty1, dict) and len(empty1) == 0
    assert isinstance(empty2, dict) and len(empty2) == 0
    assert grades == {"Joel": 80, "Tim": 95}
    print("✓ Dictionary creation works correctly")

    # Test dict access
    joels_grade = demo_dict_access()
    assert joels_grade == 80
    print("✓ Dictionary access works correctly")

    # Test KeyError handling
    result = demo_dict_key_error(grades)
    assert result == "no grade for Kate!"
    print("✓ KeyError handling works correctly")

    # Test membership
    joel_has, kate_has = demo_dict_membership()
    assert joel_has is True
    assert kate_has is False
    print("✓ Dictionary membership check works correctly")

    # Test get method
    joel, kate, no_one = demo_dict_get()
    assert joel == 80
    assert kate == 0
    assert no_one is None
    print("✓ Dictionary get method works correctly")

    # Test assignment
    num_students, updated_grades = demo_dict_assignment()
    assert num_students == 3
    assert updated_grades["Tim"] == 99
    assert updated_grades["Kate"] == 100
    print("✓ Dictionary assignment works correctly")

    # Test structured data
    tweet = demo_dict_structured_data()
    assert tweet["user"] == "joelgrus"
    assert tweet["retweet_count"] == 100
    print("✓ Dictionary structured data works correctly")

    # Test iteration
    keys, values, items = demo_dict_iteration()
    assert "user" in keys
    assert "joelgrus" in values
    assert len(items) == 4
    print("✓ Dictionary iteration works correctly")

    # Test membership checks
    check1, check2, check3 = demo_dict_membership_check()
    assert check1 is True
    assert check2 is True
    assert check3 is True
    print("✓ Dictionary membership checks work correctly")

    print("\nAll dictionary concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
