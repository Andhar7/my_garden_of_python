# The Professional Version 💎


def is_palindrome(s):
    # Handle edge cases first
    if s == "":
        return True  # empty string: palindrome by convention

    # Normalize: ignore case ("Racecar" == "racecar")
    s = s.lower()

    # Core logic: clean and clear
    return s == s[::-1]


 
print(is_palindrome("mama"))  # → True
print(is_palindrome("racecar"))  # → True
print(is_palindrome("Racecar"))  # → True  (normalized)
print(is_palindrome("hello"))  # → False
print(is_palindrome(""))  # → True

# Notice — no
# print()
# inside
# the
# function.A
# function
# 's job is to RETURN a value. The caller decides what to print. This is a professional habit. 🙏
