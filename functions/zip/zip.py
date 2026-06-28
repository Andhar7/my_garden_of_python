

names  = ["Arjuna", "Devaki", "Rohan"]
scores = [88,       95,       72     ]

def zip_solver():

    for name, score in zip(names, scores):
        print(f"Name: {name}, Age: {score}")

zip_solver()



## The Inner World
array_one = ["Swift", "Django", "TypeScript", "React"]
array_two = [1, 2, 3, 4, 5, 6, 7]
def zip_inner_world(*iterables):
    iterators = [iter(it) for it in iterables]

    while True:
        result = []
        for iterator in iterators:
            try:
                result.append(next(iterator))
            except StopIteration:
                return
        yield tuple(result)


for pair in zip_inner_world(array_two, array_one):
    print(pair)

# Show me *args
def show_me_args(*args):
    if not args:
        raise ValueError("Life is empty")
    print(args)
    print(len(args))
    print(args[0])
    print(args[1])
    print(type(args))

show_me_args(array_one, array_two, names, scores)


# Building of dictionaries
keys   = ["name",    "city",   "year"]
values = ["Gurudev", "Zürich", 2026  ]
def build_of_dict(lst_1, lst_2):

    if not lst_1:
        raise ValueError("The list_1 is empty")
    if not lst_2:
        raise ValueError("The list_2 is empty")

    dict_list = dict(zip(lst_1, lst_2))

    print(dict_list)

build_of_dict(keys, values)

# `zip` pairs each key with its value. `dict()` assembles the pairs. Elegant and clean.

# `zip` is not limited to two sequences. Any number may walk together:
names    = ["Arjuna", "Devaki", "Rohan"]
ages   = [88,       95,       72     ]
cities   = ["Mumbai", "Delhi",  "Pune" ]

def find_name_age_city(lst1, lst2, lst3):
    if not lst1:
        raise ValueError("The list_1 is empty")
    if not lst2:
        raise ValueError("The list_2 is empty")
    if not lst3:
        raise ValueError("The list_3 is empty")

    for name, age, city in zip(lst1, lst2, lst3):
        print(f"{name} is {age} old and live in {city} ")

    all_lists = names, ages, cities
    name, age, city = zip(*all_lists)
    print(name)
    print(age)
    print(city)

find_name_age_city(names, ages, cities)

### Example 3 — Comparing Two Lists Side by Side
predicted = [18, 22, 19, 25, 21]
actual    = [17, 23, 20, 24, 22]

def comparing_of_lists(lst1, lst2):

    if not lst1:
        raise ValueError("The list_1 is empty")
    if not lst2:
        raise ValueError("The list_2 is empty")

    for pred, real in zip(lst1, lst2):
        diff = real - pred
        sign = "+" if diff > 0 else ""
        print(f"Predictable is : {pred}°, actual is : {real}°, difference of temperature is : ({sign}{diff})°")

comparing_of_lists(predicted, actual)

## Part 6 — The Unzip Trick ✨

# `zip` can reverse itself.

# If you have a list of paired tuples, you can separate them back into individual sequences:
pairs = [("Arjuna", 88), ("Devaki", 95), ("Rohan", 72)]

name, age = zip(*pairs)
print(name)
print(age)

#If you need to use the pairs more than once, convert to a list first:
two_list_names_scores = list(zip(names, scores))
print(two_list_names_scores)
# Otherwise, use directly in a `for` loop — the most efficient and natural way. 🌿

































