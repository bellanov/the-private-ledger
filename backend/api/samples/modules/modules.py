"""Modules.

Overview of *Modules* and their usage.

Modules allow you to use features from the Python standard library and
third-party packages.
"""

import re
import re as regex
from collections import Counter, defaultdict
from typing import Pattern


def demo_import_module() -> Pattern:
    """Demonstrate importing a module."""
    # Import the re module and use it
    my_regex = re.compile("[0-9]+", re.I)
    return my_regex


def demo_import_alias() -> Pattern:
    """Demonstrate importing with an alias."""
    # Use alias to avoid name conflicts
    my_regex = regex.compile("[0-9]+", regex.I)
    return my_regex


def demo_from_import() -> tuple:
    """Demonstrate importing specific items from a module."""
    # Import specific classes from collections
    lookup = defaultdict(int)
    my_counter = Counter()
    return lookup, my_counter


def demo_standard_library() -> str:
    """Demonstrate using standard library modules."""
    import json
    import os
    import sys

    # Get Python version
    python_version = sys.version_info.major

    # Get current directory
    current_dir = os.getcwd()

    # Parse JSON
    data = json.loads('{"name": "Python", "version": 3}')

    return f"Python {python_version}: {data['name']}"


def demo_collections_module() -> tuple:
    """Demonstrate collections module utilities."""
    from collections import Counter, defaultdict, deque

    # Counter example
    word_counts = Counter("hello world hello")

    # defaultdict example
    groups = defaultdict(list)
    groups["even"].append(2)
    groups["odd"].append(1)

    # deque example
    queue = deque([1, 2, 3])
    queue.append(4)
    queue.popleft()

    return word_counts, groups, list(queue)


def demo_math_module() -> tuple:
    """Demonstrate math module."""
    import math

    sqrt_4 = math.sqrt(4)
    pi_value = math.pi
    ceil_3_2 = math.ceil(3.2)

    return sqrt_4, pi_value, ceil_3_2


def main() -> None:
    """Demonstrate module concepts."""
    # Test importing module
    regex_pattern = demo_import_module()
    assert regex_pattern is not None
    assert regex_pattern.search("test123") is not None
    print("✓ Import module works correctly")

    # Test import with alias
    regex_alias = demo_import_alias()
    assert regex_alias is not None
    print("✓ Import with alias works correctly")

    # Test from...import
    lookup, counter = demo_from_import()
    assert isinstance(lookup, defaultdict)
    assert isinstance(counter, Counter)
    print("✓ from...import works correctly")

    # Test standard library
    result = demo_standard_library()
    assert "Python" in result
    print("✓ Standard library modules work correctly")

    # Test collections module
    word_counts, groups, queue = demo_collections_module()
    assert word_counts["l"] == 5  # 'l' appears 5 times in "hello world hello"
    assert groups["even"] == [2]
    assert queue == [2, 3, 4]
    print("✓ Collections module works correctly")

    # Test math module
    sqrt_4, pi_value, ceil_3_2 = demo_math_module()
    assert sqrt_4 == 2.0
    assert 3.14 < pi_value < 3.15
    assert ceil_3_2 == 4
    print("✓ Math module works correctly")

    print("\nAll module concepts demonstrated successfully!")
    print("\nKey Takeaways:")
    print("- import <module> - import entire module")
    print("- import <module> as <alias> - import with alias")
    print("- from <module> import <item> - import specific items")
    print("- Avoid 'from module import *' to prevent namespace pollution")


if __name__ == "__main__":
    main()
