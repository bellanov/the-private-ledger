# Classes / Object-Oriented Programming (OOP)

Overview of *Classes / Object-Oriented Programming (OOP)* and their usage.

Like many languages, Python allows you to define *classes* that encapsulate data and the functions that operate on them. We’ll use them sometimes to make our code
cleaner and simpler. It’s probably simplest to explain them by constructing a heavily
annotated example.

Here we’ll construct a class representing a “counting clicker,” the sort that is used at
the door to track how many people have shown up for the “advanced topics in data science” meetup.

It maintains a `count`, can be `click`ed to increment the count, allows you to `read_count`, and can be `reset` back to zero. (In real life one of these rolls over from
*9999* to *0000*, but we won’t bother with that.)

To define a class, you use the `class` keyword and a *PascalCase* name:

```python
class CountingClicker:
    """A class can/should have a docstring, just like a function"""
```

A class contains zero or more **member** functions. By convention, each takes a first
parameter, `self`, that refers to the particular class instance.

Normally, a class has a constructor, named `__init__`. It takes whatever parameters you need to construct an instance of your class and does whatever setup you need:

```python
def __init__(self, count = 0 ):
    self.count = count
```

Although the constructor has a funny name, we construct instances of the clicker using just the class name:

```python
clicker1 = CountingClicker()                # initialized to 0
clicker2 = CountingClicker(100)             # starts with count=100
clicker3 = CountingClicker(count = 100)     # more explicit way of doing the same
```

Notice that the `__init__` method name starts and ends with double underscores. These “magic” methods are sometimes called “dunder” methods (double-UNDERscore, get it?) and represent “special” behaviors.

> Class methods whose names start with an underscore are—by convention—considered “private,” and users of the class are not supposed to directly call them. However, Python will not *stop* users from calling them.

Another such method is `__repr__`, which produces the string representation of a class instance:

```python
def __repr__(self):
    return f"CountingClicker(count={self.count})"
```

And finally we need to implement the *public* API of our class:

```python
def click(self, num_times = 1):
    """Click the clicker some number of times."""
    self.count += num_times

def read(self):
    return self.count

def reset(self):
    self.count = 0
```

Having defined it, let’s use `assert` to write some test cases for our clicker:

```python
clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"
```

Writing tests like these help us be confident that our code is working the way it’s designed to, and that it remains doing so whenever we make changes to it.

We’ll also occasionally create *subclasses* that *inherit* some of their functionality from a parent class. For example, we could create a non-reset-able clicker by using `CountingClicker` as the base class and overriding the `reset` method to do nothing:

```python
# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"
```

## Abstract Classes

An **abstract class** is a class that cannot be instantiated directly. It defines a common interface—a set of methods that every subclass *must* implement. Python provides this via the `abc` module (`ABC` and `abstractmethod`).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""

    def describe(self) -> str:
        return f"I am a {type(self).__name__} with area={self.area():.2f}"
```

The `@abstractmethod` decorator marks `area` and `perimeter` as *required*. Any subclass that doesn't implement all abstract methods will raise a `TypeError` when you try to instantiate it:

```python
# This would raise TypeError: Can't instantiate abstract class Shape
# with abstract methods area, perimeter
# s = Shape()
```

Concrete subclasses provide the implementations:

```python
import math

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
```

Now we can use polymorphism — treat every `Shape` the same way regardless of the concrete type:

```python
shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(shape.describe())
    assert shape.area() > 0
    assert shape.perimeter() > 0
```

Key points:

- Import `ABC` and `abstractmethod` from the `abc` module.
- Decorate each required method with `@abstractmethod`.
- Subclasses *must* implement every abstract method or they too become abstract.
- Non-abstract methods (like `describe` above) are inherited as-is by all subclasses.