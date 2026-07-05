# Counters

Overview of *Counters* and their usage.

A `Counter` turns a sequence of values into a `defaultdict(int)`-like object mapping keys to counts:

```python
from collections import Counter
c = Counter([0, 1, 2, 0])           # c is (basically) {0: 2, 1: 1, 2: 1}
```

This gives us a very simple way to solve our `word_counts` problem:

```python
# recall, document is a list of words
word_counts = Counter(document)
```

A `Counter` instance has a `most_common` method that is frequently useful:

```python
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)
```