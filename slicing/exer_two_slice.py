## 🎯 Exercises: Plant Your Understanding

### Exercise 1: Basic Slicing
# python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Get items at indices 2, 3, 4
# Answer:
get_items_one = numbers[2:5]
print(get_items_one) # [30, 40, 50]

# Get items at indices 0, 1
# Answer:
get_items_two = numbers[:2]
print(get_items_two)  # [10, 20]

# Get items at indices 6, 7, 8
# Answer:
get_items_three = numbers[6:9]
print(get_items_three) # [70, 80, 90]

### Exercise 2: Using -1 and Negative Indices
# ```python
word = "Python"
# Get the last 2 letters
# Answer:
last_two = word[-2:]  # on
print(last_two)

# Get everything except the last letter
# Answer:
get_all_except_last = word[:-1]  # Pytho
print(get_all_except_last)

# Get the first and last letter (using two operations)
# Answer:
last_two_only = word[0] + word[-1]
print(last_two_only)  # Pn

### Exercise 3: Step Values

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get every 2nd number
# Answer:
get_2th_number = numbers[::2]
print(get_2th_number)

# Get every 3rd number
# Answer:
get_3th_number = numbers[::3]
print(get_3th_number)

# Get the list reversed
# Answer:
list_reversed = numbers[::-1]
print(list_reversed)

### Exercise 4: Real-world Problem
# ```python
sentence = "The quick brown fox jumps over the lazy dog"

# Get the first word
# Answer:
split_first = sentence.split()
print(split_first)
get_the_first_word = split_first[0]
print(get_the_first_word)

# Get every word at an even index (hint: split first!)
# Answer:
even_index = split_first[::2]
print(even_index)

# Reverse the entire sentence, word by word
# Answer:
reverse_all = split_first[::-1]
print(reverse_all)


### Exercise 5: The Slice Object
# ```python
# Create a slice object that gets items 2 to 8 with step 2
# Then apply it to: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Answer:
class SliceObject:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.data[key]
        else:
            return self.data[key]


gets_items = SliceObject([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(gets_items[2:8:2])

# Right approach:
my_slice = slice(2, 8, 2)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[my_slice])
