



word = "Python"
print(word[:-1]) # Pytho
print(word[-1:]) # n
print(word[:4]) # Pyth
print(word[4:]) # on - characters from position 4 (included) to the end
print(word[:-4]) # Py
print(word[-4:]) # thon
print(word[:4] + word[4:]) # Python

print(word[0:5]) # characters from position 0 (included) to 2 (excluded) - Pytho
print(word[2:5]) # characters from position 2 (included) to 5 (excluded) - tho
word[-2:]  # characters from the second-last (included) to the end - on
word[4:]   # characters from position 4 (included) to the end - on

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[-4:]) # Python

print(word[:2] + 'py')

name = "Andrej Kling"
print(name[-3:] + 'new')

