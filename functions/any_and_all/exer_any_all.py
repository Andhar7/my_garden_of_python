

# **Exercise 1 — Hot Day Alert**
#
# ```python
temperatures = [18, 21, 17, 25, 22, 31, 19]
# ```
# Is there any day above 30°? Print `True` or `False`.
day_above_30 = any(t > 30 for t in temperatures)
print(f"Is it exist day above 30°? : {day_above_30}")

# **Exercise 2 — Vowel Check**
#
# ```python
word = "rhythm"
# ```
# Does this word contain any vowel (`a e i o u`)?
# Print `True` or `False`.
#
# *(Hint: loop through the characters of the word with a generator expression.)* 🌿
vowel = "aeiou"
contain_vowel = any(v in vowel for v in word)
print(f"Is word contain vowel?: {contain_vowel}")

# **Exercise 3 — Any Negative?**
#
# ```python
numbers = [5, 12, 0, 8, 3, 7]
# ```
# Are there any negative numbers in this list?
# Print `True` or `False`.
# Then change one number to `-1` and check again.
is_negative_number = any(number < 0 for number in numbers)
print(is_negative_number)


# **Exercise 4 — The Missing Field**
#
# ```python
profile = {"name": "Gurudev", "city": "Zürich", "email": "", "age" : 0}
# ```
# Does any value in this dictionary evaluate as falsy (empty, zero, None)?
#
# *(Hint: use `.values()`)* 🌿
is_empty_any_value = any(not p for p in profile.values())
print(f"Is in profile some empty filed? : {is_empty_any_value}")

# **Exercise 5 — Any Failing Student?**
#
# ```python
students = [
    {"name": "Arjuna",  "score": 88},
    {"name": "Devaki",  "score": 95},
    {"name": "Rohan",   "score": 54},
    {"name": "Priya",   "score": 72},
]
# ```
# Is there any student with a score below 60?
# If yes, print their name. *(Hint: use a loop for the name, but `any` for the check.)* 🌿
def failed_student(students):

    if not students:
        raise ValueError("No data")

    if any(s["score"] < 60 for s in students):
        for s in students:
            if s["score"] < 60:
                print(f"Here name of failing student: {s['name']} with  scores : {s['score']}")


failed_student(students)

# ### Five Exercises for `all`
#
# **Exercise 6 — All Positive?**
#
# ```python
numbers = [5, 12, 0, 8, 3, 7]
# ```
# Are ALL numbers positive (greater than zero)?
# Print `True` or `False`. *(Watch: is 0 positive?)* 🌿
is_positive_all = all(v > 0 for v in numbers)
print(is_positive_all)

# **Exercise 7 — Proper Names**
#
# ```python
names = ["Arjuna", "devaki", "Rohan", "Priya"]
# ```
# Do ALL names start with a capital letter?
# Print `True` or `False`.
capital_letter = all(name[0].isupper() for name in names)
print(capital_letter)


# **Exercise 8 — All Adults?**
#
# ```python
ages = [22, 31, 18, 45, 17, 29]
# ```
# Are ALL ages 18 or above?
# Print `True` or `False`. Then find which age breaks the condition.
all_ages_above = all(age >= 18 for age in ages)
print(all_ages_above)

# **Exercise 9 — Valid Data**
#
# ```python
records = ["Zürich", "Basel", "", "Bern", "Geneva"]
# ```
# Are ALL records non-empty strings?
# Print `True` or `False`. *(Hint: use `len` or just truthiness of the string.)* 🌿
len_records = all(len(record) for record in records)
print(len_records)

# **Exercise 10 — The Combined Question**
#
# ```python
groups = [
    [85, 92, 78],
    [91, 88, 95],
    [72, 68, 74],
]
# ```
# Do ALL groups have at least ONE score above 80?
#
# *(Use `all` on the outside, `any` on the inside.)* 🌸
all_groups_at_least_one = all(any(score > 80 for score in scores) for scores in groups)
print(all_groups_at_least_one)













