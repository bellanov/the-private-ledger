# Iterables & Generators

Overview of *Iterables & Generators* and their usage.

One nice thing about a list is that you can retrieve specific elements by their indices. But you don’t always need this! A list of a billion numbers takes up a lot of memory. If you only want the elements one at a time, there’s no good reason to keep them all around. If you only end up needing the first several elements, generating the entire billion is hugely wasteful.

Often all we need is to iterate over the collection using `for`
and `in`. In this case we can create *generators*, which can be iterated over just like lists but generate their values lazily on demand.

One way to create generators is with functions and the `yield` operator:

```python
def generate_range(n):
    i = 0
    while i < n:
        yield i     # every call to yield produces a value of the generator
        i += 1
```

The following loop will consume the `yield`ed values one at a time until none are left:

```python
for i in generate_range(10):
    print(f"i: {i}")
```

(In fact, `range` is itself lazy, so there’s no point in doing this.)

With a generator, you can even create an infinite sequence:

```python
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1
```

although you probably shouldn’t iterate over it without using some kind of `break` logic.

> The flip side of laziness is that you can only iterate through a generator once. If you need to iterate through something multiple times, you’ll need to either re-create the generator each time or use a list. If generating the values is expensive, that might be a good reason to use a list instead.

A second way to create generators is by using `for` comprehensions wrapped in parentheses:

```python
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
```

Such a “generator comprehension” doesn’t do any work until you iterate over it (using `for` or `next`). We can use this to build up elaborate data-processing pipelines:

```python
# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x**2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on
```

Not infrequently, when we’re iterating over a list or a generator we’ll want not just the values but also their indices. For this common case Python provides an `enumerate` function, which turns values into pairs `(index, value)`:

```python
names = ["Alice", "Bob", "Charlie", "Debbie"]

# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")
```