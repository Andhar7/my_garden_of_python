

# **Exercise 1 — The Inspector's Round**
#
# You have a mixed basket:
# ```python
basket = [42, "peace", 3.14, True, [1, 2, 3], None, {"key": "val"}, (1, 2)]
# ```
# Loop through each item and print its value and its exact type name:
# ```
# 42       → int
# peace    → str
# 3.14     → float
# ...
# ```
# *(Use `type(item).__name__` for the clean name.)* 🌿
for b in basket:
    print(f"This basket: {b} has a name: {type(b).__name__}")


# **Exercise 2 — The Number Gate**
#
# Write a function `is_numeric(value)` that returns `True` if the value is an `int` or `float`, and `False` otherwise:
# ```python
# is_numeric(42)       # True
# is_numeric(3.14)     # True
# is_numeric("42")     # False
# is_numeric(True)     # ?  ← what does isinstance return here? Think first, then test.

def is_numeric(value):

    if isinstance(value, (int, float)):
        return True
    return False


print(is_numeric(42))
print(is_numeric(3.14))
print(is_numeric("42"))
print(is_numeric(True))


# **Exercise 3 — The Bool Mystery**
#
# Run this and truly understand each result:
# ```python
x = True

print(type(x)) # I expect: Bool
print(type(x) == bool)  # I expect : True
print(type(x) == int)   # I expect : False
print(isinstance(x, bool)) # I expect : Int
print(isinstance(x, int))  # I expect: True
print(True + True + True)  # I expect : 3
print(True * 7)   # I expect: 7
# ```
#
# Write in a comment next to each line what you expect *before* running.
# Then run and compare. 🌿

# **Exercise 4 — The Friendly Describer**
#
# Write a function `describe(value)` that returns a human-friendly description:
# - `int` (but not `bool`) → `"whole number: 42"`
# - `bool` → `"truth value: True"`
# - `float` → `"decimal: 3.14"`
# - `str` → `"text (N characters): 'peace'"`
# - `list` → `"list with N items"`
# - anything else → `"unknown type: typename"`
#
# *(Remember: check `bool` BEFORE `int` — why is this order essential?)* 🌟
def describe(value):

    if isinstance(value, bool):
        return f"Truth value: {value}"
    elif isinstance(value, int):
        return f"Whole number: {value}"
    elif isinstance(value, float):
        return f"Decimal: {value}"
    elif isinstance(value, str):
        return f"Text {len(value)} characters: {value}"
    elif isinstance(value, list):
        return f"List with {len(value)} items"
    else:
        return f"Unknown type: {type(value).__name__}"

# **Exercise 5 — The Safe Calculator**
#
# Write a function `safe_add(a, b)` that:
# - If both `a` and `b` are numeric (`int` or `float`) — adds them and returns the result
# - If either is not numeric — raises a `TypeError` with a message naming the wrong type
#
# ```python
# safe_add(3, 5)          # 8
# safe_add(3.0, 2)        # 5.0
# safe_add("3", 5)        # TypeError: Expected number, got str
# safe_add(3, [1, 2])     # TypeError: Expected number, got list
# ```
def safe_add(a,b):

    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number, got {type(b).__name__}")
    return a + b


print(safe_add(3, 5))
print(safe_add(3.0, 2))
print(safe_add("3", 5))
print(safe_add(3, [1, 2]))


















