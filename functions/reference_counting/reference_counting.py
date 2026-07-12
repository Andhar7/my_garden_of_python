

def add_item(value, collections=[]):
    collections.append(value)
    return collections

result1 = add_item("first")
result2 = add_item("second")
result3 = add_item("third")

print(result1)   # ['first', 'second', 'third'] ← SURPRISE!
print(result2)   # ['first', 'second', 'third']
print(result3)   # ['first', 'second', 'third']

# **Why?**
#
# The default `[]` is created **once** when Python reads the function definition.
# It lives in memory with its reference count held by the function itself.
# Every call that uses the default is using the **same object** — never a fresh one.

def add_item_none(value, collections=None):
    if collections is None:
        collections = []    # fresh list created each call
        collections.append(value)
    return collections

result1 = add_item_none("first")
result2 = add_item_none("second")
result3 = add_item_none("third")

print(result1)   # ['first' ]
print(result2)   # ['second' ]
print(result3)   # ['third' ]
# Understanding reference counting explains WHY mutable defaults are dangerous.
# Not as a rule to memorize — but as a truth you now understand. 🙏

a = [2, "s", True]
b = [False, 333, "memory"]
c = a
print(a.append(b))
print(b.append(a))
print(a)
print(b)
print(c)






