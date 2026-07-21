# 🌸 Flower #21: any() & all() — The Guardians of Truth Logic

**Status:** Master the boolean guardians ✨
**Why Here:** Beyond true/false lies decision logic 🙏
**Journey:** From individual values to collective truths 🔥

---

## 🙏 A Story Before We Begin

Most Python students learn conditionals like this:

```python
if condition:
    do_something()
```

And they think they know it. They move on. They never return. 💔

But what if you need to check **multiple conditions at once?**

What if you need to ask: **"Is ANY of these true?" or "Are ALL of these true?"**

This is where **any() and all()** become your most powerful tools.

They are **the guardians of collective truth** — how Python makes decisions about groups, not just individuals. 🕉️

---

## 📖 Part 1: The Fundamental Truth

### any() — At Least One Must Be True

```python
# "Is ANY of these true?"
results = [False, False, True, False]
if any(results):
    print("At least one is True!")  # ← This runs
```

**any() means: "If even ONE element is truthy, return True"**

---

### all() — ALL Must Be True

```python
# "Are ALL of these true?"
scores = [90, 85, 92, 88]
if all(score > 80 for score in scores):
    print("Everyone passed!")  # ← This runs
```

**all() means: "Only if EVERY element is truthy, return True"**

---

## 🔥 Part 2: any() — The "At Least One" Guardian

### Basic Usage

```python
# Simple list check
flags = [False, False, False]
print(any(flags))  # → False (none are True)

flags = [False, False, True]
print(any(flags))  # → True (at least one is True)

# Empty list special case
print(any([]))  # → False (nothing to be true)
```

**Key Truth:** any([]) returns False because there's nothing to be true! 💎

---

### With Numbers (Truthy/Falsy)

```python
# Numbers: 0 is False, anything else is True
numbers = [0, 0, 0]
print(any(numbers))  # → False (all are 0/False)

numbers = [0, 0, 5]
print(any(numbers))  # → True (5 is truthy)

# Strings: empty string is False, non-empty is True
words = ["", "", ""]
print(any(words))  # → False (all empty)

words = ["", "", "hello"]
print(any(words))  # → True (hello is truthy)
```

---

### With Conditions (Generator Expressions)

```python
# "Is ANY number even?"
numbers = [1, 3, 5, 7, 9]
print(any(n % 2 == 0 for n in numbers))  # → False

numbers = [1, 3, 5, 8, 9]
print(any(n % 2 == 0 for n in numbers))  # → True (8 is even)

# "Is ANY score below 60?"
scores = [85, 92, 78, 88]
print(any(score < 60 for score in scores))  # → False

scores = [85, 92, 45, 88]
print(any(score < 60 for score in scores))  # → True (45 is below 60)
```

---

## 🌊 Part 3: all() — The "All Must Be True" Guardian

### Basic Usage

```python
# Simple list check
flags = [True, True, True]
print(all(flags))  # → True (all are True)

flags = [True, True, False]
print(all(flags))  # → False (one failed)

# Empty list special case
print(all([]))  # → True (vacuous truth - nothing to fail)
```

**Key Truth:** all([]) returns True because there's nothing to fail! 💎

---

### With Numbers (Truthy/Falsy)

```python
# All non-zero
numbers = [5, 10, 15]
print(all(numbers))  # → True (all truthy)

numbers = [5, 0, 15]
print(all(numbers))  # → False (0 is falsy)

# All non-empty strings
words = ["hello", "world", "python"]
print(all(words))  # → True (all non-empty)

words = ["hello", "", "python"]
print(all(words))  # → False (empty string)
```

---

### With Conditions (Generator Expressions)

```python
# "Are ALL numbers even?"
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # → True

numbers = [2, 4, 5, 8]
print(all(n % 2 == 0 for n in numbers))  # → False (5 is odd)

# "Are ALL scores above 60?"
scores = [85, 92, 78, 88]
print(all(score >= 60 for score in scores))  # → True

scores = [85, 92, 45, 88]
print(all(score >= 60 for score in scores))  # → False (45 fails)
```

---

## 🎯 Part 4: Real-World Patterns

### Pattern #1: Form Validation

```python
# Check if all form fields are filled
form_data = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'password': 'secure123'
}

# All values must be non-empty
all_filled = all(value for value in form_data.values())
print(f"Form complete: {all_filled}")  # → True

# One empty field
form_data['email'] = ''
all_filled = all(value for value in form_data.values())
print(f"Form complete: {all_filled}")  # → False
```

---

### Pattern #2: Quality Assurance Testing

```python
# Test results - all must pass
test_results = [True, True, True, True]
if all(test_results):
    print("✅ All tests passed!")

test_results = [True, True, False, True]
if not all(test_results):
    print("❌ Some tests failed!")

# Better: with meaningful checks
test_cases = {
    'login': True,
    'checkout': True,
    'payments': False,  # ← This one failed
    'shipping': True
}

if all(test_cases.values()):
    print("✅ Ready to deploy")
else:
    failed = [name for name, result in test_cases.items() if not result]
    print(f"❌ Fix these first: {failed}")
```

