# Type Annotations

Overview of *Type Annotations* in Python.

## Overview

Python is a *dynamically typed* language. That means that it in general it doesn’t care about the types of objects we use, as long as we use them in valid ways:

```python
def add(a, b):
    return a + b

assert add(10, 5) == 15, "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3], "+ is valid for lists"
assert add("hi ", "there") == "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")
```

whereas in a *statically typed* language our functions and objects would have specific types:

```python
def add(a: int, b: int) -> int:
    return a + b

add(10, 5)          # you'd like this to be OK
add("hi ", "there") # you'd like this to be not OK
```

In fact, recent versions of Python do (sort of) have this functionality. The preceding version of `add` with the `int` type annotations is valid Python 3.6!

However, these type annotations don’t actually *do* anything. You can still use the annotated `add` function to add strings, and the call to `add(10, "five")` will still raise the exact same `TypeError`.

That said, there are still (at least) four good reasons to use type annotations in your Python code:

- Types are an important form of documentation. This is doubly true in a book that is using code to teach you theoretical and mathematical concepts. Compare the following two function stubs:

    ```python
    def dot_product(x, y): ...

    # we have not yet defined Vector, but imagine we had
    def dot_product(x: Vector,y: Vector) -> float: ...
    ```

    I find the second one exceedingly more informative; hopefully you do too. (At this point I have gotten so used to type hinting that I now find untyped Python difficult to read.)

- There are external tools (the most popular is `mypy`) that will read your code, inspect the type annotations, and let you know about type errors before you ever run your code. For example, if you ran `mypy` over a file containing `add("hi ", "there")`, it would warn you:

    ```sh
    error: Argument 1 to "add" has incompatible type "str"; expected "int"
    ```

    Like `assert` testing, this is a good way to find mistakes in your code before you ever run it.

- Having to think about the types in your code forces you to design *cleaner* functions and interfaces:

    ```python
    from typing import Union

    def secretly_ugly_function(value, operation): ...

    def ugly_function(value: int, operation: Union[str, int, float, bool]) -> int:
        ...
    ```

    Here we have a function whose `operation` parameter is allowed to be a `string`, or an `int`, or a `float`, or a `bool`. It is highly likely that this function is fragile and difficult to use, but it becomes far more clear when the types are made explicit. Doing so, then, will force us to design in a less clunky way, for which our users will thank us.

- Using types allows your editor to help you with things like **autocomplete** and to get angry at type *errors*.

    Sometimes people insist that type hints may be valuable on large projects but are not worth the time for small ones. However, since type hints take almost no additional time to type and allow your editor to save you time, I maintain that they actually allow you to write code more quickly, even for small projects.

## How to Write Type Annotations

As we’ve seen, for built-in types like `int` and `bool` and `float`, you just use the type
itself as the annotation. What if you had (say) a `list`?

```python
def total(xs: list) -> float:
    return sum(total)
```

This isn’t wrong, but the type is not specific enough. It’s clear we really want `xs` to be a `list` of `floats`, not (say) a `list` of strings.

The `typing` module provides a number of parameterized types that we can use to do just this:

```python
from typing import List # note capital L

def total(xs: List[float]) -> float:
    return sum(total)
```

Up until now we’ve only specified annotations for function parameters and return types. For variables themselves it’s usually obvious what the type is:

```python
# This is how to type-annotate variables when you define them.
# But this is unnecessary; it's "obvious" x is an int.
x: int = 5
```

However, sometimes it’s not obvious:

```python
values = []         # what's my type?
best_so_far = None  # what's my type?
```

In such cases we will supply inline type hints:

```python
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None     # allowed to be either a float or None
```

The `typing` module contains many other types, only a few of which we’ll ever use:

```python
# the type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)
```

Finally, since Python has first-class functions, we need a type to represent those as well. Here’s a pretty contrived example:

```python
from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range (n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"
```

As type annotations are just Python objects, we can assign them to variables to make them easier to refer to:

```python
Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)
```

By the time you get to the end of the book, you’ll be quite familiar with reading and writing type annotations, and I hope you’ll use them in your code.