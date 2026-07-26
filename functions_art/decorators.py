

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

