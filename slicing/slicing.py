letters = ["a", "b", "c", "d", "e", "f", "g"]
#           0    1    2    3    4    5    6

print(letters[2:5])  # ["c", "d", "e"]   start=2, stop=5, step=1
print(letters[2:5:2])  # ["c", "e"]        start=2, stop=5, step=2
print(letters[:3])  # ["a", "b", "c"]   start defaults to 0
print(letters[3:])  # ["d", "e", "f", "g"]  stop defaults to end
print(letters[:])  # a full copy — every default used

## Summary — The Essential Map
#
# | Operation | Code | Notes |
# |---|---|---|
# | Basic slice | `seq[1:3]` | stop excluded |
# | Open start | `seq[:3]` | from the beginning |
# | Open stop | `seq[3:]` | to the end |
# | Full copy | `seq[:]` | new object, same contents |
# | Step | `seq[::2]` | every 2nd item |
# | Reverse | `seq[::-1]` | walks backward |
# | Negative bounds | `seq[-3:]`, `seq[:-2]` | counts from the end |
# | Out-of-range | `seq[1:1000]` | clamps silently, never raises |
# | Slice object | `slice(1, 5, 2)` | same thing, storable and reusable |
# | `.indices(len)` | `slice(1,100).indices(3)` | shows the clamped `(start, stop, step)` |
# | Slice assignment | `lst[1:3] = [...]` | lists only — rewrites, can change length |
# | Slice deletion | `del lst[1:3]` | same as assigning `[]` |
# | Under the hood | `obj.__getitem__(slice(...))` | the real mechanism, one method for all |


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Take every 2nd item, starting from 1, stopping before 8
result = numbers[1:8:2]
# Start at 1: take 1
# Jump by 2: take 3
# Jump by 2: take 5
# Jump by 2: take 7
# Next would be 9, but we stop before 8
# Result: [1, 3, 5, 7]

print(result)

### Example 3: The Omitted Values (The Defaults)

# ```python
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# If you omit start, it defaults to the BEGINNING
# result = numbers[:4]  # Same as numbers[0:4]
# Result: [0, 1, 2, 3]

# If you omit stop, it defaults to the END
# result = numbers[6:]  # Same as numbers[6:10]
# Result: [6, 7, 8, 9]

# If you omit both, you get everything
# result = numbers[:]  # Same as numbers[0:10]
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even with step
# result = numbers[::2]  # Start at beginning, go to end, every 2nd item
# Result: [0, 2, 4, 6, 8]

# A palindrome checker
word = "racecar"
if word == word[::-1]:
    print("It's a palindrome!")  # True!

name = "Gurudev"
#       0123456

# First three letters
name[:3]  # "Gur"

# Last three letters
name[-3:]  # "dev"

# Every other letter
name[::2]  # "Grdv"

# Reversed
name[::-1]  # "veduruG"


class MySequence:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        if isinstance(key, slice):
            # A slice was used!
            return self.data[key]
        else:
            # A single index was used
            return self.data[key]

seq = MySequence([1, 2, 3, 4, 5])
print(seq[1:3])
print(type(seq[1:3]))
print(seq[1:3:2])
print(seq[::-1]) # backward
print(seq[2]) # index 2 to give number 3

# **Pattern 1: Remove first and last**
items = [23, 33, 21, 66, 15, 87, 27, 99]
remove_first_last = items[1:-1]
print(remove_first_last)  # Deleted first and last

reversed_items = items[::-1]
print(reversed_items)

every_other = items[::2]
print(every_other)

every_third = items[::3]
print(every_third)

skip_first_two = items[6:]
print(skip_first_two)

get_first_five = items[:5]
print(get_first_five)
































