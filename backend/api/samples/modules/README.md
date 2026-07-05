# Modules

Overview of *Modules* and their usage.

Certain features of Python are not loaded by default. These include both features that are included as part of the language as well as third-party features that you download yourself. In order to use these features, you’ll need to `import` the modules that contain them.

One approach is to simply import the module itself:

```python
import re
my_regex = re.compile("[0-9]+",re.I)
```

If you already had a different `re` in your code, you could use an **alias**:

```python
import re as regex

my_regex = regex.compile("[0-9]+",regex.I)
```

You might also do this if your module has an unwieldy name or if you’re going to be typing it a lot. For example, a standard convention when visualizing data with matplotlib is:

```python
import matplotlib.pyplot as plt

plt.plot(...)
```

If you need a few specific values from a module, you can import them explicitly and use them without qualification:

```python
from collections import defaultdict, Counter

lookup = defaultdict(int)
my_counter = Counter()
```

If you were a bad person, you could import the entire contents of a module into your **namespace**, which might inadvertently *overwrite* variables you’ve already defined:

```python
match = 10
from re import *
# uh oh, re has a match function
print(match)
# "<function match at 0x10281e6a8>"
```

However, since you are not a bad person, you won’t ever do this.