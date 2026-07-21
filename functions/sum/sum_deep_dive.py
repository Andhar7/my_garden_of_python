

print(sum([1, 2, 3, 4, 5], 6))  # Output: 21

print(sum([1, 2, 3, 4, 5], - 6))  # Output: 9

print(sum([1, 2, 3, 4, 5], * [12]))  # Output: 27

print(sum([1, 2, 3, 4, 5], * [-12]))  # Output: -6

print(sum([1, 2, 3, 4, 5], * [12]))  # Output: 40

print(sum([1, 2, 3, 4, 5], * [-12]))  # Output: -15
 

expenses = [15.51, 23.45, 9.99, 12.75, 18.20]
total_spent = sum(expenses)
print(f"Total spent: ${total_spent:.2f}")  # Output: Total spent: $79.90

# monthly budget with starting balance
starting_balance = 10000.00
monthly_expenses = [250.00, 150.00, 300.00, 200.00, 100.00]
remaining_balance = starting_balance - sum(monthly_expenses)
print(f"Remaining balance after expenses: ${remaining_balance:.2f}")  # Output: Remaining balance after expenses: $9000.00

# Better way - use start parameter negatively
remaining = sum([-150, -200, -100, -50], 1000)
print(f"Remaining balance after expenses: ${remaining:.2f}")  # Output: Remaining balance after expenses: $500.00

# Calculate average
scores = [85, 90, 78, 92, 88]
average_score = sum(scores) / len(scores)
print(sum(scores))  # Output: 433
print(len(scores))  # Output: 5
print(f"Average score: {average_score:.2f}")  # Output: Average score: 86.60

# Weighted average (test vs homework)
test_scores = [80, 85]
homework_scores = [90, 95]
total = sum(test_scores) * 0.7 + sum(homework_scores) * 0.3
print(f"Weighted score: {total:.2f}")  # Output: Weighted score: 85.50

# Count True values (True = 1, False = 0)
results = [True, False, True, True, False]
correct = sum(results)
print(f"Number of correct answers: {correct}/5")    # Output: Number of correct answers: 3

# Count if condition is met (clever!)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for n in numbers if n % 2 == 0)
print(f"Number of even numbers: {even_count}")  # Output: Number of even numbers: 5

# Flatten and sum nested structure
sales_by_day = [
    [100, 150, 120],  # Monday sales
    [200, 180, 210],  # Tuesday sales
    [90, 110, 100]    # Wednesday sales
]
total_sales = sum(sum(day) for day in sales_by_day)
print(f"Total sales for the week: ${total_sales:.2f}")  # Output: Total sales for the week: $1260.00

# Or using nested sum
total = sum([sum(day) for day in sales_by_day])
print(f"Total nested: ${total:.2f}")  # Output: Total nested: $1260.00

# Use case: adding to existing total
current_total = 500
new_sales = [50, 75, 100]
updated_total = sum(new_sales, current_total)
print(f"Updated total sales: ${updated_total:.2f}")  # Output: Updated total sales: $725.00

# Sum only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(n for n in numbers if n % 2 == 0)
print(f"Sum of even numbers: {even_sum}")  # Output: Sum of even numbers: 30

# Sum numbers above threshold
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 5
above_threshold_sum = sum(n for n in numbers if n > threshold)
print(f"Sum of numbers above {threshold}: {above_threshold_sum}")  # Output: Sum of numbers above 5: 40

# Sum squares of numbers
numbers = [1, 2, 3, 4, 5]
squares_sum = sum(n**2 for n in numbers)
print(f"Sum of squares: {squares_sum}")  # Output: Sum of squares: 55

# Sum string lengths
words = ["swift", "kotlin", "python", "django"]
total_length = sum(len(word) for word in words)
print(f"Total length of words: {total_length}")  # Output: Total length of words: 16

# Sum absolute values
numbers = [-5, 3, -8, 2, -1]
absolute_sum = sum(abs(n) for n in numbers)
print(f"Sum of absolute values: {absolute_sum}")  # Output: Sum of absolute values: 19

# Sum all elements in 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Method 1: nested loop
total_matrix_sum = sum(sum(row) for row in matrix)
print(f"Total sum of matrix elements: {total_matrix_sum}")  # Output: Total sum of matrix elements: 45

# Method 2: flatten first
import itertools
total = sum(itertools.chain.from_iterable(matrix))
print(f"Total sum of matrix elements (flattened): {total}")  # Output: Total sum of matrix elements (flattened): 45

# Track cumulative total
daily_sales = [100, 150, 120, 200, 180]
running_total = 0

for sale in daily_sales:
    running_total += sale
    print(f"Running total after sale of ${sale}: ${running_total}")
    
# More Pythonic way:
import itertools
running_totals = list(itertools.accumulate(daily_sales))
print(f"Running totals in more Pythonic way: {running_totals}")  # Output: Running totals: [100, 250, 370, 570, 750]

starting_balance = 1000
transactions = [100, 50, 75]
result = sum(transactions, starting_balance)
print(f"Final balance: ${result}")  # Output: Final balance: $1225

numbers_and_strings = [1, 2, "three", 4]
numbers = [n for n in numbers_and_strings if isinstance(n, (int, float))]
total = sum(numbers)
print(f"Total of numeric values: {total}")  # Output: Total of numeric values: 7

empty = []
total_empty = sum(empty, 0) # Be explicit! Clearly shows start value 
print(f"Total of empty list: {total_empty}")  # Output: Total of empty list: 0


