
# **Exercise 1 — Sort by Last Letter**

# Sort this list of words by their **last character** (using `sorted` with a `lambda`):
# ```python
words = ["banana", "fig", "mango", "plum", "kiwi"]
# ```
# Expected: `['banana', 'mango', 'fig', 'kiwi', 'plum']`
# *(a, o, g, i, m — sorted alphabetically by last letter)*
check_last_word = sorted(words, key=lambda w: w[-1])
print(check_last_word)
# ['banana', 'fig', 'kiwi', 'plum', 'mango']

# **Exercise 2 — Keep the Long**
#
# From this list, keep only words with **more than 4 characters** (using `filter` + `lambda`):
# ```python
words = ["om", "peace", "love", "stillness", "joy", "harmony"]
# ```
# Expected: `['peace', 'stillness', 'harmony']`
use_filter = list(filter(lambda w: len(w) > 4, words))
print(use_filter)


# **Exercise 3 — Celsius to Fahrenheit**
#
# Convert these temperatures from Celsius to Fahrenheit using `map` + `lambda`:
# ```python
temps_c = [0, 20, 37, 100]
# ```
# Formula: `F = C × 9/5 + 32`
#
# Expected: `[32.0, 68.0, 98.6, 212.0]`
convert = list(map(lambda t: t * 9/5 + 32, temps_c))
print(convert)

#
# **Exercise 4 — Sort the Market**
#
# Sort these products by price, lowest first (using `sorted` + `lambda` on a dict key):
# ```python
products = [
    {"name": "tea",    "price": 3.5},
    {"name": "book",   "price": 12.0},
    {"name": "candle", "price": 7.5},
    {"name": "honey",  "price": 5.0},
]
# ```
sorted_by_price = sorted(products, key=lambda p: p["price"])
print(sorted_by_price)

# **Exercise 5 — The Pipeline**
#
# In **one line**, using `filter` and `map` with lambdas:
#
# From `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
# 1. Keep only numbers divisible by 3
# 2. Square each of them
#
# Expected: `[9, 36, 81]`
#
# *(Think of filter first, then map — reading left to right, like a pipeline.)* 🌿
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(map(lambda n: n ** 2, filter(lambda n: n % 3 == 0, numbers)))
print(filtered_numbers)






























