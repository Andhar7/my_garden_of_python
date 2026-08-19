

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound")
    
    def eat(self):
        print(f"{self.name} is eating")
    
class Dog(Animal):
    
    def sound(self):
        print(f"{self.name} says Woooffff!")
        
    def fetch(self):
        print(f"{self.name} fetching!")
        
class Cat(Animal):
    
    def sound(self):
        print(f"{self.name} says : Weowww!")
    
class Bird(Animal):
    
    def sound(self):
        print(f"{self.name} says: Chirk!")


class Zoo:
    
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def make_all_sounds(self):
        for animal in self.animals:
            animal.sound() # Polymorthizm
            
    def feed_all(self):
        for animal in self.animals:
            animal.eat() # Polymorthizm

zoo = Zoo()
zoo.add_animal(Dog("Eric"))
zoo.add_animal(Cat("Bady"))
zoo.add_animal(Bird("Cucki"))

print("=============== All animals speak =================")
zoo.make_all_sounds()

print("=============== All animals eat =================")
zoo.feed_all()