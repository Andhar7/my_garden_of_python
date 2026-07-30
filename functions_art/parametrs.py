

# - `def` — the keyword that creates a function
# - `greet` — the name we give to this thought
# - `name` — the parameter (the question the function asks)
# - `return` — the answer it gives back

# This is the foundation. Now we go deeper. 🌿

## Part 2 — Default Parameter Values

# A parameter can have a default — a value used when the caller does not provide one:

def greet(name, greeting="Namaste"):
    return f"{greeting}, {name}!"

print(greet("Gurudev"))            # Namaste, Gurudev!    ← uses default
print(greet("Arjuna"))             # Namaste, Arjuna!     ← uses default
print(greet("Devaki", "Welcome"))  # Welcome, Devaki!     ← caller overrides

# Defaults make parameters **optional** — the function works with or without them.

### The Rule: Required Parameters First

# ✅ Correct — required first, defaults after:
def create_user(name, city, role="student", active=True):
    pass

# ❌ SyntaxError — required after default:
# def create_user(name, role="student", city):
#    pass

# Python enforces this. If defaults could come before required parameters,
# how would Python know which is which in `create_user("Gurudev", "Zürich")`? 🌿






