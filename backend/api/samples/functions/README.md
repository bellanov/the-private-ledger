# Functions

Overview of *Functions* and their usage.

A **function** is a rule for taking zero or more inputs and returning a corresponding output. In Python, we typically define functions using `def`:

```python
def double(x):
    """
    This is where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2
```

Python functions are **first-class**, which means that we can *assign* them to **variables** and *pass* them into functions just like any other arguments:

```python
def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double              # refers to the previously defined function
x = apply_to_one(my_double)     # equals 2
```

It is also easy to create short **anonymous** functions, or lambdas:

```python
y = apply_to_one(lambda x: x + 4)    # equals 5
```

You can assign lambdas to variables, although most people will tell you that you should just use `def` instead:

```python
another_double = lambda x: 2 * x        # don't do this

def another_double(x):
    """Do this instead"""
    return 2 * x
```

Function parameters can also be given **default arguments**, which only need to be specified when you want a value other than the default:

```python
def my_print(message="my default message"):
    print(message)

my_print("hello")       # prints 'hello'
my_print()              # prints 'my default message'
```

It is sometimes useful to specify arguments by **name**:

```python
def full_name(first="What's-his-name",last="Something"):
    return first + " " + last
```