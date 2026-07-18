

# **Exercise 1 — The Precise Cuts**

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Using slicing only:
# 1. Get the weekdays (Mon–Fri)
# 2. Get the weekend (Sat, Sun)
# 3. Get every other day starting from Monday
# 4. Get the week in reverse order
print(week[:5])  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
print(week[-2:]) # ['Sat', 'Sun']
print(week[::2]) # ['Mon', 'Wed', 'Fri', 'Sun']
print(week[::-1])  # ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']

#**Exercise 2 — The Forgiving Test**
small = [1, 2, 3]
#
# Predict the result of each *before* running it, then verify:
# - `small[10:20]`
# - `small[-100:2]`
# - `small[1:]`
# - `small[100]` — what happens here, and why is it different from the slices above?
print(small[10:20]) # []
print(small[-100:2]) # [1,2]
print(small[1:]) # [2,3]
# print(small[100]) # list - IndexError: list index out of range


# **Exercise 3 — Slice Assignment**

letters = ["a", "b", "c", "d", "e"]

# Using slice assignment only (no `.insert`, no `.remove`):
# 1. Replace `"b"` and `"c"` with `"x"`, `"y"`, `"z"`
# 2. Delete `"d"` and `"e"` entirely
# 3. Insert `"NEW"` right after the first letter, without removing anything
#
# Print the list after each step.
letters[1:3] = ["x", "y", "z"]
print(letters)

letters[4:] = []
print(letters)

letters[-3:1] = ["NEW"]
print(letters)

# **Exercise 4 — Reusable Slices**
#
# Given a table of rows where each row is `[name, age, city]`, use named `slice`
# objects (not raw `1:2` written three times) to build a `names` list, an `ages`
# list, and a `cities` list from:

rows = {
    "name": "Andrej",
    "age": 34,
    "cities": "Zürich",
    "countries": "Swiss",
    "occupation": "production",
}

# *(Hint: you'll slice `row` inside a loop or comprehension using your named slice.)*
keys_to_extract = ['name', 'age', 'cities']
sliced_dict = {key: rows[key] for key in keys_to_extract}
print(sliced_dict)


# **Exercise 5 — Build Your Own Sliceable**
#
# Write a class `Playlist` that stores a list of song titles internally and
# implements `__getitem__` so that:
# - `playlist[2]` returns a single song (a string)
# - `playlist[1:4]` returns a new `Playlist` containing just those songs (not a
#   plain list)
#
# *(Hint: inside `__getitem__`, check `isinstance(key, slice)` to decide which
# kind of answer to build.)*
























