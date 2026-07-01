

# **Exercise 1 — Distance**
#
# Given two price lists (before and after discount), find the absolute difference for each item:
# ```python
before = [100, 45, 230, 18, 75]
after  = [85,  45, 199, 20, 60]
# ```
# Print each difference using `abs`.
def find_difference(lst1, lst2):

    if not lst1:
        raise ValueError("The list1 is empty")

    if not lst2:
        raise ValueError("The list2 is empty")

    for b, a in zip(lst1, lst2):
        print(f"The difference between {b} and {a} is : {abs(b - a)}")

find_difference(before, after)

# **Exercise 2 — The Banker**
#
# Before running, predict the output of each:
# ```python
# round(0.5)    round(1.5)    round(2.5)    round(3.5)
# round(1.25, 1)    round(1.35, 1)    round(1.45, 1)
# ```
# Then run and check. Were you surprised? 🌿
print(round(0.5)) # My predict is: 0
print(round(1.5)) # My predict is: 1  -> Surprised!!! -> out 2
print(round(2.5)) # My predict is: 2
print(round(3.5)) # My predict is: 3  -> Surprised!!! -> out 4
print(round(1.25, 1)) # My predict is: 1.2
print(round(1.35, 1)) # My predict is: 1.3 -> Surprised!!! -> out 1.4
print(round(1.45, 1)) # My predict is: 1.4

# **Exercise 3 — The Youngest**
#
# ```python
participants = [
    {"name": "Arjuna",  "age": 28},
    {"name": "Devaki",  "age": 65},
    {"name": "Rohan",   "age": 19},
    {"name": "Priya",   "age": 41},
    {"name": "Kiran",   "age": 22},
]
# ```
# Find the youngest and the oldest participant using `min` and `max` with `key=`.
min_age = min(participants, key=lambda p: p["age"])
print(min_age)
max_age = max(participants, key=lambda p: p["age"])
print(max_age)

# **Exercise 4 — The Clamp**
#
# Write a function `clamp(value, low, high)` that:
# - Returns `value` if it is between `low` and `high`
# - Returns `low` if `value` is below `low`
# - Returns `high` if `value` is above `high`
#
# ```python
# clamp(50, 0, 100)    # 50
# clamp(-5, 0, 100)    # 0
# clamp(150, 0, 100)   # 100
# ```
# *(Use `max` and `min` — no `if` statements needed.)* 🌿







