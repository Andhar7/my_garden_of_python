
# **Exercise 1 — The Warmest Day**
#
# Write your **own** max function (not Python's built-in) and use it to find the warmest temperature:
temperatures = [18, 22, 19, 25, 21, 17, 23]

def max_temperature(temperatures):

    warmest = temperatures[0]

    for temp in temperatures:
        if temp > warmest:
            warmest = temp
    return warmest

print(f"The warmest day reached: {max_temperature(temperatures)}° ")

#**Exercise 2 — The Eldest**
#You have a list of people:
# Using `max()` with `key=`, find and print the eldest person's name and age.
people = [
    {"name": "Arjuna",  "age": 28},
    {"name": "Devaki",  "age": 65},
    {"name": "Rohan",   "age": 19},
    {"name": "Priya",   "age": 41},
]

eldest_people = max(people, key=lambda p: p["age"])
print(eldest_people)

# **Exercise 3 — The Longest Word**

# Find the longest word in this sentence (use `max()` with `key=len`):
# ```python
sentence = "The mountain stands in peaceful silence"
solution = sentence.split()
# ```
# Print: `Longest word: "peaceful" (8 letters)`

longest_with_max = max(solution, key=len)
print(f"The longest  word: {longest_with_max} {len(longest_with_max)} letters")

# **Exercise 4 — The Best Branch**
#
# Find which branch had the highest monthly sales:
# ```python
branches = [
    {"name": "Zürich",   "monthly_sales": 45000},
    {"name": "Basel",    "monthly_sales": 38000},
    {"name": "Bern",     "monthly_sales": 52000},
    {"name": "Geneva",   "monthly_sales": 47000},
]
# ```
# Print: `Best branch: Bern with 52000 CHF`
best_branch = max(branches, key=lambda b: b["monthly_sales"]  )
print(f"The branch: {best_branch['name']} {best_branch['monthly_sales']} CHF")

# **Exercise 5 — The Complete max**
#
# Write a `universal_max` function that:
# - Accepts **either** a list `universal_max([4, 7, 2])` **or** separate numbers `universal_max(4, 7, 2)`
# - Raises `ValueError` for empty input
# - Returns the correct maximum in both cases
#
# *(Hint: combine what you know about `*args` and the inner world of max.)* 🌿
def universal_max(*args):

    if len(args) == 1 and isinstance(args[0], list):
        items = args[0]
    else:
        items = args

    if not items:
        raise ValueError("No arguments provided")

    longest = items[0]

    for n in items:
        if n > longest:
            longest = n
    return longest


print(universal_max(4, 7, 2))
print(universal_max(4, 7, 2, 9))     # 9  — separate numbers
print(universal_max([4, 7, 2, 9]))   # 9  — a list
print(universal_max(42))             # 42 — one number









































