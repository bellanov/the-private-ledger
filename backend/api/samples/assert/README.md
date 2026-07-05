# assert

Overview of *assert* and its usage.

As data scientists, we’ll be writing a lot of code. How can we be confident our code is correct? One way is with **types**, but another way is with
**automated** tests.

There are elaborate frameworks for writing and running tests, but in this book we’ll
restrict ourselves to using `assert` statements, which will cause your code to raise an `AssertionError` if your specified condition is not truthy:

```python
assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"
```

As you can see in the second case, you can optionally add a message to be printed if
the assertion fails.

It’s not particularly interesting to assert that `1 + 1 = 2`. What’s more interesting is to
assert that functions you write are doing what you expect them to:

```python
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1
```

Throughout the book we’ll be using `assert` in this way. It is a good practice, and I
strongly encourage you to make liberal use of it in your own code. (If you look at the book’s code on GitHub, you will see that it contains many, many more `assert` statements than are printed in the book. This helps *me* be confident that the code I’ve written for you is correct.)

Another less common use is to assert things about inputs to functions:

```python
def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)
```
