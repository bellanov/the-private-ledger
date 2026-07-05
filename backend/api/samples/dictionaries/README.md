# Dictionaries

Overview of *Dictionaries* and their usage.

Another fundamental data structure is a *dictionary*, which associates **values** with **keys** and allows you to quickly retrieve the value corresponding to a given key:

```python
empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {"Joel": 80, "Tim": 95}    # dictionary literal
```

You can look up the value for a key using square brackets:

```python
joels_grade = grades["Joel"]    # equals 80
```

But you’ll get a `KeyError` if you ask for a key that’s not in the dictionary:

```python
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")
```

You can check for the existence of a key using `in`:

```python
joel_has_grade = "Joel" in grades   # True
kate_has_grade = "Kate" in grades   # False
```

This membership check is fast even for large dictionaries.

Dictionaries have a `get` method that returns a default value (instead of raising an exception) when you look up a key that’s not in the dictionary:

```python
joels_grade = grades.get("Joel", 0)     # equals 80
kates_grade = grades.get("Kate", 0)     # equals 0
no_ones_grade = grades.get("No One")    # default is None
```

You can assign key/value pairs using the same square brackets:

```python
grades["Tim"] = 99          # replaces the old value
grades["Kate"] = 100        # adds a third entry
num_students = len(grades)  # equals 3
```

You can use dictionaries to represent structured data:

```python
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
```

although we’ll soon see a better approach.

Besides looking for specific keys, we can look at all of them:

```python
tweet_keys = tweet.keys()       # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items = tweet.items()     # iterable for the (key, value) tuples

"user" in tweet_keys        # True, but not Pythonic
"user" in tweet             # Pythonic way of checking for keys
"joelgrus" in tweet_values  # True (slow but the only way to check)
```

Dictionary keys must be **“hashable”**; in particular, you cannot use lists as keys. If you
need a *multipart key*, you should probably use a *tuple* or figure out a way to turn the
key into a string.