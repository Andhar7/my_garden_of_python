

temperatures = [18, 21, 17, 31, 22, 19]
is_hot_day = any(t > 30 for t in temperatures)
print(is_hot_day)

# Inner World of any ...
def any_world(iterable):
    for item in iterable:
        if item:
            return True
    return False

# Inner World of all ...
def all_world(iterable):
    for item in iterable:
        if not item:
            return False
    return True

print(any_world(temperatures))
print(all_world(temperatures))

scores  = [88, 72, 91, 65, 77, 45]
words   = ["Peace", "Love", "Harmony", "light"]

calculate_any = any(score > 90 for score in scores)
print(f"Found more then 90? : {calculate_any}")
lowercase_words_any = any(word.islower() for word in words)
print(f"Found lowercase ? : {lowercase_words_any}")

calculate_all = all(score >= 60 for score in scores)
print(f"Found score more then 60?: {calculate_all} ")
uppercase_words_all = all(word.isupper() for word in words)
print(f"Found upper word? : {uppercase_words_all}")


## any and all Together
students = {
    "Arjuna": [88, 92, 85, 91],
    "Devaki": [95, 98, 91, 99],
    "Rohan":  [72, 68, 75, 70],
}
# Does any student have ALL scores above 80?
found = any(all(s > 80 for s in scores) for scores in students.values())
print(found)

all_have_one = all(any(s > 90 for s in scores) for scores in students.values())
print(all_have_one)   # False — Rohan has no score above 90
























