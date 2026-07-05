# List Comprehensions

Overview of *List Comprehensions* and their usage.

Frequently, you’ll want to transform a list into another list by choosing only certain elements, by transforming elements, or both. The Pythonic way to do this is with *list comprehensions*:

```python
even_numbers = [x for x in range(5) if x % 2 == 0]      # [0, 2, 4]
squares = [x*x for x in range(5)]                       # [0, 1, 4, 9, 16]
even_squares = [x*x for x in even_numbers]              # [0, 4, 16]
```

You can similarly turn lists into dictionaries or sets:

```python
square_dict = {x: x*x for x in range(5)}    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set = {x*x for x in [1, -1]}         # {1}
```

If you don’t need the value from the list, it’s common to use an underscore as the variable:

```python
zeros = [0 for _ in even_numbers]           # has the same length as even_numbers
```

A list comprehension can include multiple `for`s:

```python
pairs = [(x,y)
        for x in range(10)
        for y in range(10)]     # 100 pairs (0,0) (0,1) ... (9,8), (9,9)
```

and later `for`s can use the results of earlier ones:

```python
increasing_pairs = [(x,y)                       # only pairs with x < y,
                    for x in range(10)          # range(lo, hi) equals
                    for y in range(x + 1, 10)]  # [lo, lo + 1, ..., hi - 1]
```