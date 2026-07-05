# Dataclasses

Overview of *Dataclasses* and their usage.

# Background

Some programming languages provide a more **data-oriented** version of a `Class`. For instance, **C#** has the `Struct` type that is more suited to represent data structures.

In *Python 3.7*, the **Dataclasses** module was made available.

How are *Dataclasses* different than regular *Classes*?

- They have a built-in initializer that helps you fill in objects very quickly.
- They are an easy way to print, compare, and order data.
- You can create data that's read-only.

# Example

The example implements a `Person` class that stores some personal information about a person. The `before.py` sample begins with a regular class, which will then be converted into a Dataclass.

```python
class Person:
    name: str
    job: str
    age: str

    def __init__(self, name: str, job: str, age: str) -> None:
        self.name = name
        self.job = job
        self.age = age

person1 = Person("Alice", "Engineer", "30")
person2 = Person("Charlie", "Manager", "30")
person3 = Person("Charlie", "Manager", "40")

print(person1)  # <__main__.Person object at 0x...>
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these should be equal!!!
print(person3 == person2)  # False
```

When executed, the following output is generated.

```sh
<__main__.Person object at 0x000002447C878980>
2493170305616
2493170305936
False
Traceback (most recent call last):
  File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dataclasses\before.py", line 23, in <module>
    print(person1 < person2)  # TypeError: '<' not supported between instances of 'Person' and 'Person'
          ^^^^^^^^^^^^^^^^^
TypeError: '<' not supported between instances of 'Person' and 'Person'
```

Printing `person1` doesn't yield any useful information. You would also expect `person1` and `person2` to be equal since they have the exact same values.

This behavior is typical in regular classes. With Dataclasses, you would prefer these behaviors provide more use.

**Scenarios:**

- *Initializing Data*

    They have a built-in initializer that helps you fill in objects very quickly.

- *Printing Data*

    Dataclasses make it very easy to print the contents of Classes.

- *Comparing Data*

    With data, you may sometimes want to do deeper comparisons, where you take into account multiple `Class` attributes. Also, if the data is the same, you would expect the objects to be the same.

Dataclasses address the problems in the above scenarios.

## Creating a Dataclass

1. To convert this `Class` into a Dataclass, first you import the dataclass module.

    ```python
    from dataclasses import dataclass
    ```

2. Decorate the class with the `@dataclass` decorator.

    ```python
    @dataclass
    class Person:
        name: str
        job: str
        age: str
    ```

3. There is a built-in initializer helps you fill in objects very quickly, eliminating the need for an `__init__` function, so remove it.

    ```python
    @dataclass
    class Person:
        name: str
        job: str
        age: str

    person1 = Person("Alice", "Engineer", "30")
    person2 = Person("Charlie", "Manager", "30")
    person3 = Person("Charlie", "Manager", "40")
    ```

    This already makes the code more readable by eliminating unnecessary lines from every `Class` we create.

4. We also receive a different result when executing the same program.

    ```sh
    Person(name='Alice', job='Engineer', age='30')
    1164363942480
    1164363952720
    True
    ```

    Instead of the cryptic memory address, we now receive a more readable representation for **Alice**.

    We are also able to compare two objects correctly, with `person3 == person2` now yielding `True`, meaning the two data items are identical.

# Sorting a Dataclass

1. Dataclasses also make it easier to **sort** or **order** data. This can be achieved by specifying `order=True` in the `@dataclass` decorator.

    ```python
    @dataclass(order=True)
    class Person:
        name: str
        job: str
        age: str
    ```

By default, Dataclasses are sorted in order of their class attribute definition. In this case it would be, `name -> job -> age`.

