# Lists

Overview of *Lists* and their usage.

Probably the most fundamental data structure in Python is the **list**, which is simply an ordered collection (it is similar to what in other languages might be called an **array**, but with some added functionality):

```python
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)     # equals 3
list_sum = sum(integer_list)        # equals 6
```

You can get or set the *n*th element of a list with *square* brackets:

```python
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]         # equals 0, lists are 0-indexed
one = x[1]          # equals 1
nine = x[-1]        # equals 9, 'Pythonic' for last element
eight = x[-2]       # equals 8, 'Pythonic' for next-to-last element
x[0] = -1           # now x is [-1, 1, 2, 3, ..., 9]
```

You can also use square brackets to *slice* lists. The slice `i:j` means all elements from `i` (inclusive) to `j` (not inclusive). If you leave off the start of the slice, you’ll slice from the beginning of the list, and if you leave of the end of the slice, you’ll slice until the end of the list:

```python
first_three = x[:3]                     # [-1, 1, 2]
three_to_end = x[3:]                    # [3, 4, ..., 9]
one_to_four = x[1:5]                    # [1, 2, 3, 4]
last_three = x[-3:]                     # [7, 8, 9]
without_first_and_last = x[1:-1]        # [1, 2, ..., 8]
copy_of_x = x[:]                        # [-1, 1, 2, ..., 9]
```

You can similarly slice strings and other *“sequential”* types.

A slice can take a third argument to indicate its *stride*, which can be negative:

```python
every_third = x[::3]            # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]       # [5, 4, 3]
```

Python has an `in` operator to check for list membership:

```python
1 in [1, 2, 3]      # True
0 in [1, 2, 3]      # False
```

This check involves examining the elements of the list one at a time, which means that you probably shouldn’t use it unless you know your list is pretty small (or unless you don’t care how long the check takes).

It is easy to *concatenate* lists together. If you want to modify a list in place, you can use
`extend` to add items from another collection:

```python
x = [1, 2, 3]
x.extend([4, 5, 6])   # x is now [1, 2, 3, 4, 5, 6]
```

If you don’t want to modify `x`, you can use list addition:

```python
x = [1, 2, 3]
y = x +[4, 5, 6]    # y is [1, 2, 3, 4, 5, 6]; x is unchanged
```

More frequently we will append to lists one item at a time:

```python
x = [1, 2, 3]
x.append(0)     # x is now [1, 2, 3, 0]
y = x[-1]       # equals 0
z = len(x)      # equals 4
```

It’s often convenient to *unpack* lists when you know how many elements they contain:

```python
x,y = [1,2]     # now x is 1, y is 2
```

although you will get a `ValueError` if you don’t have the same number of elements on both sides.

A common idiom is to use an *underscore* for a value you’re going to throw away:

```python
_,y = [1, 2]    # now y == 2, didn't care about the first element
```