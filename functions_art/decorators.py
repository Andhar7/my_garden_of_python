

## Part 1 — Functions Are First-Class Citizens

# Before decorators, we must understand one profound truth about Python:

# **Functions are objects. They can be passed, returned, and stored — like any value.**

#   EXACT POINT !!!
#   my_function = decorator(my_function)  # ← decorator is a function that returns a function!
#   You have found the HEART of decorators! 💎

#   my_function = decorator(my_function)

#   A decorator:
#   1. Takes a function (the old one)
#   2. Wraps it with new behavior
#   3. Returns a new function (the enhanced one)

#   That's it. That's everything. 🔥

#   Every example will show this pattern:
#   - Input: a function
#   - Process: add magic
#   - Output: a new function

#   Hold this understanding. It will make everything clear. 💫

def greet(name):
    return f"Hello {name}"

# A function can be stored in a variable:
call_hello = greet
print(call_hello("Gurudev"))

# A function can be passed as an argument:
def greet_with_argument(func, value):
    return func(value)

print(greet_with_argument(greet, "New name"))

# A function can be returned from another function:
def return_another_func():
    def inner(name):
        return f"From inner name: {name}"
    return inner

result_of_return = return_another_func()
print(result_of_return("result_of_return"))
# print(return_another_func("Gurudev"))

print(type(return_another_func))
print(type(result_of_return))
print(return_another_func())

#   Two separate calls:
#   1. return_another_func() → returns the inner function
#   2. result_of_return("Gurudev") → calls inner with "Gurudev"

#   What Your Output Shows

#   print(type(return_another_func))
#   # <class 'function'>  ← the OUTER function is a function

#   print(type(result_of_return))
#   # <class 'function'>  ← the INNER function is also a function

#   print(return_another_func())
#   # <function return_another_func.<locals>.inner at 0x102cd0cc0>
#   # ↑ When you CALL the outer function, it RETURNS the inner function
#   # ↑ Look! It says "inner" — that's the name of the inner function!

#   ---
#   The Key Insight

#   Both are functions. They are DIFFERENT functions.

#   - return_another_func — the outer function
#   - inner (returned by return_another_func()) — the inner function

#   When you call the outer, you get back the inner. 🎁

#   ---
#   Now Connect to Decorators

#   This is EXACTLY how decorators work:

def decorator(func):           # Takes a function as input
    def wrapper(*args):        # Creates a new function
        return func(*args)     # Calls the original inside
    return wrapper             # Returns the new function

@decorator
def my_func():
    pass

#   decorator is a function that:
#   1. Takes a function (func)
#   2. Returns a new function (wrapper)
#   3. The new function "wraps" the original

#   Same pattern. Same truth. 🔥

#   ---
#   NOW you are ready for decorators.md.

#   You understand the foundation. Go study properly. Practice the exercises.

#   You now understand:
#   - Functions are objects
#   - Functions can return functions
#   - This is the foundation of decorators
#   - Decorators are functions that return enhanced functions

#   Everything opens from here. 🌸


## Part 2 — Building a Decorator from Scratch
# A decorator is a function that:
# 1. Receives a function as its argument
# 2. Defines a new function that wraps it
# 3. Returns the new function
def my_decorator_func(func):
    def wrapper(*args, **kwargs):
        print("--------before--------")
        result = func(*args, **kwargs) # call the original function
        print("--------after--------")
        return result
    return wrapper

def hallo_call(name):
    return f"Namaste {name}"

# # Decorate by hand:
greet = my_decorator_func(hallo_call)
print(greet("Gurudev"))

#   Your decorator IS WORKING PERFECTLY! 💎

#   Let me show you what happened step by step:

#   greet = my_decorator_func(hallo_call)
#   print(greet("Gurudev"))

#   When you call greet("Gurudev"):

