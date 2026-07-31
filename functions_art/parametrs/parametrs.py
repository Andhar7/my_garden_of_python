

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


### The Mutable Default Trap ⚠️

# This is one of Python's most famous pitfalls:

# ```python
# ❌ DANGEROUS — mutable default:
def add_item(item, collection=[]):
    collection.append(item)
    return collection

print(add_item("a"))   # ["a"]
print(add_item("b"))   # ["a", "b"]  ← WRONG! Expected: ["b"]
print(add_item("c"))   # ["a", "b", "c"]  ← the list persists!
# ```

# The default `[]` is created **once** when the function is defined — not at each call.
# Every call that uses the default shares the **same** list.

# We saw this in the 18th flower (`id()`) — now we understand it fully.

# ```python
# ✅ CORRECT — use None as default, create fresh inside:
def add_item_correct(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection

print(add_item_correct("a"))   # ["a"]
print(add_item_correct("b"))   # ["b"]   ← correct!
# ```

# **The rule:** Never use a mutable object (`[]`, `{}`, `set()`) as a default.
# Use `None` and create fresh inside. 🙏


## Part 3 — `*args` · The Open Door

# We planted this seed in Part 1, Flower 3. Now we understand it fully.

# `*args` allows a function to receive **any number of positional arguments**:
def total(*args):
    print(f"Arguments: {args}")
    return sum(args)

print(total(2, 3, 5))
print(total(22, 34, 55))
print(total(-2, -3, 5))

# Inside the function, `args` is a **tuple** — all the extra positional arguments collected.


### `*args` With Required Parameters
def greet_all(gretting, *names):
    
    for name in names:
        print(f" * - * {gretting} 🙏 * - *  {name} ! ")
        

greet_all("Namaste", "Arjuna", "Devaki", "Bhishma", "Gurudev")


# `greeting` receives the first argument. `*names` receives all the rest.


### Unpacking Into `*args`

# The `*` operator also works in reverse — unpacking a list or tuple into arguments:
def add(a, b, c):
   return a + b + c

numbers = [1, 2, 3]
print(*numbers)

scores = [122, 212, 333]
print(*scores)

numbers = [1, 2, 3]
print(add(*numbers))

scores = [121, 212, 333]
print(add(*scores))
# The `*` in the call unpacks the collection into separate positional arguments. 🌿

## Part 4 — `**kwargs` · The Named Open Door

# `**kwargs` allows a function to receive **any number of keyword arguments**:
def describe(**kwargs):
    
    print(f"Recived arguments of kwargs: {kwargs}")
    
    for key, value in kwargs.items():
        print(f"The Key is : {key} and value is : {value}")
        
describe(name="Gurudev", city="Zürich", years=18)
# Recived arguments of kwargs: {'name': 'Gurudev', 'city': 'Zürich', 'years': 18}
# The Key is : name and value is : Gurudev
# The Key is : city and value is : Zürich
# The Key is : years and value is : 18

# Inside the function, `kwargs` is a **dictionary** — all the keyword arguments collected.



### `**kwargs` Unpacking — The Mirror

#Just as `*` unpacks a list, `**` unpacks a dictionary into keyword arguments:
def greet_kwargs(name, city, years):
    return f"Namaste 🙏 {name} - from city: {city} and years {years} of mediation practise 🌹"

person = {"name": "Gurudev", "city": "Zürich", "years": 18}
print(greet_kwargs(**person))
#This is used constantly with Django forms, API calls, and configuration. 🙏

## Part 5 — The Complete Parameter Order

# Python has a strict order for all parameter types:

# ```python
# def full_example(
#     pos_only,              # positional-only (before /)
#     /,                     # ← the / separator
#     normal,                # normal (positional or keyword)
#     *,                     # ← the * separator (no *args, just forces keyword-only)
#     keyword_only,          # keyword-only (after *)
#     **kwargs               # catches all remaining keyword args
# ):
#     pass
# ```

# In practice, the most common combinations:

# Most common: normal + defaults
def create_post(title, body, published=False, author="Anonymous"):
    pass

# With *args:
def log(level, *messages):
    pass

# With **kwargs:
def configure(**settings):
    pass

# All together:
def api_call(endpoint, *path_parts, method="GET", **headers):
    pass

## Part 6 — Keyword-Only Arguments

# After `*args` (or a bare `*`), all parameters must be passed **by name**:
def create_user(name, *, role="student", active=True):
    #                 ↑ bare * forces keyword-only after this point
    return {"name": name, "role": role, "active": active}


create_user("Gurudev")                          # ✅ uses defaults
create_user("Gurudev", role="admin")            # ✅ keyword
create_user("Gurudev", active=False)            # ✅ keyword
# create_user("Gurudev", "admin")                 # ❌ TypeError — "admin" has no positional slot

# **Why keyword-only?**

# When a function has many optional parameters, callers can make mistakes with positional order.
# Keyword-only forces them to be explicit:

# ```python
# Without keyword-only — easy to mix up:
# send_email("gurudev@om.com", True, False, "high")   # what do True, False, "high" mean?

# With keyword-only — crystal clear:
# send_email("gurudev@om.com", html=True, track=False, priority="high")

## Part 7 — Positional-Only Arguments

# Before the `/`, parameters can **only** be passed by position — never by name:
def distance(x, y, /):
    return (x ** 2 + y ** 6) ** 0.5

dist_of_param = distance(3, 4)
print(dist_of_param)

# **Why positional-only?**
# For mathematical or low-level functions where the parameter names are not meaningful to callers,
# and where you want freedom to rename them internally without breaking caller code.

# Python's own built-ins use this: `len(obj)`, `abs(x)` — you cannot write `len(obj=mylist)`.

# In everyday application code, positional-only is rare.
# Know it exists. Use it if you are writing library functions. 🌿

## Part 8 — Docstrings · The Function's Voice

# A docstring is a string placed at the very start of a function — its self-description:

# ```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float, rounded to 1 decimal place.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.9
    """
    return round(weight_kg / height_m ** 2, 1)

# ```

# Python stores the docstring and makes it available:

# ```python
print(calculate_bmi.__doc__)   # prints the docstring
help(calculate_bmi)            # prints formatted help
# ```
### Docstring Styles

# Three common styles — be consistent within a project:

# **Google style (recommended for readability):**
# ```python
def greet(name, greeting="Namaste"):
    """Greet a person by name.

    Args:
        name: The person's name.
        greeting: The greeting word. Defaults to "Namaste".

    Returns:
        A formatted greeting string.
    """
    return f"{greeting}, {name}!"
# ```

# **One-liner — for simple functions:**
# ```python
def double(n):
    """Return n multiplied by two."""
    return n * 2
# ```

# **When to write a docstring:**
# - Public functions (used by others or in Django views/models)
# - Any function whose purpose is not immediately obvious from its name
# - Complex functions with multiple parameters

# **When not to:**
# - A simple private helper whose name says everything: `def _is_even(n):`

## Part 9 — Type Hints · The Language of Intention

# Type hints tell readers (and tools) what types a function expects and returns:

# ```python
def greet_namaste(name: str, times: int = 3) -> str:
    return (f"Namaste, {name}! " * times).strip()

print(greet_namaste("Gurudev", 5))
# ```

# - `name: str` — this parameter should be a string
# - `times: int = 1` — this should be an int, with default 1
# - `-> str` — this function returns a string

# **Type hints are not enforced at runtime** — Python does not check them.
# They are documentation, IDE assistance, and input for type-checking tools like `mypy`.

### Common Type Hints

# ```python
from typing import Optional, List, Dict, Tuple, Union, Any

def process(
    name:    str,
    score:   float,
    tags:    list[str],           # Python 3.9+
    config:  dict[str, int],      # Python 3.9+
    result:  str | None = None,   # Python 3.10+  (or Optional[str])
) -> tuple[str, float]:
    pass

# ```

### In Real Django-Style Code

def get_user_score(user_id: int, default: float = 0.0) -> float:
    """Return the score for a user, or default if not found."""
    pass

def create_post(
    title:     str,
    body:      str,
    author_id: int,
    published: bool = False,
) -> dict[str, str | int | bool]:
    pass

# Type hints make large codebases navigable — your IDE can tell you exactly what each function needs. 🌿

## Part 10 — Putting It All Together

from typing import Optional


def send_notification(
    recipient:   str,
    message:     str,
    /,
    *,
    subject:     str = "Notification",
    priority:    str = "normal",
    cc:          Optional[list[str]] = None,
) -> bool:
    """Send a notification to a recipient.

    Args:
        recipient: Email address of the primary recipient.
        message:   The notification body.
        subject:   Email subject line. Defaults to 'Notification'.
        priority:  Message priority — 'low', 'normal', or 'high'.
        cc:        Optional list of CC email addresses.

    Returns:
        True if the notification was sent successfully.
    """
    if cc is None:
        cc = []

    print(f"To:       {recipient}")
    print(f"Subject:  {subject} [{priority}]")
    print(f"CC:       {', '.join(cc) if cc else 'none'}")
    print(f"Message:  {message}")
    return True


# Usage:
send_notification(
    "gurudev@om.com",
    "Your session begins in 10 minutes.",
    subject  = "Meditation Reminder",
    priority = "high",
    cc       = ["arjuna@om.com", "devaki@om.com"],
)
# ```

# Every technique in this flower — together in one function. 🙏