---

### Pattern #3: Access Control / Permissions

```python
# User has ALL required permissions
user_permissions = ['read', 'write', 'delete']
required = ['read', 'write']

has_access = all(perm in user_permissions for perm in required)
print(f"Has access: {has_access}")  # → True

# Check if ANY permission is missing
admin_permissions = ['read', 'write', 'delete', 'admin']
required = ['read', 'write', 'admin']

missing = [p for p in required if p not in admin_permissions]
if missing:
    print(f"❌ Missing: {missing}")
else:
    print("✅ All permissions granted")
```

---

### Pattern #4: Data Validation

```python
# Validate that all items meet criteria
prices = [10.50, 25.00, 5.99, 15.75]

# All prices positive
all_positive = all(price > 0 for price in prices)
print(f"Valid prices: {all_positive}")  # → True

# At least one within discount range
discount_eligible = any(10 < price < 30 for price in prices)
print(f"Discount available: {discount_eligible}")  # → True

# Check stock levels
inventory = {'apples': 50, 'oranges': 0, 'bananas': 120}
in_stock = all(qty > 0 for qty in inventory.values())
print(f"All items in stock: {in_stock}")  # → False
```

---

### Pattern #5: Email/List Validation

```python
# Check if ANY email is invalid (simple check)
emails = [
    'alice@example.com',
    'bob@company.org',
    'charlie@mail.co.uk'
]

valid_emails = all('@' in email for email in emails)
print(f"All emails valid: {valid_emails}")  # → True

# Check if ANY email is missing domain
emails = ['alice@example.com', 'bob.local', 'charlie@mail.org']
valid_emails = all('@' in email and '.' in email for email in emails)
print(f"All emails valid: {valid_emails}")  # → False (bob.local fails)
```

---

## 💎 Part 5: The Deep Truth — Short-Circuit Evaluation

### any() Stops Early

```python
# any() returns True as soon as it finds a True value
results = [False, False, False, True, False, False]

# Without any() - checks all 6 values
for r in results:
    if r:
        print("Found True!")
        break

# With any() - stops at index 3 (doesn't check indices 4, 5)
if any(results):
    print("Found True!")

# This matters with expensive operations:
def expensive_check(n):
    print(f"Checking {n}...")
    return n > 50

numbers = [10, 20, 30, 60, 70, 80]

# This checks 10, 20, 30, 60 then stops (doesn't check 70, 80)
if any(expensive_check(n) for n in numbers):
    print("At least one is > 50")

# Output:
# Checking 10...
# Checking 20...
# Checking 30...
# Checking 60...
# At least one is > 50
```

---

### all() Also Stops Early

```python
# all() returns False as soon as it finds a False value
scores = [90, 85, 78, 88]

# Stops immediately at 78 (doesn't check 88)
if all(score >= 80 for score in scores):
    print("All passed")
else:
    print("Someone failed")

# Efficient!
```

**Key Truth:** This short-circuit behavior makes any() and all() FAST! 💡

---

## 🎨 Part 6: Common Mistakes (Learn From Them!)

### Mistake #1: Confusing Emptiness

```python
# ❌ Forgotten: empty list behavior
print(any([]))  # → False (nothing is true)
print(all([]))  # → True (nothing failed!)

# This can surprise you in edge cases
data = []  # Empty dataset
if all(value > 0 for value in data):  # → True!
    print("All values positive")  # ← Runs even though no data!

# ✅ Handle empty case explicitly
data = []
if data and all(value > 0 for value in data):
    print("All values positive")  # ← Won't run
```

---

### Mistake #2: Using any/all on Booleans Directly

```python
# ❌ Confusing
if any([True, False, False]):  # → True
if all([True, False, False]):  # → False

# ✅ More readable
results = [True, False, False]
if True in results:
    print("At least one True")
if False not in results:
    print("All are True")
```

---

### Mistake #3: Not Using Generator Expressions

```python
# ❌ Creates list in memory (wasteful)
large_numbers = range(1000000)
if any([n > 999999 for n in large_numbers]):
    print("Found!")

# ✅ Uses generator (efficient)
if any(n > 999999 for n in large_numbers):
    print("Found!")
```

---

## 🎓 Part 7: any() vs all() vs if/else

### When to Use Each

```python
# Use any() when: "Is at least one true?"
if any(error for error in error_list):
    print("Errors found")

# Use all() when: "Are all true?"
if all(test for test in tests):
    print("All tests pass")

# Use if/else when: Simple single condition
if x > 5:
    print("x is large")

# Avoid: Clunky alternatives
❌ if len([x for x in items if x]) > 0:  # Just use any()!
✅ if any(items):
```

---

## 🎯 Part 8: Your Exercises — Type, Predict, Run

### Exercise 1: Understanding any() and all()

**Task:** Predict output BEFORE running:

```python
# What do these return?
print(any([False, False, False]))
print(all([True, True, True]))
print(any([]))
print(all([]))
print(any([0, 0, 5]))
print(all([1, 2, 0]))
```

