import this

# **Exercise 1 — Ascending and Descending**
#
# Sort these mountain heights both ways:
# ```python
heights = [4480, 8849, 5895, 6961, 4807]
# Matterhorn, Everest, Kilimanjaro, Aconcagua, Mont Blanc
# ```
# Print them ascending (lowest first) and descending (highest first).
ascend_mount = sorted(heights)
desc_mount = sorted(heights, reverse=True)
print(f"From low to high: {ascend_mount}")
print(f"From high to low: {desc_mount}")

# **Exercise 2 — By Length, Then Alphabetically**
#
# You have a list of words:
# ```python
words = ["peace", "om", "love", "stillness", "joy", "harmony", "is", "light"]
# ```
# Sort them by **length** (shortest first).
#
# Then, as a bonus: what happens when words have the same length?
# *(Think about stability — which word comes first among equal-length words?)* 🌿
shortest = sorted(words, key=len)
print(f"Shortest words first: {shortest}")


# **Exercise 3 — The Leaderboard**
#
# Sort these students by score, highest first. Print their rank (1, 2, 3...) with their name and score:
# ```python
students = [
    {"name": "Arjuna",  "score": 88},
    {"name": "Devaki",  "score": 95},
    {"name": "Rohan",   "score": 72},
    {"name": "Priya",   "score": 91},
    {"name": "Kiran",   "score": 88},
]
# ```
# Expected:
# ```
# 1. Devaki  95
# 2. Priya   91
# 3. Arjuna  88
# 4. Kiran   88
# 5. Rohan   72
# ```
# *(Notice: Arjuna and Kiran both scored 88. Which comes first — and why?)* 🙏
sort_by_scores = sorted(students, key=lambda s: s["score"], reverse=True)[:5]
for num, s in enumerate(sort_by_scores, start=1):
    print(f"{num}. {s['name']}  {s['score']} ")

# **Exercise 4 — Ignoring Case**
#
# Sort this list of city names alphabetically, ignoring uppercase/lowercase:
# ```python
cities = ["zürich", "Basel", "bern", "Geneva", "lausanne", "Zug"]
# ```
# Expected (case-insensitive alphabetical):
# ```
# ['Basel', 'bern', 'Geneva', 'lausanne', 'Zug', 'zürich']
# ```
sort_list_of_city = sorted(cities, key=str.lower)
print(sort_list_of_city)

# **Exercise 5 — Sort a String**
#
# Sort the characters of this word alphabetically and join them back into a string:
# ```python
word = "harmony"
# ```
# Expected: `"ahmnory"`
#
# *(Hint: `sorted()` on a string returns a list of characters. How do you join a list of characters back into a string?)* 🌿
sort_in_characters = sorted(word)
join_word = "".join(sort_in_characters)
print(join_word)



