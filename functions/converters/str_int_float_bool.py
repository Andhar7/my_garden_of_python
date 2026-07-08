

str(42)          # "42"
str(3.14)        # "3.14"
str(True)        # "True"
str(False)       # "False"
str(None)        # "None"
str([1, 2, 3])   # "[1, 2, 3]"
str({"a": 1})    # "{'a': 1}"

age = 25
message = "I am " + str(age) + " years old."   # must convert — cannot add int to str
print(message)   # "I am 25 years old."

int("42")      # 42    — string of digits → integer ✅
int("  7  ")   # 7     — leading/trailing spaces are fine ✅
int(3.9)       # 3     — decimal → integer: truncates (cuts off, does NOT round!)
int(3.1)       # 3     — same: always toward zero
int(-3.9)      # -3    — toward zero, not toward -4
int(True)      # 1     — True → 1
int(False)     # 0     — False → 0


### What `int()` Cannot Do

#```python
int("3.14")    # ValueError ❌ — "3.14" is not a clean integer string
int("peace")   # ValueError ❌ — not a number at all
int(None)      # TypeError  ❌ — None has no numeric meaning

int(3.9)    # 3  — NOT 4!
int(-3.9)   # -3 — NOT -4!


float(42)        # 42.0   — integer → float (adds the .0)
float("3.14")    # 3.14   — string → float ✅
float("42")      # 42.0   — whole number string → float ✅
float("  3.1 ")  # 3.1    — spaces trimmed ✅
float(True)      # 1.0
float(False)     # 0.0
float("inf")     # inf    — positive infinity
float("-inf")    # -inf   — negative infinity


float("peace")   # ValueError ❌
float(None)      # TypeError  ❌
float([1, 2])    # TypeError  ❌


int("3.14")     # ValueError ❌ — cannot jump from string to int if there's a decimal
float("3.14")   # 3.14       ✅ — must go through float first
int(float("3.14"))   # 3     ✅ — string → float → int: two steps


bool(0)      # False
bool(0.0)    # False
bool("")     # False  — empty string
bool([])     # False  — empty list
bool({})     # False  — empty dict
bool(())     # False  — empty tuple
bool(set())  # False  — empty set
bool(None)   # False

# Everything else is True:
bool(1)          # True
bool(42)         # True
bool(-1)         # True  — any non-zero number
bool("peace")    # True  — any non-empty string
bool([0])        # True  — a list with one item (even if the item is 0!)
bool("False")    # True  — "False" is a non-empty string!


bool("False")   # True  — it's a string, not the boolean False
bool("")        # False — empty string




































