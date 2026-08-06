

# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def eat(self):
        print(f"{self.name} eating")
    
    def sleep(self):
        print(f"{self.name} sleeping")
    
    def info(self):
        print(f"{self.name} is {self.age} years old!") 
    
    def sound(self):
        print(f"{self.name} makes a sound")


# Child class
class Dog(Animal):
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} the {self.breed} says: Wooooof!")
    
    def sound(self):
        print(f"{self.name} says: Wooof!")
        
class Cat(Animal):
    
    def sound(self):
        print(f"{self.name} says : Meowww!")
        
class Bird(Animal):
    
    def sound(self):
        print(f"{self.name} says : Chirp!")
        


# The Test
dog = Dog("Eric", 3, "Golden Retriever")
dog.info()
dog.eat()
dog.sleep()
dog.bark()

# Test of sound
dog = Dog("Eric", 3, "Golden Retriever")
cat = Cat("Whiskers", 5)
bird = Bird("Tweety", 12)

dog.sound()
cat.sound()
bird.sound()
        

