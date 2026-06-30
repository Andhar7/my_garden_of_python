
prices = [12.5, 8.0, 22.5, 5.0, 14.0]

def old_way(lst):

    if not lst:
        raise ValueError("Emtpy list")

    total = 0
    for price in prices:
        total += price
    return total

print(old_way(prices))

# New way
total = sum(prices)
print(f"Total in new way: {total}")

## Part 2 — The Inner World
def sum_inner_world(iterable, start=0):

    total = start

    for item in iterable:
        total += item
    return total


## Part 4 — The `start=` Parameter
prices   = [12.5, 8.0, 22.5, 5.0]
delivery = 4.5   # delivery fee added at the start

price_delivery = sum(prices, delivery)
print(price_delivery)

existing_total = 100
new_items      = [15, 25, 10]

together = sum(new_items, existing_total)
print(together)


# Sum with range
# `range(1, 101)` produces 1, 2, 3, ... 100.
# `sum(...)` gathers them all.

total = sum(range(1, 101))
print(total)


## Part 6 — sum With the Other Flowers
### sum + map — Total of Transformed Values
words = ["peace", "love", "harmony", "light"]

total_letters = sum(map(len, words))
print(total_letters)

### sum + filter — Total of Selected Values
temperatures = [22, -5, 18, -3, 25, 14, -8]
total_warmth = sum(filter(lambda t: t > 0, temperatures))
print(total_warmth)

## Part 7 — What sum Does NOT Do
## Part 7 — What sum Does NOT Do

# `sum` is for numbers. For strings, it does not work:
#
# ```python
# words = ["peace", "love", "light"]
# sum(words)   # TypeError ❌
# ```
#
# To join strings, use `"".join()`:
#
# ```python
# "".join(words)        # "peacelovelight"
# " ".join(words)       # "peace love light"
# ```
#
# `sum` gathers numbers. `join` gathers strings. Each has its own work. 🙏

## Part 8 — A Beautiful Pattern: Counting Truths
# A clever use of `sum` — counting how many items satisfy a condition:
scores = [88, 45, 92, 61, 77, 95, 53]

count = sum(map(lambda s: s > 75, scores))
print(count)

# This is synthesis — the counterpart to analysis.
#
# We analyse when we break one thing into many parts.
# We synthesise when we gather many parts into one understanding.
#
# `sum` is synthesis. 🙏



























