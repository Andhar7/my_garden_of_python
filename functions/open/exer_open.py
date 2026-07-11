
# **Exercise 1 — First Writing**
# Create a file called `peace.txt` and write three lines of your choice into it. Then read it back and print each line.
def create_write_read_print():

    with open("peace.txt", "w", encoding="utf-8") as f:
        f.write("Peace 🕉️\n")
        f.write("Calm 🕉️\n")
        f.write("Stillness 🕉️\n")

    with open("peace.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        reading = [f"Welcome, {line}! 🙏\n" for line in lines]
        for line in lines:
            print(f"Each line: {line}")

        print(f"Here the length of all worlds: {len(reading)}")

create_write_read_print()

# **Exercise 2 — The Log**
# Write a program that appends one line to `log.txt` each time it runs:
# ```
# Run at: 2026-06-16 — Garden session complete 🌸
# ```
# Run it three times. Then read and print the whole log.
def log():

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("Run at: 2026-06-16 — Garden session complete 🌸\n")

    with open("log.txt", "r", encoding="utf-8") as f:
        reading_log = f.read()
        print(reading_log)

log()

# **Exercise 3 — Word Counter**
# Read the file `peace.txt` you created. Count how many words are in the file total.
# *(Hint: split each line into words, sum the word counts.)* 🌿
def read_and_count():

    with open("peace.txt", "r", encoding="utf-8") as f:
        split_lines = sum(len(line.split()) for line in f)

        print(split_lines)

read_and_count()

# **Exercise 5 — Safe Reader**
# Write a function `safe_read(filename)` that:
# - Returns the content of the file if it exists
# - Returns `None` if the file does not exist
# *(Hint: use `try/except` with `FileNotFoundError`.)* 🌿
def safe_read(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None

print(safe_read("peace.txt"))
print(safe_read("some_file.txt"))

def sentence(sent):

    if not sent:
        raise ValueError("No Words")

    sentence_by = len(sent.split())

    return sentence_by

print(sentence("Om Namah Shivaya 🙏"))

# **Exercise 4 — The Transformer**
# Read a file, convert every line to UPPERCASE, and write the result to a new file.
def transformer():

    with open("peace.txt" , "r", encoding="utf-8") as f:
        convert_upper = f.read().upper()

    with open("new_peace_upper.txt", "w", encoding="utf-8") as f:
        f.write(convert_upper)

    with open("new_peace_upper.txt", "r", encoding="utf-8") as f:
        read_from_new_file = f.read()
        print(read_from_new_file)

transformer()






























