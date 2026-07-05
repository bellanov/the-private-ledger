# Asynchronous Programming

Overview of *Asynchronous Programming* in Python.

The following article gives a great summary on concurrency.

[Different Forms of Concurrency](http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/)

## Making the Right Choice

A summarization of the above article.

```python
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
       print("Use Threads")
else:
    print("Multi Processing")
```

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
- I/O Bound, Slow I/O, Many connections => Asyncio