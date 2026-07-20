
### Exercise 1: Understanding stop is Exclusive
for i in range(1, 4):
    print(i) # Output: 1, 2, 3

for i in range(10, 15):
    print(i) # Output: 10, 11, 12, 13, 14

output_of_range = range(5, 10)
print(list(output_of_range)) # Output: [5, 6, 7, 8, 9]

### Exercise 2: Stepping Patterns
for i in range(0, 12, 2):
    print(f"{i}", end=" ")   # Output: 0, 2, 4, 6, 8, 10

for i in range(10, -1, -2):
    print(f"{i}", end=" ")   # Output: 10, 8, 6, 4, 2, 0
    
for i in range(1, 14, 3):
    print(f"{i}", end=" ")   # Output: 1, 4, 7, 10, 13

### Exercise 3: List Reversal

# **Task:** Create a list, then print it backwards using range():
 
animals = ["cat", "dog", "bird", "fish", "snake"]

# Print backwards using range()
for i in range(len(animals) - 1, -1, -1):
    print(animals[i])  # Output: snake, fish, bird, dog, cat

### Exercise 4: Even and Odd Numbers
# **Task:** Generate:
# 1. All even numbers from 0 to 20
# 2. All odd numbers from 1 to 20
for i in range(0, 21, 2):  # Even numbers from 0 to 20
    print(f"{i}", end=" ")  # Output: Even: 0, 2, 4, ..., 20

for i in range(1, 21, 2):
    print(f"{i}", end=" ")   # Output: Odd: 1, 3, 5, ..., 19

### Exercise 5: The Challenge — Create a Multiplication Table

# **Task:** Print a 5×5 multiplication table:
# ```
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12 15
# 4  8  12 16 20
# 5  10 15 20 25
# ``` 

for i in range(1, 6): 
    for j in range(1, 6):   
        print(f"{i * j:<2}", end=" ")   
    print()   
    



