

# "Is ANY of these true?"
results = [False, False, True, False]
if any(results):
    print("At least one is True!")
    
# **any() means: "If even ONE element is truthy, return True"**

### all() — ALL Must Be True
# "Are ALL of these true?"
scores = [90, 85, 92, 88]
if all(score > 80 for score in scores):
    print("Everyone passed")

# **all() means: "Only if EVERY element is truthy, return True"**
# "Is ANY number even?"
numbers = [1, 3, 5, 7, 9]
print(any(n % 2 == 0 for n in numbers))

# "Is ANY score below 60?"
scores = [85, 92, 78, 88]
print(any(score < 60 for score in scores)) # False

# Simple list check
flags = [True, True, True]
print(all(flags)) # True

flags = [True, True, True, False]
print(all(flags)) # False

# All non-empty strings
words = ["hello", "world", "python"] 
print(all(words)) # True

words = ["hello", "", "python"] 
print(all(words)) # False

### With Conditions (Generator Expressions)
# Check if all form fields are filled
form_data = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'password': 'secure123'
}

all_field = all(value for value in form_data.values())
print(f"All Form is complete: {all_field}") # True

# Test results - all must pass
test_results = [True, True, True, True, False]
def new_func(test_results):
    if all(test_results):
        print("All is passed")
    else:
        print("❌ Some tests failed!")

new_func(test_results)

# User has ALL required permissions
user_permissions = ['read', 'write', 'delete']
required = ['read', 'write']

has_access = all(perm in user_permissions for perm in required)
print(f"Has access: {has_access}") # True

# Check if ANY permission is missing
admin_permissions = ['read', 'write', 'delete', '']
required = ['read', 'write', 'admin']
def check_if_permissions_missing(admin_permissions):
    
    missing = [p for p in required if p not in admin_permissions]
    if missing:
        print(f"❌ Missing: {missing}")
    else:
        print("✅ All permissions granted")
    
check_if_permissions_missing(admin_permissions)


### Pattern #4: Data Validation
# Validate that all items meet criteria
prices = [10.50, 25.00, 5.99, 15.75]

# All prices positive
all_positive = all(price > 0 for price in prices)
print(f"Valid prices: {all_positive}")

# At least one within discount range
discount_any = any(10 < price < 30 for price in prices)
print(f"Discount is available for : {discount_any} for prices: {prices}")

# Check stock levels
inventory = {'apples': 50, 'oranges': 0, 'bananas': 120}
in_stock = all(qty > 0 for qty in inventory.values())
print(f"All items in stock: {in_stock} for inventory: {inventory}")

# Check if ANY email is invalid (simple check)
emails = [
    'alice@example.com',
    'bob@company.org',
    'charlie@mail.co.uk',
]

def check_all_emails(emails):
    
    check_valid = all('@' in email for email in emails)
    check_dot = all('@' in email and '.' in email for email in emails)
    if check_valid:
        print(f"All emails is valid: {check_valid}")
    if check_dot:
        print(f"Some email has dot . {check_dot}")
    else:
        print("Something wrong")
    
check_all_emails(emails)

# any() returns True as soon as it finds a True value
result_true = [False, False, False, True, False, False]
def check_true(result_true):
    
    if any(result_true):
        print("Finally! We are found the truth!")
    else:
        print("Try to continue...")

check_true(result_true)

numbers_expensive = [10, 20, 30, 60, 70, 80]
def expensive_check(n):
    print(f"Checking {n} ... ")
    return n > 50

def find_any_expensive(numbers_expensive):
    
    if any(expensive_check(n) for n in numbers_expensive):
        print(f"We found numbers of expensive > 50: {numbers_expensive}")
    else:
        print("Error")
    
find_any_expensive(numbers_expensive)





