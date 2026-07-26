

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





















