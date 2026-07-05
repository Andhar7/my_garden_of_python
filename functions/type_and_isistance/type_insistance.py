
# Since Python does not enforce Optional, the professional way to protect a function is exactly what we just learned:

# def greet(name: Optional[str]) -> str:
#     if name is not None and not isinstance(name, str):
#         raise TypeError(f"Expected str or None, got {type(name).__name__}")
#     if name is None:
#         return "Hello, friend"
#     return f"Hello, {name}"

# Notice is not None — this is the professional Python pattern for checking None. Not != None, but is not None. Because None is a singleton, is is the correct comparison. 🌿

# `isinstance` sees the whole family tree.
# `type` sees only the exact leaf. 🌿

# This is the most practical pattern when you want to accept a *family* of types:
#
# ```python
def process_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    return value * 2
# ```
#
# One check. Multiple families. Clean and clear. 🌿

# `type` has a second face. Called with **three arguments**, it creates a new class:
#
# ```python
# This creates a class, just like the class keyword:
Dog = type("Dog", (), {"sound": "woof"})
my_dog = Dog()
print(my_dog.sound)   # woof
# ```
#
# This door leads into Python's **metaclass** system — the deepest garden of all, where classes are created and modified dynamically. We note it here and leave the door open. 🌱

## Part 6 — type(x).__name__ — A Useful Pattern

# When you want the name of a type as a string — for messages, logs, errors:
#
# ```python
x = [1, 2, 3]

print(type(x))           # <class 'list'>
print(type(x).__name__)  # list   ← clean, just the name
# ```
#
# Used in error messages:
#
# ```python
def double(x):
    if not isinstance(x, (int, float)):
        raise TypeError(
            f"Expected int or float, got {type(x).__name__}"
        )
    return x * 2

# double("peace")   # TypeError: Expected int or float, got str
# ```
#
# The error message names the actual type received — helpful, honest, professional. 🙏

### Pattern 1 — Validate Function Input

# ```python
def calculate_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError(f"width must be a number, got {type(width).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"height must be a number, got {type(height).__name__}")
    return width * height

def describe(value):
    if isinstance(value, bool):            # check bool BEFORE int — bool is a subclass of int!
        return f"A truth value: {value}"
    elif isinstance(value, int):
        return f"A whole number: {value}"
    elif isinstance(value, float):
        return f"A decimal number: {value}"
    elif isinstance(value, str):
        return f"A text of {len(value)} characters: '{value}'"
    elif isinstance(value, list):
        return f"A list of {len(value)} items"
    else:
        return f"Something else: {type(value).__name__}"

print(describe(True))      # A truth value: True
print(describe(42))        # A whole number: 42
print(describe(3.14))      # A decimal number: 3.14
print(describe("peace"))   # A text of 5 characters: 'peace'
 #*Notice: `bool` is checked BEFORE `int`. If we checked `int` first, `True` would match it (because bool is a subclass of int) and never reach the `bool` check.* 🌟


### Pattern 3 — Safe Conversion

def to_number(value):
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Cannot convert '{value}' to a number")
    raise TypeError(f"Cannot convert {type(value).__name__} to a number")

print(to_number(42))        # 42
print(to_number(3.14))      # 3.14
print(to_number("100"))     # 100
print(to_number("3.14"))    # 3.14



































