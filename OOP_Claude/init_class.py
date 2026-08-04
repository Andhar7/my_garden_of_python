

class My_Dog: 
    def __init__(self, name, breed="shepherd dog", best_food="meat"):
        self.name = name
        self.breed = breed
        self.best_food = best_food
    
    def introduce_name(self):
        print(f"Welcome {self.name} between us...")
        
    def woof(self):
        print(f"The {self.name} bark - Woooof!!! Woof!!!")
        
    def dog_food(self):
        print(f"The {self.name} like mostly a {self.best_food}")
            
    def fetching(self):
        print(f"The {self.name} is very happy to fetch a ball!!!")
        
    def new_food(self, new_food):
        self.best_food = new_food # Please REMEBER THIS EXCELENT LESSON! ALWAYS UPDATE NEW VALUE!
        print(f"The {self.name} now eatting {self.best_food}")
        
#           🌟 This is Important

#   This small mistake teaches a BIG concept:
#   - Objects have STATE (their attributes)
#   - Methods should MAINTAIN that state
#   - Don't create new attributes — update existing ones

#   This is the foundation of professional OOP! 💪
            
#   You wrote:
#   self.best_food = new_food  # Update, don't create from nothing

#   The Universe does the same!
#   Supreme's STATE = current state of all things
#   Actions update STATE = maintain cosmic order
#   Never create new reality = only transform what exists




my_dog = My_Dog("Eric")
my_dog.introduce_name()
my_dog.woof()
my_dog.dog_food()
my_dog.fetching() 
my_dog.new_food("cake")
my_dog.dog_food() # UPDATE STATE!!!!
