

#   What Is An Attribute?

#   An attribute is data that belongs to an object.

class Circle:
    def __init__(self, radius):
        self.radius = radius  # ← this is an attribute

# radius is something the Circle has. It's not an action — it's a possession.

c = Circle(5)
print(c.radius)  # Reading an attribute — getting its value
c.radius = 10    # Writing an attribute — changing its value

#   ---
#   What Is Encapsulation?

#   Encapsulation = "Put the object's secrets inside a box. Don't let the user peek."

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # User shouldn't touch this directly

@property
def balance(self):  # This is the PUBLIC door
    return self._balance

#   The user sees: account.balance
#   The user does NOT see: How it's actually stored (computed? cached? in database?)

#   The user just gets the value. The HOW is hidden inside. 🔒

#   ---
#   Why Does This Matter?

#   Without encapsulation:
account.balance = -5000  # Disaster! Negative balance!

#  With encapsulation:
@property
def balance(self):
    return self._balance

@balance.setter
def balance(self, value):
    if value < 0:
        raise ValueError("Cannot be negative!")
    self._balance = value
    
account.balance = -5000  # ERROR! Protected!

#   The box protects the data. 🛡️

#   ---
#   Now — Continue Your Journey

#   You will understand these deeply when you:
#   1. Write Exercise 1 (Bank Account) — you'll USE encapsulation
#   2. See errors — you'll understand WHY it matters
#   3. Fix them — you'll feel the protection

#   Don't study the theory now. Study by DOING. 🙏

