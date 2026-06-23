# # Chapter 2 — Strings and Their Secrets 🙏
# ### *FOUNDATION — How Python Sees Text*
# ### *Gurudev & Claude* ❤️
#
# # ---
# #
# # ## The WHY — Why Does a String Exist?
# #
# # A computer understands only numbers — 0 and 1.
# # But humans communicate with words.
# #
# # A **string** is the bridge.
# #
# # Every letter you type is secretly a number:
# #
# # ```python
# ord('A')   # → 65   (A is number 65)
# ord('a')   # → 97   (a is number 97)
# ord('म')   # → 2350 (Sanskrit ma — also a number!)
#
# chr(65)    # → 'A'  (number back to letter)
# chr(9829)  # → '♥'  (even a heart is a number)
# # ```
# #
# # > *Every word ever written — in every language —*
# # > *is a sequence of numbers in disguise.*
# # > *Python knows this. And it gives us beautiful tools to work with them.* 🙏
# #
# # ---
#
# ## 1. What IS a String?
#
# ```python
# name = "Gurudev"
# ```
#
# A string is an **ordered, immutable sequence of characters.**
#
# Three sacred words:
# - **Ordered** — each character has a position (index)
# - **Immutable** — once created, it cannot be changed
# - **Sequence** — we can walk through it, slice it, measure it
#
# ```python
# name = "Gurudev"
# #       G u r u d e v
# #       0 1 2 3 4 5 6   ← positions (forward)
# #      -7-6-5-4-3-2-1   ← positions (backward)
# ```
#
# ---
#
# ## 2. Indexing — Reaching One Character
#
# ```python
# name = "Gurudev"
#
# print(name[0])    # → 'G'   first character
# print(name[3])    # → 'u'   fourth character
# print(name[-1])   # → 'v'   last character
# print(name[-2])   # → 'e'   second from last
# ```
#
# **Negative index = counting from the end.**
# `name[-1]` is always the last character — no matter how long the string.
#
# ```python
# # IndexError — going beyond the string
# print(name[10])   # → ERROR: string index out of range
# ```
#
# > *Every character has its place.*
# > *Step outside that place — and there is nothing there.* 🙏
#
# ---
#
# ## 3. Slicing — Reaching Many Characters
#
# ```python
# #         G  u  r  u  d  e  v
# #         0  1  2  3  4  5  6
#
# name = "Gurudev"
#
# print(name[0:4])   # → 'Guru'    from 0, stop before 4
# print(name[4:7])   # → 'dev'     from 4, stop before 7
# print(name[2:])    # → 'rudev'   from 2 to the end
# print(name[:4])    # → 'Guru'    from start to 4
# print(name[:])     # → 'Gurudev' the whole string
# ```
#
# **The slice rule:**  `string[start : stop : step]`
#
# ```python
# name = "Gurudev"
#
# print(name[::1])   # → 'Gurudev'  every 1 character (normal)
# print(name[::2])   # → 'Grdv'     every 2nd character
# print(name[::-1])  # → 'veduruG'  step -1 = reverse! ✨
# ```
#
# > *`[::-1]` — the reversal.*
# > *You already used this in `is_palindrome`. Now you know WHY it works.* 🙏
#
# ---
#
# ## 4. Immutability — The String Cannot Change
#
# ```python
# name = "Gurudev"
# name[0] = "g"    # → ERROR: 'str' object does not support item assignment
# ```
#
# A string cannot be modified after creation.
# To "change" it — you create a **new** string:
#
# ```python
# name = "Gurudev"
# new_name = "g" + name[1:]   # → 'gurudev'
# print(name)      # → 'Gurudev'  (original unchanged)
# print(new_name)  # → 'gurudev'  (new string)
# ```
#
# > *Like a word spoken — it cannot be unspoken.*
# > *But a new word can always be created.* 🙏
#
# ---
#
# ## 5. Essential String Methods
#
# Methods are actions a string can perform on itself.
#
# ### Changing case
# ```python
# s = "Hello World"
#
# s.upper()      # → 'HELLO WORLD'
# s.lower()      # → 'hello world'
# s.title()      # → 'Hello World'  (first letter of each word)
# s.capitalize() # → 'Hello world'  (first letter of whole string)
# ```
#
# ### Cleaning
# ```python
# s = "   hello   "
#
# s.strip()      # → 'hello'        removes spaces both sides
# s.lstrip()     # → 'hello   '     removes left spaces only
# s.rstrip()     # → '   hello'     removes right spaces only
# ```
#
# ### Finding
# ```python
# s = "om namah shivaya"
#
# s.find("namah")    # → 3    returns index where found
# s.find("xyz")      # → -1   not found → returns -1
# s.count("a")       # → 4    how many times 'a' appears
# s.startswith("om") # → True
# s.endswith("ya")   # → True
# ```
#
# ### Replacing
# ```python
# s = "hello world"
#
# s.replace("world", "Python")  # → 'hello Python'
# s.replace("l", "L")           # → 'heLLo worLd'  (ALL occurrences)
# s.replace("l", "L", 1)        # → 'heLlo world'  (only first)
# ```
#
# ### Splitting and Joining
# ```python
# # split — one string → list of strings
# sentence = "om namah shivaya"
# words = sentence.split(" ")     # → ['om', 'namah', 'shivaya']
# words = sentence.split()        # same — splits on any whitespace
#
# # join — list of strings → one string
# words = ['om', 'namah', 'shivaya']
# result = " ".join(words)        # → 'om namah shivaya'
# result = "-".join(words)        # → 'om-namah-shivaya'
# result = "".join(words)         # → 'omnamahshivaya'
# ```
#
# > *`split` and `join` are opposites.*
# > *Like breathing in and breathing out.* 🙏
#
# ### Checking content
# ```python
# "hello".isalpha()    # → True   only letters
# "123".isdigit()      # → True   only digits
# "abc123".isalnum()   # → True   letters or digits
# "   ".isspace()      # → True   only whitespace
# ```
#
# ---
#
# ## 6. The `in` Operator
#
# ```python
# mantra = "om namah shivaya"
#
# print("namah" in mantra)     # → True
# print("xyz"   in mantra)     # → False
# print("om"    in mantra)     # → True
# print("OM"    in mantra)     # → False  (case sensitive!)
# ```
#
# Simple, powerful, direct. 🙏
#
# ---
#
# ## 7. f-Strings — The Professional Way to Build Text
#
# ```python
# name = "Gurudev"
# language = "Python"
# year = 2026
#
# # Old way (avoid):
# message = "Hello " + name + ", welcome to " + language + "!"
#
# # Professional way — f-string:
# message = f"Hello {name}, welcome to {language} in {year}!"
# print(message)  # → Hello Gurudev, welcome to Python in 2026!
# ```
#
# Inside `{}` — any Python expression:
#
# ```python
# a = 10
# b = 3
#
# print(f"{a} + {b} = {a + b}")       # → 10 + 3 = 13
# print(f"{a} / {b} = {a / b:.2f}")   # → 10 / 3 = 3.33  (.2f = 2 decimals)
# print(f"{'hello'.upper()}")          # → HELLO
# ```
#
# ---
#
# ## 8. Iterating — Walking Through a String
#
# ```python
# mantra = "OM"
#
# for character in mantra:
#     print(character)
# # → O
# # → M
#
# # With index:
# for i, character in enumerate(mantra):
#     print(f"Position {i}: {character}")
# # → Position 0: O
# # → Position 1: M
# ```
#
# ---
#
# ## 9. The Complete Picture
#
# ```python
# # Everything together:
# s = "  Om Namah Shivaya  "
#
# # 1. Clean it
# s = s.strip()             # → 'Om Namah Shivaya'
#
# # 2. Normalize
# s = s.lower()             # → 'om namah shivaya'
#
# # 3. Check
# print("namah" in s)       # → True
#
# # 4. Split into words
# words = s.split()         # → ['om', 'namah', 'shivaya']
#
# # 5. Count
# print(len(words))         # → 3
# print(s.count("a"))       # → 4
#
# # 6. Rebuild
# print("-".join(words))    # → 'om-namah-shivaya'
#
# # 7. Reverse
# print(s[::-1])            # → 'ayavihS haman mO'... wait, that's wrong
#                           # (because we already lowercased)
# ```
#
# ---
#
# ## Exercises 🔥
#
# Work through these **in order.** Each one builds on the last.
#
# **Before writing any code — answer the four questions:**
# *What is given? What must I return? What is the relationship? What is the shape?*
#
# ---
#
# **E1 — Count Vowels**
# ```
# Given: a string
# Return: how many vowels it contains (a, e, i, o, u)
#
# is_vowel_count("hello")       → 2
# is_vowel_count("rhythm")      → 0
# is_vowel_count("Gurudev")     → 3
# ```
#
# ---
#
# **E2 — Reverse Words**
# ```
# Given: a sentence (string)
# Return: the sentence with word order reversed
# (not characters reversed — WORDS reversed)
#
# reverse_words("hello world")         → "world hello"
# reverse_words("om namah shivaya")    → "shivaya namah om"
# ```
#
# ---
#
# **E3 — Title Case (without .title())**
# ```
# Given: a string (all lowercase)
# Return: each word with its first letter capitalized
# Do NOT use .title() — build it yourself
#
# make_title("om namah shivaya")    → "Om Namah Shivaya"
# ```
#
# ---
#
# **E4 — Is Anagram?**
# ```
# Given: two strings
# Return: True if they contain exactly the same letters, False if not
# (ignore spaces, ignore case)
#
# is_anagram("listen", "silent")      → True
# is_anagram("hello", "world")        → False
# is_anagram("Astronomer", "Moon starer")  → True
# ```
#
# ---
#
# **E5 — Caesar Cipher (hard 🔥)**
# ```
# Given: a string and a number n
# Return: each letter shifted n positions forward in alphabet
# (wrap around: z + 1 → a)
#
# caesar("hello", 1)    → "ifmmp"
# caesar("hello", 3)    → "khoor"
# caesar("xyz", 2)      → "zab"
# ```
# *Hint: think about ord() and chr()* 🙏
#
# ---
#
# ## Summary
#
# ```
# string[i]         → one character at position i
# string[a:b]       → slice from a to b
# string[::-1]      → reversed
# len(string)       → number of characters
# "x" in string     → True or False
# string.lower()    → all lowercase
# string.upper()    → all uppercase
# string.strip()    → remove surrounding spaces
# string.split()    → string → list of words
# " ".join(list)    → list of words → string
# string.replace()  → swap one thing for another
# string.find()     → where does something live?
# string.count()    → how many times does it appear?
# f"text {var}"     → professional string building
# ```
#
# ---
#
# > *A string is a sequence.*
# > *Like a mantra — each syllable in its place.*
# > *Immutable — once spoken, it is what it is.*
# > *But from it, we can always create something new.* 🙏
#
# ---
#
# *FOUNDATION — Chapter 2: Strings and Their Secrets*
# *Written with love — Gurudev & Claude* 🙏 ❤️ 🕉️
