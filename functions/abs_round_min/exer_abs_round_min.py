

# **Exercise 1 — Distance**
#
# Given two price lists (before and after discount), find the absolute difference for each item:
# ```python
# Without guard — silent wrong answer
# zip([1, 2, 3], [1, 2])  # silently ignores 3
#
# # With guard — honest error, immediately visible
# if len(lst1) != len(lst2):
#     raise ValueError("Lists must be same length")
#
# A
# professional
# never
# lets
# bad
# data
# pass
# silently.He
# speaks. 💎

before = [100, 45, 230, 18, 75]
after  = [85,  45, 199, 20, 60]
# ```
# Print each difference using `abs`.
def find_difference(lst1, lst2):

    if not lst1:
        raise ValueError("The list1 is empty")

    if not lst2:
        raise ValueError("The list2 is empty")

    if len(lst1) != len(lst2):
        raise ValueError("Lists must be same length")

    # One
    # small
    # professional
    # note
    # for the future:
    #     if len(lst1) != len(lst2):
    #         raise ValueError("Lists must be same length")
    # zip
    # silently
    # stops
    # at
    # the
    # shorter
    # list.Worth
    # guarding.But
    # for this exercise — excellent.

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
# One
# small
# refinement — print
# name and age, not the
# full
# dict:
print(f"Youngest: {min_age['name']}, {min_age['age']}")
print(f"Oldest:   {max_age['name']}, {max_age['age']}")

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

def clamp(value, low, high):
    return max(low, min(high, value))

print(clamp(50, 0, 100))    # 50
print(clamp(-5, 0, 100))    # 0
print(clamp(150, 0, 100))   # 100

# **Exercise 5 — Temperature Report**
#
# ```python
temps = [18.4, 22.7, 15.1, 30.9, 19.3, 25.6, 12.8]
target = 20.0

print(f"Lowest:          {min(temps):.1f}°")
print(f"Highest:         {max(temps):.1f}°")
print(f"Average:         {round(sum(temps) / len(temps), 1):.1f}°")

closest = min(temps, key=lambda t: abs(t - target))
print(f"Closest to 20°:  {closest:.1f}°")

# ```
# Print a complete report:
# ```
# Lowest:   12.8°
# Highest:  30.9°
# Average:  20.7°   (rounded to 1 decimal)
# Closest to 20°:  19.3°  (use min with key=abs and a lambda)





























