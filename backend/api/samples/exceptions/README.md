# Exceptions

Overview of *Exceptions* and their usage.

When something goes wrong, Python raises an exception. Unhandled, exceptions will cause your program to crash. You can handle them using `try` and `except`:

```python
try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")
```

Although in many languages exceptions are considered bad, in Python there is no shame in using them to make your code cleaner, and we will sometimes do so.