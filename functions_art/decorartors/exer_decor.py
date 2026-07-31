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


def retry(times: int = 3, delay: float = 0):
    """Decorator factory: retry a function up to "times" times on failure"""

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
import inspect


def validate_types(func):
    """Check argument type against type hints at call time"""
    hints = func.__annotations__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Match positional args to param names
        params = list(inspect.signature(func).parameters.keys())

        for i, (param_name, value) in enumerate(zip(params, args)):
            expected_type = hints.get(param_name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{param_name}' must be {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
                # Check keyword arguments
        for param_name, value in kwargs.items():
            expected_type = hints.get(param_name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{param_name}' must be {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )

        return func(*args, **kwargs)
    return wrapper

@validate_types
def add(a: int, b: int) -> int:
    return a + b 

result_validation = add(12, 3)
print(result_validation)


### Exercise 4 — The Cache With Expiry
def cache(max_age_seconds: float=60):
    
    """ Decorator factory: cache results but expire after  max_age_seconds """
    def decorator(func):
        stored = {}  # {args: (result, timestamp)}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            if key in stored:
                result, cached_at = stored[key]
                if now - cached_at < max_age_seconds:
                    return result  # cache hit - still fresh
                else:
                    del stored[key] # expired remove
                    
            result = func(*args, **kwargs)
            stored[key] = (result, now) # store with timestamp
            
            return result
        
        return wrapper
    
    return decorator

@cache(max_age_seconds=2)
def get_data_user(key):
    print(f"Fetching the key: {key}...")
    return f"Data for ... key: {key}"

print(get_data_user("users"))
print(get_data_user("users"))
time.sleep(3)
print(get_data_user("users"))
                    
# **`(args, tuple(sorted(kwargs.items())))`** — the cache key.
# We must include kwargs too — `f(a=1, b=2)` and `f(1, 2)` might differ.
# Sorting kwargs ensures `f(b=2, a=1)` and `f(a=1, b=2)` produce the same key. 🌿

### Exercise 5 — The Django-Style Guard
import time as _time

current_user = {"name": "Gurudev", "role": "admin"}

def require_auth(role: str="user"):
    
    """ Decorator factory: check that current_user has the required role """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_role = current_user.get("role", "anonymous")
            roles = ["anonymous", "user", "editor", "admin", "superuser"]
            
            if user_role not in roles or roles.index(user_role) < roles.index(role):
                raise PermissionError(
                    f" '{user_role}' role cannot access '{func.__name__}'."
                    f"Required role: '{role}' or higher"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

def measure(func):
    """ Log how long a function takes """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function name: {func.__name__} completed in {(end - start) * 1000:.2f}ms")
        return result
    return wrapper

@measure
@require_auth(role="admin")
def admin_dashboard():
    return "Welcome to admin dashboard"

@measure
@require_auth(role="superuser")
def superuser_panel():
    return "Top secret panel"

print(admin_dashboard())

try:
    print(superuser_panel())
except PermissionError as e:
    print(f"PermissionError: {e}")
# PermissionError: 'admin' role cannot access 'superuser_panel'. Required: 'superuser' or higher.


    
