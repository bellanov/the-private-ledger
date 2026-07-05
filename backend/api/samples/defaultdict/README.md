# defaultdict

Overview of *defaultdict* and its usage.

Imagine that you’re trying to count the words in a document. An obvious approach is to create a dictionary in which the keys are words and the values are counts. As you check each word, you can increment its count if it’s already in the dictionary and add it to the dictionary if it’s not:

```python
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
```

You could also use the “forgiveness is better than permission” approach and just handle the exception from trying to look up a missing key:

```python
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
```

A third approach is to use `get`, which behaves gracefully for missing keys:

```python
from collections import defaultdict

word_counts = defaultdict(int)      # int() produces 0
for word in document:
    word_counts[word] += 1
```

They can also be useful with `list` or `dict`, or even your own functions:

```python
dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])   # Define custom types
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}
```

These will be useful when we’re using dictionaries to *“collect”* results by some key and don’t want to have to check every time to see if the key exists yet.

A useful rule of thumb is:

- use `defaultdict(int)` when the default can come from calling `int()`
- use `defaultdict(list)` when the default can come from calling `list()`
- use `defaultdict(lambda: [0, 0])` when you need a `custom` fresh object each time