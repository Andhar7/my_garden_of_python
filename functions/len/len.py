
huge = list(range(1_000_000))
result_huge = len(huge)

print(result_huge) # 1000000
# len(huge)   # instant — reads a stored number, does not count

fruits = ["mango", "apple", "pear"]
for i in range(len(fruits)):
    print(i, fruits[i])

# This works — but `enumerate` is more elegant:
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Understanding `range(len(...))` shows you *why* `enumerate` was created — to free you from writing this pattern. 🌸

### len With the Other Flowers
words = ["om", "peace", "stillness", "harmony", "is"]
# How many words are longer than 4 characters?
count = sum(1 for word in words if len(word) > 4)
print(count)   # 3 (peace, stillness, harmony)

# The longest word:
longest = max(words, key=len)
print(longest)   # stillness


# Sort by length:
by_length = sorted(words, key=len)
print(by_length)   # ['om', 'is', 'peace', 'harmony', 'stillness']


# Python´s Data Model
class Garden:
    def __init__(self, flowers):
        self.flowers = flowers

    def __len__(self):
        return len(self.flowers)

my_garden = Garden(["rose", "lotus", "jasmine", "lily"])
print(len(my_garden))

# Before you `sum`, you may want to know the count.
# Before you `sort`, you may want to know if the list is empty.
# Before you `zip`, you may want to verify both lists have the same length.
# Before you `filter`, you may want to know how many will pass.







































