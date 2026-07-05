"""Regular Expressions.

Overview of *Regular Expressions* in Python.

Regular expressions provide a powerful way to search and manipulate text patterns.
"""

import re


def demo_regex_match() -> bool:
    """Demonstrate re.match - checks if string STARTS with pattern."""
    # 'cat' doesn't start with 'a', so match returns None (falsy)
    return not re.match("a", "cat")


def demo_regex_search() -> bool:
    """Demonstrate re.search - checks if pattern exists ANYWHERE in string."""
    # 'cat' has an 'a' in it
    return bool(re.search("a", "cat"))


def demo_regex_search_not_found() -> bool:
    """Demonstrate re.search when pattern is not found."""
    # 'dog' doesn't have a 'c' in it
    return not re.search("c", "dog")


def demo_regex_split() -> list:
    """Demonstrate re.split - split string by pattern."""
    # Split on 'a' or 'b' in "carbs" to get ['c', 'r', 's']
    return re.split("[ab]", "carbs")


def demo_regex_sub() -> str:
    """Demonstrate re.sub - replace pattern with replacement."""
    # Replace all digits with dashes in "R2D2" to get "R-D-"
    return re.sub("[0-9]", "-", "R2D2")


def demo_extract_numbers() -> list:
    """Demonstrate extracting numbers from text."""
    text = "The prices are 10, 25, and 42 dollars"
    # findall returns all matches
    return re.findall(r"\d+", text)


def demo_extract_emails() -> list:
    """Demonstrate extracting emails from text."""
    text = "Contact alice@example.com or bob@test.org for more info"
    # Simple email pattern
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


def demo_word_boundary() -> bool:
    """Demonstrate word boundary matching."""
    # Match 'cat' as a whole word, not as part of 'catalog'
    return bool(re.search(r"\bcat\b", "catalog")) is False


def main() -> None:
    """Demonstrate regular expression concepts."""
    # Test match
    assert demo_regex_match() is True
    print("✓ re.match works correctly")

    # Test search
    assert demo_regex_search() is True
    print("✓ re.search works correctly")

    # Test search not found
    assert demo_regex_search_not_found() is True
    print("✓ re.search (not found) works correctly")

    # Test split
    result = demo_regex_split()
    assert len(result) == 3
    assert result == ["c", "r", "s"]
    print("✓ re.split works correctly")

    # Test sub
    result = demo_regex_sub()
    assert result == "R-D-"
    print("✓ re.sub works correctly")

    # Test extracting numbers
    result = demo_extract_numbers()
    assert result == ["10", "25", "42"]
    print("✓ Extracting numbers works correctly")

    # Test extracting emails
    result = demo_extract_emails()
    assert "alice@example.com" in result
    assert "bob@test.org" in result
    print("✓ Extracting emails works correctly")

    # Test word boundary
    assert demo_word_boundary() is True
    print("✓ Word boundary matching works correctly")

    # Test comprehensive regex operations
    re_examples = [
        not re.match("a", "cat"),
        re.search("a", "cat"),
        not re.search("c", "dog"),
        3 == len(re.split("[ab]", "carbs")),
        "R-D-" == re.sub("[0-9]", "-", "R2D2"),
    ]
    assert all(re_examples), "all the regex examples should be True"
    print("✓ All comprehensive regex examples work correctly")

    print("\nAll regex concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
