from zoneinfo import reset_tzpath

# with open("poem.txt", "r") as file:
#    content = file.read()
    # file is automatically closed here — guaranteed, always
#print(content)
# **The most important distinction:**

#```python
#open("notes.txt", "w")   # ⚠️ ERASES everything in notes.txt first!
open("notes.txt", "a")   # ✅ ADDS to the end of notes.txt
with open("notes.txt", "r") as f:
    content = f.read()
  #  print(content)
# ```

# Always think before writing. The `"w"` mode is irreversible. 🌿
# The file object has several methods:
#
# ```python
# file.read()          # Read the entire file as one string
# file.readline()      # Read one line at a time
# file.readlines()     # Read all lines into a list
# file.write(text)     # Write a string to the file
# file.writelines(lst) # Write a list of strings
# file.close()         # Close the file

open("haiku.txt", "a")
with open("haiku.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())   # strip() removes the \n at the end
        line = f.readline()

### Way 3 — Looping Directly — The Most Pythonic
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# A file object is **iterable** — Python walks through its lines, one at a time. This is the most natural and memory-efficient way.
# For large files, only one line is in memory at a time. 🌿

# Creating or Overwriting
with open("message.txt", "w") as f:
    f.write("Om Namah Shivaja\n")
    f.write("Session started!")

### Appending — Adding Without Erasing
with open("login.txt", "a") as f:
    f.write("Login is success!")

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

## Part 6 — Encoding — Reading Non-English Text
with open("poem.txt", "w", encoding="utf-8") as f:
    f.write("Om Namah Shivaya 🕉️\n")
    f.write("Om Namah Shivaya one more 🕉️\n")



open("names.txt", "a")
with open("names.txt", "r") as f:
    names = [line.strip() for line in f if line.strip()]

# process
greetings = [f"Namaste, {name}! 🙏\n" for name in names]

with open("greetings.txt", "w", encoding="utf-8") as f:
    f.writelines(greetings)

print(f"Wrote {len(greetings)} greetings.")

# It is also the place where humility is required. The file may not exist. The disk may be full. The permissions may be wrong.
# Real programs always prepare for this — with error handling we will meet in a future garden.





















