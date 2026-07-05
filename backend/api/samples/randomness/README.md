# Randomness

Overview of *Randomness* in Python.

As we learn data science, we will frequently need to generate random numbers, which we can do with the `random` module:

```python
import random
random.seed(10)  # this ensures we get the same results every time
four_uniform_randoms = [random.random() for _ in range(4)]

# [0.5714025946899135,  # random.random() produces numbers
# 0.4288890546751146,   # uniformly between 0 and 1.
# 0.5780913011344704,   # It's the random function we'll use
# 0.20609823213950174]  # most often.
```

The `random` module actually produces *pseudorandom* (that is, deterministic) numbers based on an internal state that you can set with `random.seed` if you want to get reproducible results:

```python
random.seed(10)         # set the seed to 10
print(random.random())  # 0.57140259469
random.seed(10)         # reset the seed to 10
print(random.random())  # 0.57140259469 again
```

We’ll sometimes use `random.randrange`, which takes either one or two arguments and returns an element chosen randomly from the corresponding `range`:

```python
random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]
```

There are a few more methods that we’ll sometimes find convenient. For example, `random.shuffle` randomly reorders the elements of a list:

```python
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5] (your results will probably be different)
```

If you need to randomly pick one element from a list, you can use `random.choice`:

```python
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me
```

And if you need to randomly choose a sample of elements without replacement (i.e., with no duplicates), you can use `random.sample`:

```python
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]
```

To choose a sample of elements *with* replacement (i.e., allowing duplicates), you can
just make multiple calls to `random.choice`:

```python
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement) # [9, 4, 4, 2]
```