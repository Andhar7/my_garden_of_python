# Exercise number 1

import functools


def log_calls(func):
    """Log every call with arguments, return value and exceptions"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f" -> Calling {func.__name__} ({signature})")

        try:
            result = func(*args, **kwargs)
            print(f" <- {func.__name__} returned {result!r}")
            return result
        except Exception as e:
            print(f"x {func.__name__} raised {type(e).__name__}: {e}")
            raise
    
    return wrapper

@log_calls
def divide(a, b):
    return a / b

divide(12, 2)
divide(10, 3)

# **`raise` without an argument** — re-raises the current exception.
# The decorator logs the error AND allows it to propagate normally.
# Callers still see the exception — the decorator only adds observation. 🌿



# Exercise number 2

# **Exercise 2 — The Retry Decorator**

# Write `@retry(times=3, delay=0)` that calls a function up to `times` times
# if it raises an exception. If all attempts fail, raise the last exception.

# ```python
# import random

# @retry(times=3)
# def unreliable():
#     if random.random() < 0.7:   # 70% chance of failure
#         raise RuntimeError("Random failure!")
#     return "Success!"

# print(unreliable())   # retries up to 3 times, then either succeeds or raises
# ```

# *(Use `import time; time.sleep(delay)` between retries if `delay > 0`.)* 🌿

import time

def retry(times: int=3, delay: float=0):
    
    """ Decorator factory: retry a function up to "times" times on failure """
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} / {times} failed : {e}")
                    if attempt < times and delay > 0:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

import random
seed = random.seed(42)
print(f"Seed : {seed}")

@retry(times=5)
def unreliable():
    if random.random() < 0.7:
        raise RuntimeError("Random Failure")
    return "Success!!!"

print(f"Here is unreliable : {unreliable()}")

# **`last_exception`** — we store the exception from each attempt.
# If all attempts fail, we raise the last one — so the caller sees a real exception, not silence.

# **Three levels:**
# `retry(times=5)` → returns `decorator`.
# `decorator(unreliable)` → returns `wrapper`.
# `wrapper()` → runs the retry logic. 🌺


### Exercise 3 — The Type Checker