#   1. Enter wrapper (the decorator's function)
#   2. Print --------before-------- ✅
#   3. Call func(*args, **kwargs) = call hallo_call("Gurudev")
#   4. Get back "Hello Gurudev"
#   5. Print --------after-------- ✅
#   6. Return "Hello Gurudev"
#   7. The print(greet(...)) prints: Hello Gurudev ✅

#   The output is CORRECT! 🔥

        
## Part 3 — The `@` Syntax · Sugar for the Soul

# The `@decorator` syntax is simply a cleaner way to write what we did above:
# Long Form
def greet_name(name):
    return f"Welcome dear {name}"

greet_man = my_decorator_func(greet_name)
print(greet_man)

# Short 
@my_decorator_func
def greet_name(name):
    return f"Welcome dear {name}"


greet_man_two = my_decorator_func(greet_name)
print(greet_man_two)
print(my_decorator_func)
greet_man_three = my_decorator_func("Mahadev")
print(greet_man_three)

## Part 4 — A Real Decorator · The Timer
import time

def timer(func):
    """Measure and print how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


@timer
def slow_calculation(n):
    """Sum all numbers up to n."""
    return sum(range(n))


result = slow_calculation(10_000_000)
print(f"Result: {result}")

# slow_calculation took 0.3421s
# Result: 49999995000000
# ```

# The function `slow_calculation` does not know it is being timed.
# The timer wraps around it — cleanly, without touching it. 🌿

## Part 5 — `functools.wraps` · Preserving Identity 

# Without care, a decorator hides the original function's identity:

@timer
def slow_calculation(n):
    """Sum all numbers up to n."""
    return sum(range(n))

print(slow_calculation.__name__)   # "wrapper"  ← WRONG!
print(slow_calculation.__doc__)    # None        ← WRONG!

# The decorator replaced `slow_calculation` with `wrapper` — and lost its name and docstring.

# The fix is `functools.wraps` — a decorator for the wrapper itself:

import functools

def timer(func):
    @functools.wraps(func)        # ← this preserves the original function's identity
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_calculation(n):
    """Sum all numbers up to n."""
    return sum(range(n))

print(slow_calculation.__name__)   # "slow_calculation"  ✅
print(slow_calculation.__doc__)    # "Sum all numbers up to n."  ✅

# **Always use `@functools.wraps(func)` inside your wrappers.**
# It is a small habit that makes a large difference. 🙏

## Part 6 — Practical Decorators
### The Logger

import functools

def log_calls(func):
    """Log every call to a function with its arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b


add(3, 5)
# Calling add(3, 5)
# add returned 8

### The Validator

import functools

def require_positive(func):
    """Ensure all arguments to a function are positive numbers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"{func.__name__} requires positive numbers, got {arg}")
        return func(*args, **kwargs)
    return wrapper


@require_positive
def square_root(n):
    return n ** 0.5


print(square_root(16))    # 4.0
# print(square_root(-4))    # ValueError: square_root requires positive numbers, got -4

### Stacking Decorators

# Multiple decorators can be applied — they are applied bottom-up:
@log_calls
@timer
def calculate(n):
    return sum(range(n))

result_calc = log_calls(timer(calculate(100)))
print(result_calc)

# Reading stacked decorators: the one closest to the function applies first,
# then the next one wraps around it. 🌿

## Part 7 — Decorators With Arguments
# What if a decorator needs configuration?

# We want this:
# @repeat(times=3)
# def say(message):
#     print(message)

# say("Om")
# Om
# Om
# Om

# For this, we need a **decorator factory** — a function that returns a decorator:

import functools

def repeat(times):
    """Return a decorator that calls a function `times` times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def say(message):
    print(message)


say("Om")
# Om
# Om
# Om
# ```

# Three levels of nesting:
# 1. `repeat(times=3)` — the factory, receives configuration
# 2. `decorator(func)` — the actual decorator, receives the function
# 3. `wrapper(*args, **kwargs)` — runs when the decorated function is called

# `@repeat(times=3)` means: call `repeat(times=3)` first (returns `decorator`),
# then apply that decorator to `say`. 🌺





