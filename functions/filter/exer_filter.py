
# **Exercise 1 — Keep the Positives**
#
# From this list, keep only the numbers greater than zero:
# ```python
numbers = [-3, 7, -1, 0, 5, -2, 8, -4, 3]
# ```
# Expected: `[7, 5, 8, 3]`
positive = list(filter(lambda n: n > 0, numbers))
print(positive)

# **Exercise 2 — The Long Words**
#
# Keep only the words with more than 4 characters:
# ```python
words = ["om", "peace", "love", "stillness", "joy", "harmony", "is"]
# ```
# Expected: `["peace", "stillness", "harmony"]`
only_4_character = list(filter(lambda word: len(word) > 4, words))
print(f"Here only 4 characters Words: {only_4_character}")


# **Exercise 3 — The Clean List**
#
# Remove all falsy values from this mixed list using `filter(None, ...)`:
# ```python
data = [0, "peace", "", None, 42, False, "love", [], "light"]
# ```
# Expected: `["peace", 42, "love", "light"]`
only_truthy = list(filter(None, data))
print(only_truthy)


# **Exercise 4 — The Adults**
#
# Keep only the people aged 18 or older:
# ```python
people = [
    {"name": "Arjuna", "age": 17},
    {"name": "Devaki", "age": 25},
    {"name": "Rohan",  "age": 14},
    {"name": "Priya",  "age": 32},
    {"name": "Kiran",  "age": 18},
]
# ```
# Print each adult's name and age.
adults = list(filter(lambda person: person["age"] >= 18, people))
for adult in adults:
    print(f"{adult['name']}: {adult['age']}")

# **Exercise 5 — The Full Pipeline**
#
# From `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
#
# 1. **filter** — keep only the **odd** numbers
# 2. **map** — square each one
#
# Write this as one expression — filter flowing into map.
#
# Expected: `[1, 9, 25, 49, 81]`
#
# *(The gardener selects the odd ones. The goldsmith squares each survivor.)* 🌸
numbers_map_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = list(filter(lambda n: n % 2 != 0, numbers_map_filter))
print(odd)

square = list(map(lambda n: n ** 2, numbers_map_filter))
print(square)

one_line_only = list(map(lambda n: n ** 2, filter(lambda n: n % 2 != 0, numbers_map_filter)))
print(one_line_only)


































