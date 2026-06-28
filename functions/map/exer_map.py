

# **Exercise 1 — The Capitals**
#
# Convert every word to UPPERCASE using `map` and a built-in function (no lambda):
# ```python
words = ["peace", "love", "harmony", "light", "stillness"]
# ```
# Expected: `["PEACE", "LOVE", "HARMONY", "LIGHT", "STILLNESS"]`
capital_letters = list(map(str.upper, words))
print(capital_letters)

# **Exercise 2 — The Lengths**
#
# Find the length of every word using `map` and `len` (no lambda, no loop):
# ```python
words = ["om", "peace", "stillness", "fire", "gratitude"]
# ```
# Expected: `[2, 5, 9, 4, 9]`
length_of_words = list(map(len, words))
print(length_of_words)

# **Exercise 3 — The Converter**
#
# Write a proper `def` function called `celsius_to_fahrenheit` and use it with `map`:
# ```python
temps_c = [0, 10, 20, 37, 100]
# ```
# Formula: `F = C × 9/5 + 32`
#
# Expected: `[32.0, 50.0, 68.0, 98.6, 212.0]`
#
# *(Write the def function first, then pass it — without parentheses — to map.)* 🙏
def celsius_to_fahrenheit(C):
    return C * 9/5 + 32

result_of_converting = list(map(celsius_to_fahrenheit, temps_c))
print(result_of_converting)


# **Exercise 4 — The Parser**
#
# You receive data as strings from a form. Convert them to integers:
# ```python
raw = ["42", "7", "100", "13", "88"]
# ```
# Use `map` with a built-in to convert all at once.
# Then find their sum using `sum()`.
#
# Expected: integers `[42, 7, 100, 13, 88]`, sum `250`
convert_to_int = list(map(int, map(int, raw)))
print(convert_to_int)
result_of_sum = sum(convert_to_int)
print(f"sum is: {result_of_sum}")


# **Exercise 5 — The Pipeline**
#
# Starting from:
# ```python
numbers = [1, 2, 3, 4, 5]
# ```
# Using two `map` calls chained together (no intermediate variable):
# 1. Square each number
# 2. Convert each result to a string
#
# Expected: `["1", "4", "9", "16", "25"]`
#
# *(The inner map flows directly into the outer map — no list() in between.)*
# *(Only the final result needs list().)* 🌿
convert_to_str_and_square = list(map(str, map(lambda n: n ** 2, numbers)))
print(convert_to_str_and_square)





































