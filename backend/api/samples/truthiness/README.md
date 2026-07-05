# Truthiness

Overview of *Truthiness* in Python.

Booleans in Python work as in most other languages, except that they’re capitalized:

```python
one_is_less_than_two = 1 < 2        # equals True
true_equals_false = True == False   # equals False
```

Python uses the value `None` to indicate a nonexistent value. It is similar to other languages’ `null`:

```python
x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"
```

Python lets you use any value where it expects a Boolean. The following are all *“falsy”*:

- `False`
- `None`
- `[]` (an empty list)
- `{}` (an empty dict)
- `""`
- `set()`
- `0`
- `0.0`

Pretty much anything else gets treated as `True`. This allows you to easily use `if` statements to test for empty lists, empty strings, empty dictionaries, and so on. It also
sometimes causes tricky bugs if you’re not expecting this behavior:

```python
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""
```

A shorter (but possibly more confusing) way of doing the same is:

```python
first_char = s and s[0]
```

since `and` returns its *second* value when the *first* is “truthy,” and the first value when
it’s not. Similarly, if x is either a number or possibly `None`:

```python
safe_x = x or 0
```

is definitely a number, although:

```python
safe_x = x if x is not None else 0
```

is possibly more readable.

Python has an `all` function, which takes an iterable and returns `True` precisely when every element is *truthy*, and an `any` function, which returns `True` when at least **one** element is truthy:

```python
all([True, 1, {3}])     # True, all are truthy
all([True, 1, {}])      # False, {} is falsy
any([True, 1, {}])      # True, True is truthy
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy elements in the list
```