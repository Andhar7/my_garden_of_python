# **Exercise 1 — The Morning List (start from 1)**
practices = ["Breathing", "Walking", "Chanting", "Silence", "Gratitude"]


# Print them numbered from 1, as a teacher writes on a blackboard:
def on_blackboard_list(lst):
    if not lst:
        raise ValueError("The List is an empty")

    for number, practice in enumerate(lst, start=1):
        print(f"{number}. {practice}")


on_blackboard_list(practices)

# **Exercise 2 — The Broken Sensor**

# A temperature sensor recorded these hourly readings:
# ```python
hourly_temps = [20, 22, 21, 999, 23, 22, -999, 21]


# ```
# Values above `100` or below `-50` are sensor errors.

# Find and print the **index and value** of the **first** erroneous reading.
def find_hourly_temps_errors(lst):
    if not lst:
        raise ValueError("List an empty")

    for index, temp in enumerate(lst):
        if temp > 100 or temp < -50:
            print(f"First error at index: {index} - temp: {temp}")
            return


find_hourly_temps_errors(hourly_temps)

# **Exercise 3 — The Corrector**

# Some words were typed in ALL CAPS by mistake:
# ```python
words = ["peace", "LOVE", "harmony", "LIGHT", "stillness"]


# ```
# Using `enumerate`, correct the list **in place** — every word should become lowercase.
# Then print the corrected list.
def correct_word(lst):
    if not lst:
        raise ValueError("The list empty")

    for place, word in enumerate(lst):
        lst[place] = word.lower()

    return lst


print(correct_word(words))

# **Exercise 4 — Pair the Gardens (no `zip` allowed)**
#
# Using only `enumerate` — not `zip` — pair each fruit with its colour:
# ```python
fruits = ["mango", "apple", "grape", "orange"]
colours = ["yellow", "red", "purple", "orange"]
# ```
# Print:
# ```
# mango is yellow
# apple is red
# grape is purple
# orange is orange
# ```
for i, fruit in enumerate(fruits):
    print(f"{fruit} is {colours[i]}")

# **Exercise 5 — The Scoreboard**
#
# ```python
scores = [78, 95, 88, 95, 72, 95, 61]


# ```
# Find all **positions** where the maximum score appears and print:
# ```
# Maximum score: 95
# Found at positions: [1, 3, 5]
# ```
# *(Use `max()` to find the maximum, then `enumerate` to find its positions.)* 🌿
def find_max_and_enumerate(lst):
    if not lst:
        raise ValueError("The list is empty")

    list_of_max_position = []
    max_nums = max(lst)

    for i, score in enumerate(lst):
        if score == max_nums:
            list_of_max_position.append(i)

    return max_nums, list_of_max_position


max_score, positions = find_max_and_enumerate(scores)
print(f"Maximum score: {max_score}")
print(f"Found at positions: {positions}")
