

name = "Gurudev"
print(repr(name))

import datetime 
today = datetime.date(2026, 6, 7)
print(str(today))
print(repr(today))

class Meditator:
    
    def __init__(self, name, years):
        self.name = name
        self.years = years
        
    def __repr__(self):
        return f"Meditator from repr is: (name={self.name}, years={self.years})"
    
    def __str__(self):
        return f"{self.name} - {self.years} years of practice 🙏🌹"

gurudev = Meditator("Mahadev", 21)
print(repr(gurudev))
print(str(gurudev))

# If an object has only `__repr__` and no `__str__`, Python uses `repr()` for both.
# If an object has both, each serves its own purpose.

### `repr()` in Practice — Debugging

# The true home of `repr()` is debugging. When something unexpected appears:

# ```python
# user_input = "  42  "    # user typed with spaces
# number = int(user_input)

# # Which of these is wrong?
# print(user_input)         # 42         ← looks like a number!
# print(repr(user_input))   # '  42  '   ← ah, spaces! now you see it
# ```

# `repr()` reveals what is hidden. Spaces, newlines, invisible characters — all are shown:

where_live_class = Meditator
print(id(where_live_class)) # 49338252304 

### The Deep Insight — Identity vs Equality

# This is one of Python's most important philosophical distinctions:
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)        # True  ← same VALUE (equality)
print(a is b)        # False ← different OBJECTS (identity)
print(id(a) == id(b)) # False ← live at different addresses


# When you write `b = a`, you do not copy the list.
# You create a second name for the **same** object.

# Like giving a person two names — they are still one person.
# Change the person, and both names see the change. 🙏

### Why hash() Matters — The Dictionary's Secret

d = {}
d["name"] = "Gurudev"
print(d)
store_hash = hash
print(store_hash)
store_d_name = d["name"]
print(store_d_name)

s = {1,  2, 3}
print(2 in s)

### The Law of Immutability

# Only **immutable** objects can be hashed.

 
hash(42)           # ✅ integers are immutable
hash("Gurudev")    # ✅ strings are immutable
hash((1, 2, 3))    # ✅ tuples are immutable

# hash([1, 2, 3])    # ❌ TypeError: unhashable type: 'list'
# hash({"a": 1})     # ❌ TypeError: unhashable type: 'dict'
 

# **Why?**
# If you change an object after storing it in a dictionary, Python would never find it again.
# The hash would change — but the object would still be stored at the old location.
# This is why mutable objects refuse to be hashed: they are protecting you. 🛡️

text = "Om Namah Shivaya"

print(f"Value:    {repr(text)}")    # 'Om Namah Shivaya'   — what it truly is
print(f"Identity: {id(text)}")      # unique memory address — where it lives
print(f"Hash:     {hash(text)}")    # fingerprint           — its unchanging seal







