

# **Exercise 1 — Characters and Words**
#
# You have this sentence:
# ```python
sentence = "Om Namah Shivaya"
split_sentence = sentence.split()
# ```
# Find:
# - Total number of characters (including spaces)
# - Total number of characters (without spaces)
# - Total number of words
total_number_char = len(sentence)
print(f"Total number of characters (including spaces): {total_number_char}")

total_number_char_no_space = len(sentence.replace(" ", ""))
print(f"Total number of characters (without spaces): {total_number_char_no_space}")

total_number_words = len(split_sentence)
print(f"Total number of words: {total_number_words}")

# **Exercise 2 — The Password Gate**
#
# Write a function `is_valid_password(password)` that returns `True` if the password
# is at least 8 characters long, `False` otherwise.
#
# Test it:
# ```python
# is_valid_password("open")       # False
# is_valid_password("opengate1")  # True
# is_valid_password("12345678")   # True
def is_valid_password(password):

    if not password:
        raise ValueError("Please write the password")

    return len(password) >= 8

print(is_valid_password("open"))
print(is_valid_password("opengate1"))
print(is_valid_password("12345678"))

# **Exercise 3 — The Longest and Shortest**
#
# From this list of rivers, find the name with the most letters and the name with the fewest:
# ```python
rivers = ["Rhine", "Rhône", "Aare", "Inn", "Reuss", "Limmat"]
# ```
# *(Use `max` and `min` with `key=len`.)* 🌿
max_len = max(rivers, key=len)
print(f"Max letters in river: {max_len}")

min_len = min(rivers, key=len)
print(f"Min letters in river : {min_len}")


# **Exercise 4 — Same Length Check**
#
# Before zipping two lists together, check that they have the same length.
# If they do — zip and print the pairs. If they don't — print a warning.
#
# ```python
names  = ["Arjuna", "Devaki", "Rohan"]
scores = [88, 95, 72, 33]
# ```
#
# *(What happens if you test with a scores list that has only 2 items?)* 🌿
def same_length_check(lst_1, lst_2):
    if not lst_1:
        raise ValueError("The list_1 is empty")

    if not lst_2:
        raise ValueError("The list_2 is empty")

    if len(lst_1) == len(lst_2):
        for item_1, item_2 in zip(lst_1, lst_2):
            print(f"List_1 is : {item_1} and List_2 is : {item_2}")
    else:
        print(f"Length of list_1: {len(lst_1)} and length of list_2: {len(lst_2)} not equal!")


same_length_check(names, scores)

# **Exercise 5 — The Counter**
#
# Without using any loop, count how many words in this list have **exactly 4 letters**:
# ```python
words = ["love", "peace", "fire", "om", "soul", "path", "deep", "yoga"]
# ```
#
# *(Use `sum` + `len` together — no `for` loop, no `filter`.)* 🌿
count_exact = sum(1 for word in words if len(word) == 4)
print(f"How many words include 4 letters: {count_exact}")

