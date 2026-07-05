# Tuples

Overview of *Tuples* and their usage.

*Tuples* are lists’ **immutable** cousins. Pretty much anything you can do to a list that doesn’t involve modifying it, you can do to a tuple. You specify a tuple by using
**parentheses** (or nothing) instead of square brackets:

```python
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3      # my_list is now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
```

Tuples are a convenient way to return multiple values from functions:

```python
def sum_and_product(x, y):
    return (x + y), (x * y )

sp = sum_and_product(2, 3)      # sp is (5, 6)
s, p = sum_and_product(5, 10)   # s is 15, p is 50
```

Tuples (and lists) can also be used for multiple assignment:

```python
x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # Pythonic way to swap variables; now x is 2, y is 1
```