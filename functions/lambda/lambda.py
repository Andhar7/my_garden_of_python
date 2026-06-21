

# Multiple parameters
call_multi_in = lambda x, y, z: x * y / z
print(call_multi_in(4, 5, 6))

# With max()
words = ["fig", "watermelon", "plum", "pomegranate"]
check_words_lambda = max(words, key=lambda word: len(word))
print(check_words_lambda)
check_words_len = max(words, key=len)
print(check_words_len)

# With sorted()
people = [
    {"name": "Rohan",  "age": 19},
    {"name": "Devaki", "age": 65},
    {"name": "Arjuna", "age": 28},
]
check_by_age = sorted(people, key=lambda person: person["age"])
print(check_by_age)

# With map()
# `map()` applies a function to every element of a list:
numbers = [1, 2, 3, 4, 5]
check_by_numbers = list(map(lambda a: a * 23 / 108, numbers))
print(check_by_numbers)

# With filter()
# `filter()` keeps only the elements where the function returns `True`:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


## The Two Gardens Together 🌺
#`*args` and `lambda` often walk side by side:
def apply_to_all(*args, transform):
    return [transform(n) for n in args]

apply_to_all( 1, 2, 3, 4, 5, transform=lambda n: n ** 2)
























