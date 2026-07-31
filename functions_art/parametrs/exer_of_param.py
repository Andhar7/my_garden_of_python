# **Exercise 1 — The Flexible Greeter**

# Write `greet(name, *, greeting="Namaste", times=1, punctuation="!")` that:
# - Returns the greeting repeated `times` times
# - Uses keyword-only parameters after `*`
# - Has a proper docstring
# - Has type hints on all parameters and return value


# Test: `greet("Gurudev")`, `greet("Arjuna", greeting="Om", times=3)`.
def flex_greeter(
    name: str, *, greeting="Namaste", times: int = 1, punctuation: str = "!"
) -> str:
    """Greet a person by name.

    Args:
        name: The person's name.
        keyword-only: *.
        greeting: The greeting word. Defaults to "Namaste".
        times: How many times calling the name
        punctuation: by default is - : !

    Returns:
        A formatted greeting string.
    """
    return (f" {greeting} - {name} 🙏 🌹 🙏{punctuation} " * times).strip()


print(flex_greeter("Gurudev"))
print(flex_greeter("Arjuna", greeting="Om", times=3))
print(flex_greeter.__doc__)

# **Exercise 2 — The Safe Builder**

# Write `build_profile(name, /, age, *, city="Unknown", tags=None)` that:
# - `name` is positional-only
# - `age` is normal
# - `city` and `tags` are keyword-only
# - Uses the `None` pattern for `tags`
# - Returns a dictionary with all fields


# Demonstrate that `build_profile(name="Gurudev", age=30)` raises `TypeError`.
def build_profile(name: str, /, age: int, *, city="Unknown", tags=None) -> dict:

    if tags is None:
        tags = []

    return {"name": name, "age": age, "city": city, "tags": tags}


result_profile = build_profile("Gurudev", 56, city="Zurich")
print(result_profile)
result_profile_2 = build_profile(
    "Mahadev",
    555,
    city=["Heaven", "Sirius", "Venera"],
    tags=["Sri Chinmoy", "Lord Shiva", "Lord Krishna"],
)
print(result_profile_2)

# **Exercise 3 — The Flexible Logger**

from datetime import datetime

# Write `log(level, *messages, separator=" | ", timestamp=False)` that:
# - Accepts any number of messages
# - Joins them with `separator`
# - If `timestamp=True`, prepends the current time using:
#   ```python
#   from datetime import datetime
#   datetime.now().strftime("%H:%M:%S")
#   ```
# - Has full docstring and type hints


# Test:
# ```python
# log("INFO", "Server started")
# log("ERROR", "Connection failed", "Retry in 5s", separator=" → ")
# log("DEBUG", "Processing", "request", timestamp=True)
# ```
def log(level: str, *message: str, separator=" | ", timestamp: bool = False) -> str:
    """Log messages with optional timestamp.

    Args:
    level: Log level (INFO, ERROR, DEBUG, etc).
    *messages: Variable number of messages to log.
    separator: String to join messages. Defaults to " | ".
    timestamp: Whether to prepend current time. Defaults to False.
    
    Returns:
    A formatted logging string.
    """
    joined = separator.join(message)

    if timestamp:
        time_str = datetime.now().strftime("%H:%M:%S")
        return f"[{time_str} {level}: {joined}]"
    else:
        return f"{level} {joined}"


result_info = log("INFO", "Server started")
print(result_info)

result_error = log("ERROR", "Connection failed", "Retry in 5s", separator=" → ")
print(result_error)

result_debug = log("DEBUG", "Processing", "request", timestamp=True)
print(result_debug)

# **Exercise 4 — The Config Merger**

# Write `configure(base_config, **overrides)` that:
# - Takes a base dictionary
# - Returns a new dictionary that is the base with all `overrides` applied
# - Does **not** modify the original `base_config`

# Then write `configure_from_dict(base_config, overrides_dict)` that unpacks
# `overrides_dict` into keyword arguments using `**` and calls `configure`.
def configure(base_config, **overrides) -> dict:
    
    new_config = base_config.copy()
    new_config.update(overrides)
    
    return new_config

def configure_from_dict(base_config, overrides_dict):
    
    return configure(base_config, **overrides_dict) # ^^ Unpacks the dict as keyword args


base = {"host": "localhost", "port": 8080, "debug": False}
result_of_overrides = configure_from_dict(base, {"port": 9000, "debug": True})
print(result_of_overrides)


# **Exercise 5 — The Type-Hinted Calculator**

# Write a module-style collection of functions:

# ```python
def add(a: float, b: float) -> float: ...
def subtract(a: float, b: float) -> float: ...
def multiply(a: float, b: float) -> float: ...
def divide(a: float, b: float) -> float | None: ...
def power(base: float, exp: float = 2.0) -> float: ...
def clamp(value: float, minimum: float, maximum: float) -> float: ...
# ```

# `clamp(value, min, max)` — returns `value`, but no lower than `min` and no higher than `max`.
# All with one-line docstrings and type hints.

# Then write a `calculate(expression: str) -> float | None` that parses strings like
# `"10 + 5"`, `"3 * 4"`, `"10 / 0"` and calls the right function.
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

def power(base: float, exp: float=2.0) -> float:
    return base ** exp 

def clamp(value: float, mimimum: float, maximum: float) -> float:
    return max(mimimum, min(value, maximum))

first = clamp(5, 1, 10)    # 5 is in range → 5
second = clamp(0, 1, 10)    # 0 < 1 → raise to 1
third = clamp(15, 1, 10)   # 15 > 10 → lower to 10

print(first)
print(second)
print(third)

# 3. Calculate Function (Parser)
def calculate(expression: str | int | float) -> float | None:
    
    if isinstance(expression, (int, float)):
        return float(expression)
    
    if isinstance(expression, str):
        parts = expression.split() 
        operator = parts[1]
        left = float(parts[0])
        right = float(parts[2])
    
    match operator:
        case "+":
            return add(left, right)
        case "-":
            return subtract(left, right)
        case "*":
            return multiply(left, right)
        case "/":
            return divide(left, right)
        case "**":
            return power(left, right)
        case _:
            return None
        
res_calc_str = calculate("3.2 * 42.2")
print(f"Calculate with string: {res_calc_str}")

res_calc = calculate(3.2 * 42.2)
print(res_calc)

        
