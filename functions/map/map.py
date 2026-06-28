

numbers = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda n: n * 2, numbers))
print(doubled_list)
# *"Apply this transformation to every item, and give me the results."*
# One idea. One line. 🌿

## Part 2 — The Inner World
def map_numbers(function, iterable):

    for item in iterable:
        yield function(item)

def double(n):
    return n * 2

result = list(map_numbers(double, numbers))
print(result)

## Part 3 — A Walk Through, Step by Step

# ```python
# numbers = [1, 2, 3, 4, 5]
# result  = list(map(lambda n: n * 2, numbers))
# ```
#
# **What happens inside:**
#
# ```
# function = lambda n: n * 2
# iterable = [1, 2, 3, 4, 5]
#
# ── Step 1 ─────────────────────────────
#   item = 1
#   function(1) = 1 * 2 = 2
#   yield 2
#
# ── Step 2 ─────────────────────────────
#   item = 2
#   function(2) = 2 * 2 = 4
#   yield 4
#
# ── Step 3 ─────────────────────────────
#   item = 3
#   function(3) = 3 * 2 = 6
#   yield 6
#
# ── Step 4 ─────────────────────────────
#   item = 4
#   function(4) = 4 * 2 = 8
#   yield 8
#
# ── Step 5 ─────────────────────────────
#   item = 5
#   function(5) = 5 * 2 = 10
#   yield 10
#
# No more items. list() collects all: [2, 4, 6, 8, 10]
# ```
#
# The goldsmith touched each piece once. Each emerged transformed.
#
# ---

### Way 3 — A Built-in Function (elegant and direct)

# Python's built-in functions are also functions. You can pass them directly:
#
# ```python
words = ["peace", "love", "harmony"]
upper = list(map(str.upper, words))
print(upper)
# ["PEACE", "LOVE", "HARMONY"]
# ```
#
# ```python
lengths = list(map(len, words))
print(lengths)
# [5, 4, 7]
# ```
#
# ```python
string_numbers = ["42", "7", "100"]
integers = list(map(int, string_numbers))
print(integers)
# [42, 7, 100]
# ```
#
# `str.upper`, `len`, `int` — these are all functions. Map welcomes them all.
#
# This is one of map's most elegant uses: applying a well-known transformation to every item without writing a single lambda. 🌿
#
# ---


# This is economical. If you have one million items and only need the first ten, `map` does not calculate all one million. It calculates only what you ask for.
## The Original List Is Never Changed

big_numbers = range(14)
first_twelve = list(map(lambda n: n * 1, big_numbers))[:12]
print(first_twelve)
# The goldsmith's original material is never consumed. He works from a copy of the idea.
# This is purity. The source remains clean. The transformation is a new creation. 🌸

## Part 7 — map With Two Sequences
# Just as `zip` can walk two sequences side by side, `map` can transform two sequences together:
prices    = [10.0, 25.0, 8.5, 30.0]
discounts = [0.1,  0.2,  0.0, 0.15]   # 10%, 20%, 0%, 15%

final = list(map(lambda price, disc: price * (1 - disc), prices, discounts))
print(final)
# Map takes one item from each sequence at the same step and passes both to the function.

## Part 8 — Chaining Maps
# The result of one `map` can flow directly into another:
#
# ```python
numbers = [1, 2, 3, 4, 5]

result = list(
    map(str,                    # Step 2: convert each to a string
        map(lambda n: n ** 2,   # Step 1: square each number
            numbers))
)
#
print(result)   # ["1", "4", "9", "16", "25"]
# ```
#
# Read from inside out:
# 1. `map(lambda n: n ** 2, numbers)` → squares: 1, 4, 9, 16, 25
# 2. `map(str, ...)` → strings: "1", "4", "9", "16", "25"








































