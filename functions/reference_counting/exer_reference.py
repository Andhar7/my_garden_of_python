

# **Exercise 1 — Count the Cords**
#
# ```python
import sys

sacred = {"mantra": "Om Namah Shivaya"}
# ```
#
# Create 4 references to `sacred`. Print the count after each one.
# Then delete them one by one. Print the count after each deletion.
# Observe the lamp's cord count rising and falling.
print(f"Reference to sacred: {sys.getrefcount(sacred) - 1}") # 1

cord_one = sacred
cord_two = sacred
print(f"Connection with two cords: {sys.getrefcount(sacred) - 1}") # 3

del cord_one
print(f"Deleted first connection with first cord: {sys.getrefcount(sacred) - 1}") # 2

del cord_two
print(f"Deleted second connection with second cord: {sys.getrefcount(sacred) - 1}") # 1

# del sacred
# print(f"Deleted all sacred: {sys.getrefcount(sacred)}") # NameError: name 'sacred' is not defined

# **Exercise 2 — The del Experiment**
#
# ```python
a = [1, 2, 3]
b = a
c = a

print(f"All three: {sys.getrefcount(c) - 1}")  # 3

del a
print(f"After del a — check via b: {sys.getrefcount(b) - 1}")  # 2
# list still alive! b and c hold it

del b
print(f"After del b — check via c: {sys.getrefcount(c) - 1}")  # 1
# list still alive! only c holds it

del c
# count → 0 — list gone
# nothing remains to check through — this is correct!
print("After del c — the list has returned to silence. 🍂")


# **Exercise 3 — The Safe Function**
#
# Rewrite this dangerous function so it creates a fresh list each call:
#
# ```python
# Dangerous — mutable default:
def add_name(name, names=[]):
    names.append(name)
    return names

# Your task: rewrite it safely
def add_name_safe(name, names=None):
    if names is None:
        names = []
        names.append(name)
    return names

result_add_name1 = add_name("Andrej")
result_add_name2 = add_name("Tatjana")
result_add_name3 = add_name("Claude")

print(result_add_name1) # ['Andrej', 'Tatjana', 'Claude']
print(result_add_name2) # ['Andrej', 'Tatjana', 'Claude']
print(result_add_name3) # ['Andrej', 'Tatjana', 'Claude']

result_add_name_safe1 = add_name_safe("Andrej")
result_add_name_safe2 = add_name_safe("Tatjana")
result_add_name_safe3 = add_name_safe("Claude")

print(result_add_name_safe1) # ['Andrej']
print(result_add_name_safe2) # ['Tatjana']
print(result_add_name_safe3) # ['Claude']
# ```
#
# Test both versions. Show the difference. 🌿





