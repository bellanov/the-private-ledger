# Sorting

Overview of *Sorting* and its usage.

Every Python list has a `sort` method that sorts it in place. If you don’t want to mess up your list, you can use the `sorted` function, which returns a new list:

```python
x = [4, 1, 2 , 3]
y = sorted(x)       # y is [1, 2, 3, 4], x is unchanged
x.sort()            # now x is [1, 2, 3, 4]
```

By default, `sort` (and`sorted`) sort a list from smallest to largest based on naively comparing the elements to one another.

If you want elements sorted from largest to smallest, you can specify a `reverse=True` parameter. And instead of comparing the elements themselves, you can compare the results of a function that you specify with `key`:

```python
# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)   # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)
```