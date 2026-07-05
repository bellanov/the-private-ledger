# Common Mistakes

A catalogue of rookie / amateur mistakes that Python beginners frequently make, with the correct idiomatic approach shown side-by-side.

| # | Mistake | Why It's Wrong | Fix |
|---|---|---|---|
| 1 | **Mutable default arguments** | Default is evaluated once — all callers share the same object | Use `None` as default; create the object inside the function |
| 2 | **`== None` / `== True`** | `__eq__` can be overridden; singletons should be compared by identity | Use `is None`, `is True`, `is False` |
| 3 | **Bare `except:`** | Swallows `KeyboardInterrupt`, `SystemExit`, and hides bugs | Catch the specific exception type(s) you expect |
| 4 | **String `+=` in a loop** | Creates a new `str` object every iteration — O(N²) | Use `"".join(items)` — O(N) |
| 5 | **`range(len(x))`** | Throws away Python's iteration protocol; fragile and verbose | Use `enumerate(x)` for index+value, or iterate directly |
| 6 | **No context manager for resources** | File/socket stays open if an exception is raised | Use `with open(...) as f:` — guaranteed cleanup |
| 7 | **Implicit `None` return on some paths** | Callers get a surprising `None` with no error | Add an explicit `raise` or `return` on every path |
| 8 | **Mutating a list while iterating** | Internal index shifts — items get skipped silently | Build a new list with a comprehension |
| 9 | **`assert` for input validation** | Assertions are stripped with `python -O` | Use `if … raise ValueError(…)` — always enforced |
| 10 | **Shadowing built-in names** | Replaces `list`, `dict`, `id`, etc. for the rest of the scope | Use descriptive variable names that don't clash with builtins |
