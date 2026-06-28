

# **Exercise 1 — The Scoreboard**
#
# ```python
names  = ["Arjuna", "Devaki", "Rohan", "Priya"]
scores = [88, 95, 72, 91]
# ```
# Using `zip`, print each person with their score:
# ```
# Arjuna: 88
# Devaki: 95
# Rohan:  72
# Priya:  91
# ```
def scoreboard(lst_1, lst_2):

    if not lst_1:
        raise ValueError("The list_1 is empty")
    if not lst_2:
        raise ValueError("The list_2 is empty")

    for name, score in zip(lst_1, lst_2):
        print(f"{name}: {score}")

scoreboard(names, scores)


# **Exercise 2 — The Dictionary Garden**
#
# From these two lists, build a dictionary in one line using `dict(zip(...))`:
# ```python
keys   = ["crop",   "season", "water",   "harvest"]
values = ["lentil", "spring", "weekly",  "June"   ]
# ```
# Expected: `{"crop": "lentil", "season": "spring", "water": "weekly", "harvest": "June"}`

created_dict = dict(zip(keys, values))
print(created_dict)

# **Exercise 3 — Morning and Evening**
#
# Two measurements were taken of the same mountain path each day:
# ```python
morning = [1200, 1350, 1480, 1620, 1750]
evening = [1195, 1360, 1475, 1630, 1750]
# ```
# Using `zip`, print each pair and whether the morning or evening reading was higher (or equal):
# ```
# morning 1200 / evening 1195 → morning higher
# morning 1350 / evening 1360 → evening higher
# ...
# ```
def the_highest(lst_1, lst_2):

    if not lst_1:
        raise ValueError("The list_1 is empty")
    if not lst_2:
        raise ValueError("The list_2 is empty")

    for morn, even in zip(lst_1, lst_2):
        if morn > even:
            sign = "morning higher"
        elif morn < even:
            sign = "evening higher"
        else:
            sign = "equal"

        print(f"Morning is: {morn} / evening is: {even} -> {sign}")

the_highest(morning, evening)


# **Exercise 4 — Three Rivers**
#
# ```python
rivers    = ["Rhine",    "Rhône",    "Aare",          "Inn"     ]
lengths   = [1230,       812,        288,              517       ]
countries = ["Germany",  "France",   "Switzerland",   "Austria" ]
# ```
# Using `zip` with three sequences, print one line per river:
# ```
# Rhine: 1230 km, flows through Germany
# Rhône: 812 km, flows through France
# Aare: 288 km, flows through Switzerland
# Inn: 517 km, flows through Austria
# ```
def three_rivers(river_1, river_2, river_3):

    if not river_1:
        raise ValueError("The list of river_1 is empty")
    if not river_2:
        raise ValueError("The list of river_2 is empty")
    if not river_3:
        raise ValueError("The list of river_3 is empty")

    for river, length, country in zip(river_1, river_2, river_3):
        print(f"{river} is: {length} km, flows through {country}")

three_rivers(rivers, lengths, countries)


# **Exercise 5 — The Unzip**
#
# You receive a list of coordinate pairs for Swiss cities:
# ```python
coordinates = [
    (8.55, 47.37),
    (7.45, 46.95),
    (6.15, 46.20),
]
# ```
# Using `zip(*coordinates)`, separate them into two tuples:
# - `longitudes` → `(8.55, 7.45, 6.15)`
# - `latitudes`  → `(47.37, 46.95, 46.20)`
#
# Print each clearly.
#
# Then, as a **bonus**: which city has the westernmost position — the smallest longitude?
# The city names are `["Zürich", "Bern", "Geneva"]`.
longitudes, latitudes = zip(*coordinates)
print(f"longitudes  ->  {longitudes}")
print(f"latitudes  ->  {latitudes}")

cities = ["Zürich", "Bern", "Geneva"]

def cities_position(lst1, lst2, lst3):

    if not lst1:
        raise ValueError("The list1 is empty")
    if not lst2:
        raise ValueError("The list2 is empty")
    if not lst3:
        raise ValueError("The list3 is empty")

    for long, lat, city in zip(lst1, lst2, lst3):
        print(f"{city} has longitudes: {long} and latitudes: {lat}")

    west_long, west_city = min(zip(lst1, lst3))
    print(f"Westernmost city: {west_city} at longitude {west_long}")

cities_position(longitudes, latitudes, cities)







