2. In most cases, it is better to control this behavior yourself, so that your programs don't run into unexpected behavior.

    This can be achieved by specifying the `sort_index` attribute. Initialize the value with the attribute (i.e., `age`) that you would like to sort by within the `__post_init__` method, which executes right after an object is initialized.

    A tuple (i.e., `(self.age, self.name, self.job)`) can be specified to sort by multiple values.

    ```python
    @dataclass(order=True)
    class Person:
        sort_index: int = field(init=False)
        name: str
        job: str
        age: str

        def __post_init__(self):
            self.sort_index = (self.age, self.name, self.job)

    person1 = Person("Alice", "Engineer", "30")
    person2 = Person("Charlie", "Manager", "40")
    person3 = Person("Charlie", "Manager", "40")
    ```

    Upon execution, the updated output contains the sort_index as one of the class attributes.

    ```sh
    Person(sort_index=('30', 'Alice', 'Engineer'), name='Alice', job='Engineer', age='30')
    1881390107216
    1881390117456
    True
    True
    ```

We only need this to sort, so it's a good idea to remove this from this output. This can be accomplished by modifying the **string representation** of the class.

3. This can be accomplished by updating the attribute declaration with the `repr=False` parameter.

    ```python
    sort_index: int = field(init=False, repr=False)
    ```

    Upon execution, the sort_index no longer appears within the output.

    ```python
    Person(name='Alice', job='Engineer', age='30')
    2192302459472
    2192302469712
    True
    True
    ```

## Default Values

1. Dataclasses also let you define **default values**.

    To do so, initialize the attribute and set it to an initial value. 

    ```python
    @dataclass(order=True)
    class Person:
        sort_index: int = field(init=False, repr=False)
        name: str
        job: str
        age: str
        strength: int = 100
    ```

2. It can still also be passed as a parameter, with `Alice` being defined with a `strength` of 80 below.

    ```python
    Person(name='Alice', job='Engineer', age=30, strength=80)
    2587289307728
    2587289317968
    True
    True
    ```

## Creating Read-Only Objects

1. You can also `freeze` Dataclasses by specifying the `frozen=True` parameter.

    ```python
    class Person:
        sort_index: int = field(init=False, repr=False)
        name: str
        job: str
        age: int
        strength: int = 100

        def __post_init__(self):
            self.sort_index = (self.age, self.name, self.job)
    ```

2. Running the program results in an **error** because the `Class` cannot be updated after instantiation due to it being *frozen*. This shows that the class is indeed `ReadOnly`.

    ```sh
    Traceback (most recent call last):
    File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dataclasses\after.py", line 16, in <module>
        person1 = Person("Alice", "Engineer", 30, 80)
    File "<string>", line 7, in __init__
    File "C:\Users\cityd\Documents\GitHub\python-samples\samples\dataclasses\after.py", line 13, in __post_init__
        self.sort_index = (self.age, self.name, self.job)
        ^^^^^^^^^^^^^^^
    File "<string>", line 35, in __setattr__
    dataclasses.FrozenInstanceError: cannot assign to field 'sort_index'
    ```

    To get around this, we can avoid interacting with the `self` object by using the `__setattr__` method to achieve the same result without touching the `Class`.

    ```python
    @dataclass(order=True, frozen=True)
    class Person:
        sort_index: int = field(init=False, repr=False)
        name: str
        job: str
        age: int
        strength: int = 100

        def __post_init__(self):
            object.__setattr__(self, "sort_index", (self.strength, self.age))
    ```

3. Upon execution, the program now runs successfully.

    ```sh
    Person(name='Alice', job='Engineer', age=30, strength=80)
    2234643302992
    2234647581776
    True
    True
    ```

## String Representation

1. There is a nicer way to print out the data using the `__str__` method. Defining this method lets us control the output whenever this `Class` is printed.

    ```python
    @dataclass(order=True, frozen=True)
    class Person:
        sort_index: int = field(init=False, repr=False)
        name: str
        job: str
        age: int
        strength: int = 25

        def __post_init__(self):
            object.__setattr__(self, "sort_index", (self.age, self.name, self.job))

        def __str__(self) -> str:
            return f"name={self.name}, job={self.job}, age={self.age}, strength={self.strength})"
    ```

2. Upon execution, the class now outputs a more readable format that could be formated to be ready for consumption in *Web / Database Queries*, for instance.

    Dataclasses have great use in design patterns for *ingesting / transforming* data and *data manipulation*, such as the `pandas` module.

    ```python
    name=Alice, job=Engineer, age=30, strength=80)
    2362450234256
    2362454513040
    True
    True
    ```
