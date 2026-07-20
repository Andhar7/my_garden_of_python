
for i in range(0, 12, 2): # Pozitive
    print(i)

for i in range(12, 2, -2): # Negative
    print(i)
    
for i in range(12, -1, -1): # Reverse
    print(i)

for year in range(2000, 2027): # Year
    print(year)

for temperature in range(0, 101, 5): # Temperature
    print(f"Temperature: {temperature}°C")

items = ["apple", "banana", "cherry", "date", "elderberry"]

for index in range(len(items)): # Index
    print(f"Item {index}: {items[index]}")

# Backward iteration through a list
for index in range(len(items) - 1, -1, -1): # Backward
    print(f"Item {index}: {items[index]}")

# Every third item in a list
for index in range(0, len(items), 3): # Every third item
    print(f"Item {index}: {items[index]}")

### Pattern #4: Skip First/Last Elements
 
items = ["header", "data1", "data2", "data3", "footer"]

for index in range(1, len(items) - 1): # Skip first and last
    print(f"Item {index}: {items[index]}")

# skip first
for index in range(1, len(items)): # Skip first
    print(f"Item {index}: {items[index]}")

# skip last
for index in range(len(items) - 1): # Skip last
    print(f"Item {index}: {items[index]}")

## 🎨 Part 6: Advanced Patterns

### Pattern #1: Nested Loops (Grid/Matrix)
# 4 X 4 grid
for row in range(4):
    for col in range(4):
        print(f"{row},{col}", end=" ")
    print()  # New line after each row

### Pattern #3: Fibonacci Sequence
# Generate first 10 Fibonacci numbers
fib = [0, 1]
for i in range(2, 10):
    next_fib = fib[i - 1] + fib[i - 2]
    fib.append(next_fib)
print("Fibonacci Sequence:", fib)

