

# **Exercise 1 — The Shopping Basket**
#
# Find the total cost of these items:
# ```python
prices = [3.50, 12.00, 7.50, 1.20, 8.80, 4.00]
delivery = 5
# ```
# Also find the total **with** a delivery fee of 5.00 CHF using the `start=` parameter.
total_all_prices = sum(prices)
print(f"Total price: {total_all_prices} CHF")

total_price_with_delivery = sum(prices, delivery)
print(f"Price with delivery : {total_price_with_delivery} CHF")

# **Exercise 2 — Warm Days Only**
#
# Sum only the temperatures that are above zero:
# ```python
temperatures = [22, -5, 18, -3, 25, 14, -8, 0, 30]
# ```
# Use `filter` + `sum` together.
temp_only_warm = sum(filter(lambda t: t > 0, temperatures))
print(f"Total temperature above zero: {temp_only_warm} ")

# **Exercise 3 — Total Letters**
#
# Find the total number of letters across all words (not counting spaces):
# ```python
words = ["peace", "love", "harmony", "light", "stillness"]
# ```
# Use `sum` + `map` + `len` together.
total_number_of_letters = sum(map(lambda w: len(w), words))
print(f"Total number of letters in list is: {total_number_of_letters} letters")

# **Exercise 4 — Count the Passers**
#
# ```python
scores = [88, 45, 92, 61, 77, 95, 53, 70]
# ```
# Count how many scores are **60 or above** — using `sum` and a condition.
#
# *(No `filter`, no `for` loop — just `sum` and a truth check.)* 🌿
how_many_scores_above = sum(score >= 60 for score in scores)
print(f"Above 60 is : {how_many_scores_above} scores")

# **Exercise 5 — The Gauss Verification**
#
# Using one line only, verify that the sum of all numbers from 1 to 100 equals Gauss's formula:
#
# ```
# sum(1 + 2 + 3 + ... + 100)  ==  100 × 101 / 2
# ```
#
# Print `True` if they match, `False` if not.
gauss_verification = sum(range(1, 101)) == 100 * 101 // 2
print(gauss_verification)

# Count how many words have more than 4 letters
words = ["peace", "love", "harmony", "light", "stillness"]
count = sum(map(lambda w: len(w) > 4, words))
print(count)
count = sum(len(w) > 4 for w in words)

# sum(condition for item in list)  # counts what is true

# "peace"     → 5
# letters → True  ✅
# "love"      → 4
# letters → False ❌  (4 is not > 4)
# "harmony"   → 7
# letters → True  ✅
# "light"     → 5
# letters → True  ✅
# "stillness" → 9
# letters → True  ✅







