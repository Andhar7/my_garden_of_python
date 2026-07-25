

# **Exercise 1 — The Mirror**


items = [42, 3.14, "Zürich", True, None, [1, 2, 3], (4, 5)]

# For each item, print both its `str()` and its `repr()`.
# Notice where they are the **same** and where they **differ**.
# In one sentence next to each: *why* is it different (or the same)?
def check_items(items):
    for item in items:
        print(f"Check out by string: {str(item)} and by repr: {repr(item)} ")

check_items(items)

# **Exercise 2 — The Witness**

a = [10, 20, 30]
b = a
c = [10, 20, 30]

# Before running — predict with your mind:
# - Is `id(a) == id(b)`?
# - Is `id(a) == id(c)`?
# - Is `a == c`?
# - Is `a is c`?

# Then verify. Write down what each result teaches you.
print(a == c) # True
print(a is c) # False
print(id(a) == id(b)) # True
print(id(a) == id(c)) # False

# **Exercise 3 — The Seal**

words = ["Om", "Shanti", "Namaste", "Zürich", "Python"]

# For each word, print its `hash()`.
# Then change one letter in any word and print its hash again.
# Observe: how much does the hash change when the content changes even slightly?
def check_hash(words):
    
    for word in words:
        print(f"Hash for each word: {hash(word)}")
    
    change_list = []
    for word in words:
        change_list.append("m")
        print(f"Here changed hash: {hash(word)}")
        for change in change_list:
            print(f"Here changed hash: {hash(change)}")
        
        
check_hash(words)

# **Exercise 4 — The Mutation Trap**

def add_item(value, collection=[]):
    collection.append(value)
    return collection

result0 = add_item("zero")
result1 = add_item("first")
result2 = add_item("second")
result3 = add_item("third")

print(result0)
print(result1)
print(result2)
print(result3)
print(id(result0))
print(id(result1))
print(id(result2))
print(id(result3))


# Run this. The output will surprise you.

# Then use `id()` to understand WHY — are `result1`, `result2`, and `result3` the same object or different?

# *(This is one of Python's famous "gotchas" — understanding it through `id()` is the clearest path.)* 🙏



# **Exercise 5 — The `__repr__` Garden**

# Create a class called `Mantra` with two attributes: `text` (the words) and `repetitions` (how many times it is chanted).

# Give it a `__repr__` that returns something like:

# Mantra(text='Om Namah Shivaya', repetitions=108)

# Give it a `__str__` that returns something like:
# ```
# 🕉️  Om Namah Shivaya  ×108
# ```

# Create one Mantra and verify that `repr()` and `str()` each show their proper face. 🙏
class Mantra:
    
    def __init__(self, text, repetitions):
        self.text = text
        self.repetitions = repetitions
        
    def __repr__(self):
        return f"Repr return text: {self.text} and repeation: {self.repetitions}"
    
    def __str__(self):
        return f"Human string of text : {self.text} and repeation: {self.repetitions}"
    
result_mantra_class = Mantra(text='Om Namah Shivaya', repetitions=108)
print(repr(result_mantra_class))
print(str(result_mantra_class))