**What to explore:**
- Why does any([]) return False?
- Why does all([]) return True?
- How do truthiness rules apply?

---

### Exercise 2: Conditional Checks

**Task:** Check conditions using any() and all():

```python
numbers = [2, 4, 6, 8, 10]

# Are ALL numbers even?
all_even = all(n % 2 == 0 for n in numbers)
print(f"All even: {all_even}")

# Is ANY number odd?
any_odd = any(n % 2 != 0 for n in numbers)
print(f"Any odd: {any_odd}")

numbers = [2, 4, 5, 8, 10]

# Are ALL numbers even?
all_even = all(n % 2 == 0 for n in numbers)
print(f"All even: {all_even}")

# Is ANY number odd?
any_odd = any(n % 2 != 0 for n in numbers)
print(f"Any odd: {any_odd}")
```

**What to explore:**
- How do generator expressions work with any/all?
- What conditions are most useful?

---

### Exercise 3: Form Validation

**Task:** Validate a form using all():

```python
# Form data
form = {
    'username': 'alice',
    'email': 'alice@example.com',
    'password': 'secure123'
}

# Check all fields are filled
all_filled = all(form.values())
print(f"Form complete: {all_filled}")

# Now with empty field
form['email'] = ''
all_filled = all(form.values())
print(f"Form complete: {all_filled}")

# Check all fields meet minimum length
min_length = 3
all_valid = all(len(str(v)) >= min_length for v in form.values())
print(f"All fields valid: {all_valid}")
```

**What to explore:**
- How to validate multiple fields?
- How to combine multiple conditions?

---

### Exercise 4: Quality Assurance

**Task:** Check if all tests pass:

```python
tests = {
    'login_test': True,
    'checkout_test': True,
    'payment_test': True,
    'shipping_test': False
}

# All tests must pass
if all(tests.values()):
    print("✅ All tests passed - ready to deploy!")
else:
    failed = [name for name, result in tests.items() if not result]
    print(f"❌ Tests failed: {failed}")

# How many tests passed?
passed_count = sum(1 for result in tests.values() if result)
total_count = len(tests)
print(f"Passed {passed_count}/{total_count}")
```

**What to explore:**
- How to identify which tests failed?
- How to combine with other logic?

---

### Exercise 5: The Challenge — Access Control

**Task:** Check user permissions:

```python
user_roles = ['user', 'moderator']
admin_roles = ['admin', 'super_admin']

# Can user moderate?
can_moderate = any(role in ['admin', 'moderator'] for role in user_roles)
print(f"Can moderate: {can_moderate}")

# Is user admin?
is_admin = any(role in admin_roles for role in user_roles)
print(f"Is admin: {is_admin}")

# Permission system
required_permissions = ['read', 'write', 'delete']
user_permissions = ['read', 'write']

# Has ALL required?
has_access = all(perm in user_permissions for perm in required_permissions)
print(f"Full access: {has_access}")

# Is MISSING any?
missing = [perm for perm in required_permissions if perm not in user_permissions]
print(f"Missing: {missing}")
```

**What to explore:**
- How to check permissions efficiently?
- How to find missing permissions?
- Real-world access control logic?

---

## 🌟 Part 9: any() & all() in the Real World

### Production Code Example

```python
# Data quality check before processing
records = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': ''},
    {'id': 3, 'name': '', 'email': 'charlie@example.com'}
]

# Find invalid records
invalid = [r for r in records if not all(r.values())]
print(f"Invalid records: {invalid}")

# Check if ANY record is valid
has_valid = any(all(r.values()) for r in records)
print(f"Has at least one valid record: {has_valid}")

# Process only valid records
valid_records = [r for r in records if all(r.values())]
for record in valid_records:
    print(f"Processing: {record['name']}")
```

---

## 🙏 Closing Wisdom

Dear Gurudev...

any() and all() are **the guardians of collective truth**.

When you truly understand them, you understand:
- 🎯 How to make decisions about groups
- 🎯 How to validate multiple conditions
- 🎯 How to check permissions and access
- 🎯 How to validate data quality
- 🎯 How to think in boolean logic

This is **decision-making architecture**. 💎

---

## ✨ Remember the Contract

As you practice:

✅ **TYPE every example** — feel the logic
✅ **PREDICT** before running — build mental models
✅ **EXPERIMENT** — mix any() and all()
✅ **ASK WHY** — understand short-circuit behavior
✅ **DEBUG** your errors yourself first

This is how mastery is built. 🔥

---

## 📚 Your Next Steps

1. **Type all the examples in this guide** (every one!)
2. **Predict the output before running**
3. **Do all 5 exercises** — build practice files
4. **Ask questions** when anything is unclear
5. **Debug your own errors** before asking for help

Then, when you're ready, we'll review and continue to **Flower #22**.

---

**Om Namah Shivaya** 🕉️

Your Teacher awaits your questions. 🙏 ❤️ ✨

