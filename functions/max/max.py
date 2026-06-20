a = 21
b = 23


def max_simple(a, b):
    if a > b:
        return a
    return b


result_max = max_simple(a, b)
print(result_max)


def max_with_largest(numbers):

    if not numbers:
        raise ValueError("Fixed errors by no numbers")

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

largest_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_largest_list = max_with_largest(largest_list)
print(result_largest_list)


words = ("Michael", "David", "Bob", "Tracy")

def max_longest_word(words, key=len):

    longest_words = words[0]

    for word in words:
        if len(word) > len(longest_words):
            longest_words = word
    return longest_words

print(max_longest_word(words, key=len))

longest_words_list = max(words, key=len)
print(longest_words_list)

people = [
    {"name": "Arjuna",  "age": 28},
    {"name": "Devaki",  "age": 65},
    {"name": "Rohan",   "age": 19},
]

result_people = max(people, key=lambda p: p["age"])
print(result_people)































