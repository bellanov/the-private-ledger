"""Strings.

Overview of *Strings* and their usage.

Strings are one of the most commonly used data types in Python. They can be
created with single or double quotes, and support various operations.
"""


def demo_string_delimiters() -> tuple[str, str]:
    """Demonstrate single and double quoted strings."""
    single_quoted_string = "data science"
    double_quoted_string = "data science"
    return single_quoted_string, double_quoted_string


def demo_escape_characters() -> tuple[int, int]:
    """Demonstrate escape characters and raw strings."""
    # Tab character (escape sequence)
    tab_string = "\t"  # represents the tab character
    tab_length = len(tab_string)

    # Raw string (backslashes are literal)
    not_tab_string = r"\t"  # represents the characters '\' and 't'
    not_tab_length = len(not_tab_string)

    return tab_length, not_tab_length


def demo_multiline_strings() -> str:
    """Demonstrate multiline strings using triple quotes."""
    multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
    return multi_line_string


def demo_string_concatenation(first_name: str, last_name: str) -> tuple[str, str, str]:
    """Demonstrate multiple ways to construct strings."""
    # String addition (old way)
    full_name1 = first_name + " " + last_name

    # String.format method
    full_name2 = "{0} {1}".format(first_name, last_name)

    # F-string (preferred in Python 3.6+)
    full_name3 = f"{first_name} {last_name}"

    return full_name1, full_name2, full_name3


def main() -> None:
    """Demonstrate string concepts."""
    # Test string delimiters
    single, double = demo_string_delimiters()
    assert single == double == "data science"
    print("✓ String delimiters work correctly")

    # Test escape characters
    tab_len, not_tab_len = demo_escape_characters()
    assert tab_len == 1, "tab string should have length 1"
    assert not_tab_len == 2, "raw string should have length 2"
    print("✓ Escape characters and raw strings work correctly")

    # Test multiline strings
    multiline = demo_multiline_strings()
    assert "first line" in multiline
    assert "second line" in multiline
    assert "third line" in multiline
    print("✓ Multiline strings work correctly")

    # Test string concatenation methods
    name1, name2, name3 = demo_string_concatenation("Joel", "Grus")
    assert name1 == "Joel Grus"
    assert name2 == "Joel Grus"
    assert name3 == "Joel Grus"
    assert name1 == name2 == name3
    print("✓ All string concatenation methods work correctly")

    print("\nAll string concepts demonstrated successfully!")


if __name__ == "__main__":
    main()
