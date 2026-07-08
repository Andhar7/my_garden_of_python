

print(str(0))           # 0
print(str(True))       # "True"
print(str(None))       # "None"
print(int("100"))      # 100
print(int(3.7))        # 3
print(int(False))      # 0
print(float("3.14"))   # 3.14
print(float(42))       # 42.0
print(float("inf"))    # inf
print(bool(0))         # False
print(bool(""))        # False
print(bool("False"))   # True

# **Exercise 2 — The Input Calculator**
#
# Write a program that:
# 1. Asks for two numbers using `input()`
# 2. Converts them to floats
# 3. Prints their sum, difference, product, and division
def input_calculator():

    first_num = float(input("Please write first number : "))
    second_num = float(input("Please write second number : "))

    total = first_num + second_num
    difference = first_num - second_num
    product = first_num * second_num
    division = first_num / second_num

    print(f"Here the total: {total}")
    print(f"Here is difference: {difference}")
    print(f"Here is product: {product}")
    print(f"Here is division: {division}")

#input_calculator()



# **Exercise 3 — The Safe Converter**
#
# Write `safe_int(text)` that:
# - Returns `int(text)` if text is a valid integer string
# - Returns `None` if it is not (using try/except)
#
# ```python
# safe_int("42")      # 42
# safe_int("3.14")    # None
# safe_int("peace")   # None
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_int("42"))
print(safe_int("3.14"))
print(safe_int("peace"))

# **Exercise 4 — The Truthiness Map**
#
# Create a list of at least 8 values of different types. Loop through and
# print each value and its boolean truth: `"peace" → True` / `0 → False`.
list_of_types = ["peace", 0, True, 3.33, None, "False", [], -1]
for each in list_of_types:
    print(f"Convert value: {each} to Bool({each}): {bool(each)}")


# **Exercise 5 — The Chain**
#
# Without using `int("3.14")` directly (which fails), convert the string `"3.14"`
# to the integer `3` using two conversion steps.
# Then write the same chain for `"-7.8"` → `-7`. 🌿
def convert_string_to_int(text):

    convert_to_float = float(text)
    result = int(convert_to_float)
    return result

test_one = convert_string_to_int("3.14")
test_two = convert_string_to_int("-7.8")
print(f"We convert string to integer: {test_one}")
print(f"We convert string to integer: {test_two}")

























