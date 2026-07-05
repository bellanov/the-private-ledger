# Whitespace Formatting

Overview of *Whitespace Formatting* in Python.

Many languages use curly braces to delimit blocks of code. Python uses **indentation**:

```python
# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code.
for i in [1, 2, 3, 4, 5]:
    print(i)                    # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)                # first line in "for j" block
        print(i+j)              # last line in "for j" block
    print(i)                    # last line in "for i" block
print("done looping")
```

This makes Python code very **readable**, but it also means that you have to be very careful with your *formatting*.

> Programmers will often argue over whether to use tabs or spaces for indentation. For many languages it doesn’t matter that much; however, Python considers tabs and spaces different indentation and will not be able to run your code if you mix the two. When writing Python you should always use spaces, never tabs. (If you write code in an editor you can configure it so that the Tab key just inserts spaces.)

Whitespace is ignored inside parentheses and brackets, which can be helpful for long-winded computations:

```python
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12
                           + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
```

and for making code easier to read:

```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]
```

You can also use a backslash to indicate that a statement continues onto the next line, although we’ll rarely do this:

```sh
two_plus_three = 2 + \
                 3
```

One consequence of whitespace formatting is that it can be hard to copy and paste code into the Python shell. For example, if you tried to paste the code:

```python
for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print(i)
```

into the ordinary Python shell, you would receive the complaint:

```sh
IndentationError: expected an indented block
```
because the interpreter thinks the blank line signals the end of the `for` loop’s block.

**IPython** has a magic function called `%paste`, which correctly pastes whatever is on your clipboard, whitespace and all. This alone is a good reason to use **IPython**.