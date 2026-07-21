

### Exercise 1: Basic Summation

# **Task:** Predict output BEFORE running:
# What gets summed?
print(sum([10, 20, 30])) # 60

print(sum(range(1, 6))) # 15

print(sum([1, 2, 3], 100)) # 106

print(sum([], 50)) # 50

### Exercise 2: Financial Calculation

# **Task:** Calculate total expenses and remaining budget:
starting_budget = 5000
expenses = [1200, 350, 75, 425, 180]
total_spent_with_budget = sum(expenses, starting_budget)
total_spent = sum(expenses)
remaining_budget = starting_budget - total_spent
print(f"Starting budget: {starting_budget}")
print(f"Total spent including starting budget: {total_spent_with_budget}") # 7230
print(f"Total spent: {total_spent}") # 2230
print(f"Remaining budget: {remaining_budget}") # 2770

### Exercise 3: Conditional Summation

# **Task:** Sum only even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(n for n in numbers if n % 2 == 0)
print(f"Sum of even numbers: {even_sum}")  # Output: Sum of even numbers: 30

# Sum only numbers greater than 5
greater_than_five_sum = sum(n for n in numbers if n > 5)
print(f"Sum of numbers greater than 5: {greater_than_five_sum}")  # Output: Sum of numbers greater than 5: 40

### Exercise 4: Average Score Calculation

#**Task:** Calculate average from a list of scores:

test_scores = [85, 90, 78, 92, 88, 95]
average_score = sum(test_scores) / len(test_scores)
total_score = sum(test_scores)
print(f"Total score: {total_score}")  # Output: Total score: 528
print(f"Average score: {average_score:.2f}")  # Output: Average score: 88.00

# Bonus: count how many passed (>80)
passed_count = sum(1 for score in test_scores if score > 80)
print(f"Number of students who passed: {passed_count}")  # Output: Number of students who passed: 5

### Exercise 5: The Challenge — Matrix Sum

# **Task:** Sum all elements in a 2D matrix:

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
matrix_sum = sum(sum(row) for row in matrix)
print(f"Sum of all elements in the matrix: {matrix_sum}")  # Output: Sum of all elements in the matrix: 450

# Sum by row
row_sums = [sum(row) for row in matrix]
print(f"Sum of each row: {row_sums}")  # Output: Sum of each row: [60, 150, 240]

# Sum by column
column_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
print(f"Sum of each column: {column_sums}")  # Output: Sum of each column: [120, 150, 180]

