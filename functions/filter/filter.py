

numbers = [-3, 7, -1, 0, 5, -2, 8]
negative_num = list(filter(lambda n: n > 0, numbers))
print(negative_num)

## The Inner World
def filter_inner(function, iterable):
    for item in iterable:
        if function(item):
            yield item


# None - use only Truthy
data = [0, "peace", "", None, 42, False, "love", [], "light"]
only_truthy = list(filter(None, data))
print(only_truthy)



# Valid temperature
readings = [22, 999, -3, -200, 37, 150, 18]

# The function name `is_valid_temperature` reads almost like a sentence.
# Clarity is always more valuable than brevity. 🙏
def is_valid_temperature(temp):
    return -50 <= temp <= 100

valid = list(filter(is_valid_temperature, readings))
print(valid)

## Filter and map Together
# A common pattern: **filter first, then transform the survivors.**
numbers_filter_map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1 — filter: keep only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers_filter_map))

# Step 2 — map: square each even number
square = list(map(lambda n: n ** 2, evens))
print(square)

# Or in one expression — the inner flows into the outer:
result_map_and_filter = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers_filter_map)))
print(result_map_and_filter)

# `filter` embodies Viveka in code.
#
# It does not judge harshly. It does not transform forcefully. It simply asks of each item one honest question:
#
# *Do you belong here?*
#
# And keeps only those who answer: *Yes.* 🙏



































