import math

class Bowl:
    
    def __init__(self, material, diametr_cm):
        self.material = material
        self.diametr_cm = diametr_cm
        
    def describer(self):
        return f"A {self.material} of bowl and {self.diametr_cm}cm across"

clay_of_bowl = Bowl("clay", 21)
wooden_bowl = Bowl("wood", 27)

print(clay_of_bowl)
print(wooden_bowl)
print(clay_of_bowl.describer())
print(wooden_bowl.describer())



class Meditator:
    
    tradition = "Sri Chinmoy" # **Class variables** — shared by all instances, defined at class level:

    
    def __init__(self, name, years): # Instance of variables
        self.name = name
        self.years = years
        
    
gurudev = Meditator("Andrej", 20)
arjuna = Meditator("Gurudev", 333)

print(gurudev.tradition)
print(arjuna.tradition)
print(Meditator.tradition)

Meditator.tradition = "Vedanta" # Class attribuite
print(gurudev.tradition)

gurudev.tradition = "Zen" # Instance attribuite
print(gurudev.tradition)
print(arjuna.tradition)

# 🌿 Instance attributes shadow class attributes — they never modify them.

class Meditation:
    
    def __init__(self, name, years):
        self.name = name
        self.years = years
        self.completed_session = 0
        
    def sit(self, minutes=21):
        """Complete one meditation session."""
        self.completed_session += 1
        return f"{self.name} sat for {minutes} and session completed at #{self.completed_session}"
    
    def progress_of_meditation(self):
        """Return a summary of practice progress."""
        total_hours = self.completed_session * 21 / 60  
        return(
            f"{self.name} - {self.years} years of practice\n"
            f"Session completed in : {self.completed_session}\n"  
            f"Total hours is : {total_hours:.1f} hours\n"
        )
gurudev_meditation = Meditation("Gurudev", 21)

print(gurudev_meditation.sit())
print(gurudev_meditation.sit(33))
print(gurudev_meditation.progress_of_meditation())


## Part 6 — `@property` · Computed Attributes
# `@property` (our preview from decorators!) makes a method behave like an attribute.
# The caller does not need to know whether they are reading a stored value or a computed one:
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    @property
    def diameter(self) -> float:
        """ Diametr twice of the radius """
        return self.radius * 2
    
    @property
    def area(self) -> float:
        return round(math.pi * self.radius ** 2, 4)
    
    @property
    def circumference(self) -> float:
        return round(2 * math.pi * self.radius, 4)
    
c = Circle(5)
print(c.radius)         # 5       ← stored attribute
print(c.diameter)       # 10      ← computed, but looks like an attribute
print(c.area)           # 78.5398
print(c.circumference)  # 31.4159

c.radius = 10           # change the radius
print(c.diameter)       # 20      ← automatically updated — always derived from radius

# Without `@property`, callers would write `c.area()` — calling it as a function.
# With `@property`, they write `c.area` — reading it as an attribute.

# The implementation detail (stored vs computed) is hidden. This is **encapsulation**. 🌿

### The Setter — Controlling How Values Are Written
class Temperature:
    
    def __init__(self, celsius:float):
        self._celsius = celsius  # _underscore means "private by convention"
        
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError(
                "Temerature can´t be below absolute zero!"
            )  
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32
    
t = Temperature(100)
print(t.celsius)      # 100
print(t.fahrenheit)   # 212.0

t.celsius = 20        # uses the setter
print(t.fahrenheit)   # 68.0

# t.celsius = -300      # ValueError: Temperature cannot be below absolute zero!

# The setter lets us **validate** values before storing them.
# External code writes `t.celsius = 20` — clean and natural.
# The validation happens invisibly inside. 🙏

## Part 7 — `@staticmethod` · Utility Without `self`

# A static method belongs to the class but needs no instance or class:

class MathHelper:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if n is a prime number."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def clamp(value: float, low: float, high: float) -> float:
        """Return value clamped between low and high."""
        return max(low, min(value, high))


print(MathHelper.is_prime(17))      # True  — no instance needed
print(MathHelper.clamp(150, 0, 100)) # 100
# ```

# Use `@staticmethod` when a function logically belongs to a class
# but does not need to access `self` or `cls`. 🌿


## Part 8 — `@classmethod` · Alternative Constructors
# A class method receives the **class itself** as its first argument (`cls` by convention):

class Meditator:
    def __init__(self, name: str, years: int, tradition: str = "Sri Chinmoy"):
        self.name      = name
        self.years     = years
        self.tradition = tradition

    @classmethod
    def beginner(cls, name: str) -> "Meditator":
        """Create a new meditator with 0 years of practice."""
        return cls(name, years=0)

    @classmethod
    def from_dict(cls, data: dict) -> "Meditator":
        """Create a Meditator from a dictionary (e.g. from JSON)."""
        return cls(
            name      = data["name"],
            years     = data.get("years", 0),
            tradition = data.get("tradition", "Sri Chinmoy"),
        )

    def __repr__(self):
        return f"Meditator(name={self.name!r}, years={self.years}, tradition={self.tradition!r})"


# Three ways to create a Meditator:
m1 = Meditator("Gurudev", 18)
m2 = Meditator.beginner("Arjuna")
m3 = Meditator.from_dict({"name": "Devaki", "years": 12})

print(m1)   # Meditator(name='Gurudev', years=18, tradition='Sri Chinmoy')
print(m2)   # Meditator(name='Arjuna', years=0, tradition='Sri Chinmoy')
print(m3)   # Meditator(name='Devaki', years=12, tradition='Sri Chinmoy')
# ```

# `@classmethod` shines as an **alternative constructor** —
# multiple clean ways to create an instance from different data sources. 🌺

## Part 9 — A Complete Example

from datetime import datetime
import math


class Crop:
    """Represents a single crop in a farm."""

    # Class variable — shared knowledge:
    SEASONS = {1: "winter", 2: "winter", 3: "spring", 4: "spring",
               5: "spring", 6: "summer", 7: "summer", 8: "summer",
               9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}

    def __init__(self, name: str, planted_kg: float, season: str):
        self.name       = name
        self.planted_kg = planted_kg
        self.season     = season
        self.harvested  = False
        self._harvest_kg: float | None = None

    @classmethod
    def from_current_season(cls, name: str, planted_kg: float) -> "Crop":
        """Plant a crop in the current calendar season."""
        month  = datetime.now().month
        season = cls.SEASONS[month]
        return cls(name, planted_kg, season)

    @property
    def yield_ratio(self) -> float | None:
        """Harvest / planted ratio, or None if not yet harvested."""
        if self._harvest_kg is None:
            return None
        return round(self._harvest_kg / self.planted_kg, 2)

    def harvest(self, kg: float):
        """Record the harvest amount."""
        if kg < 0:
            raise ValueError("Harvest cannot be negative.")
        self._harvest_kg = kg
        self.harvested   = True

    @staticmethod
    def estimate_yield(planted_kg: float, factor: float = 3.0) -> float:
        """Estimate expected harvest from planted amount."""
        return planted_kg * factor

    def __repr__(self) -> str:
        status = f"harvested {self._harvest_kg}kg" if self.harvested else "growing"
        return f"Crop({self.name!r}, {self.season}, {status})"


wheat = Crop("wheat", 100, "spring")
wheat.harvest(310)

rice = Crop.from_current_season("rice", 50)

print(wheat)              # Crop('wheat', spring, harvested 310kg)
print(wheat.yield_ratio)  # 3.1
print(rice)               # Crop('rice', summer, growing)

print(Crop.estimate_yield(100))   # 300.0



























