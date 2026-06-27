

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


