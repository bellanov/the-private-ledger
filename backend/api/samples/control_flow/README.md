# Control Flow

Overview of *Control Flow* and its usage.

As in most programming languages, you can perform an action conditionally using `if`:

```python
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
```

You can also write a **ternary** if-then-else on one line, which we will do occasionally:

```python
parity = "even" if x % 2 == 0 else "odd"
```

Python has a `while` loop:

```python
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1
```

although more often we’ll use `for` and `in`:

```python
# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")
```

If you need more complex logic, you can use `continue` and `break`:

```python
for x in range(10):
    if x == 3:
        continue    # go immediately to the next iteration
    if x == 5:
        break       # quit the loop entirely
    print(x)
```

This will print **0**, **1**, **2**, and **4**.