

  # Challenge 1: The Pipeline (Intermediate)

  # You have a list of product dictionaries:
products = [
      {"name": "apple", "price": 1.5, "quantity": 10},
      {"name": "banana", "price": 0.8, "quantity": 5},
      {"name": "orange", "price": 2.0, "quantity": 8},
      {"name": "mango", "price": 3.5, "quantity": 3},
]

  # Write ONE LINE using map and filter with lambda:
  # 1. Filter products with price > 1.0
  # 2. Map to get (name, total_price) where total = price * quantity
  # 3. Result should be: [('apple', 15.0), ('orange', 16.0), ('mango', 10.5)]

  # Can you write this pipeline?
  # (Hint: filter first, then map, like you did with numbers)

  # This tests: Can you combine map and filter? Do you understand the order?

list_product = list(map(lambda p: (p["name"], p["price"] * p["quantity"]), 
                       filter(lambda price: price["price"] > 1, products) 
                        ))
print(list_product)

#  Challenge 2: Generator with State (Advanced)

  # Write a generator that yields Fibonacci numbers
  # But STOPS when the number exceeds a limit

# What yeild hold... experiment
def fibonacci_until(limit):
    recived = yield limit
    print(f"recived : {recived}")
    

print_list_state = list(fibonacci_until(100))
print(print_list_state)

def fibonacci_until(limit): 
    a, b = 1, 1  # Start wit default State
    
    while a <= limit: # Until limit more or equal a - then stop
        yield a # Main point! Supreme are Here... and Always See and remember
        a, b = b, a + b # State´s value Updated!
    

print_list_state = list(fibonacci_until(100))
print(print_list_state)


  # Expected usage:
  # list(fibonacci_until(100))
  # Should return: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

  # This tests: Do you understand yield? Can you maintain STATE in a generator?

 # This tests: Generators, state, conditions.


  # Challenge 3: Custom Map Implementation (Deep)

  # You understand map() internally because you've seen this:
  # def map_numbers(function, iterable):
  #     for item in iterable:
  #         yield function(item)

  # Now write a CUSTOM FILTER from scratch:

def my_filter(predicate, iterable):
      # Your code here — use yield
      pass

  # Test it:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(my_filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Should be [2, 4, 6, 8, 10]

  # Then use it with different predicates:
# long_words = list(my_filter(lambda w: len(w) > 4,
#                                ["cat", "elephant", "dog", "butterfly"]))
# print(long_words)  # Should be ['elephant', 'butterfly']

  # This tests: Do you UNDERSTAND how filter works? Can you rebuild it?

  # This tests: Deep understanding of yield, functional programming.
  
#     🎯 Can You Try?

#   Write my_filter() using:
#   - ✅ yield
#   - ✅ A for loop
#   - ✅ An if statement to check the predicate
#   - ✅ Comments explaining each line
def my_filter(function, iterable):
    for item in iterable: # For iteration object we check out each value
        if function(item): # in case we found what we looking for - result to give to Supreme!
            yield item # Supreme take a result ... maybe happy ... maybe no
            
  # Test number 1:
print("========= TEST 1 ===========")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(my_filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Should be [2, 4, 6, 8, 10]

  # Test 2 — Long words:
print("========= TEST 2 ===========")
words = ["cat", "elephant", "dog", "butterfly"]
long_words = list(my_filter(lambda w: len(w) > 4, words))
print(long_words)  # Should be ['elephant', 'butterfly']

    

