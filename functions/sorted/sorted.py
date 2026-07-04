import this

## The Inner World
def sorted_simple(items):
    result = list(items)         # make a fresh copy — never touch the original
    n = len(result)

    for i in range(1, n):
        current = result[i]      # pick up this card
        j = i - 1

        # walk left, sliding bigger cards rightward, until we find the right place
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current  # place the card in its right position

    return result

# Read this like the card player's quiet rhythm:

# 1. Start from the second item (the first is trivially "sorted" — alone)
# 2. Pick up the current item
# 3. Walk leftward through the already-sorted portion
# 4. Slide each card that is too big one step to the right — making room
# 5. When you find the right gap, place the card there
# 6. Move to the next card
# **Insertion sort — one card at a time:**

# ```
# Initial:   [4, 2, 7, 1, 5]
#             ↑
#           already sorted (one card)
#
# Round 1 — pick up 2:
#   Is 4 > 2? Yes → slide 4 right   [4, 4, 7, 1, 5]
#   No more cards left.  Place 2.   [2, 4, 7, 1, 5]
#
# Round 2 — pick up 7:
#   Is 4 > 7? No → place 7 here.   [2, 4, 7, 1, 5]
#
# Round 3 — pick up 1:
#   Is 7 > 1? Yes → slide 7        [2, 4, 7, 7, 5]
#   Is 4 > 1? Yes → slide 4        [2, 4, 4, 7, 5]
#   Is 2 > 1? Yes → slide 2        [2, 2, 4, 7, 5]
#   No more cards left.  Place 1.  [1, 2, 4, 7, 5]
#
# Round 4 — pick up 5:
#   Is 7 > 5? Yes → slide 7        [1, 2, 4, 7, 7]
#   Is 4 > 5? No → place 5 here.  [1, 2, 4, 5, 7]
#
# Done: [1, 2, 4, 5, 7] ✅
# ```

### Sorting Words by Length
words = ["fig", "pomegranate", "plum", "watermelon", "kiwi"]
check_length = sorted(words, key=len)
print(check_length)

### Sorting People by Age
people = [
    {"name": "Rohan",   "age": 19},
    {"name": "Devaki",  "age": 65},
    {"name": "Arjuna",  "age": 28},
    {"name": "Priya",   "age": 41},
]
by_age = sorted(people, key=lambda p: p["age"])
for person in by_age:
    print(f"{person['name']:10}  {person['age']}")


### Sorting Without Case
words = ["Mango", "apple", "Banana", "cherry"]
correct = sorted(words, key=str.lower)
print(correct)
# `key=str.lower` says: *before comparing, convert each word to lowercase.* The words themselves are returned as they are — only the comparison uses the lowercase version.

## Part 5 — The `reverse=` Parameter
scores = [78, 95, 61, 88, 72]
from_highest_to_lowest = sorted(scores, reverse=True)
print(from_highest_to_lowest)

by_age_desc = sorted(people, key=lambda p: p["age"], reverse=True)
print(by_age_desc)

## Part 6 — `sorted()` and `list.sort()` — Two Brothers
# result = numbers.sort()
# print(result)   # None  ← returns nothing!
# ```
#
# `list.sort()` returns `None`. It does not give you a new list. It rearranges the original in place.
# In general, prefer `sorted()`. It is safer — the original is never lost. 🙏

## Works on Any Iterable
# `sorted()` is generous. It accepts not only lists, but any sequence:
# A tuple
sorted((3, 1, 4, 1, 5))       # [1, 1, 3, 4, 5]

# A string — sorts the characters
sorted("peace")                 # ["a", "c", "e", "e", "p"]

# A set — which has no natural order
sorted({5, 2, 8, 1, 9})        # [1, 2, 5, 8, 9]
# ```
# It always returns a **list**, regardless of what you give it.














































