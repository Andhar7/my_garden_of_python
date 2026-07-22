### Exercise 1: Understanding any() and all()

# **Task:** Predict output BEFORE running:

# What do these return?
print(any([False, False, False])) # False
print(all([True, True, True])) # True
print(any([])) # False
print(all([])) # True
print(any([0, 0, 5])) # True
print(all([1, 2, 0])) # False

### Exercise 2: Conditional Checks

# **Task:** Check conditions using any() and all():

numbers = [2, 4, 6, 8, 10]
# Are ALL numbers even?
def find_numbers(num):
    all_even = all(n % 2 == 0 for n in numbers)
    any_odd = any(n % 2 != 0 for n in numbers)
    if all_even:
        print(f"All even : {all_even} in  {numbers}")
        return numbers
    if any_odd:
        print(f"Any odd numbers: {any_odd}")
    return numbers 


find_numbers(numbers)


