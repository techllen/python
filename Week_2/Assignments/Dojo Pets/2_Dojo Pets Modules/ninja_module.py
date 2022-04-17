# Importing external module
import pet_module as PetModule
# Translating external module to a single name
Pet = PetModule.Pet
class Ninja(Pet):
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print("Walking the Pet")
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        print(f"Feeding {self.pet_food}")
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
# initializing an instance of a pet
pet1 = Pet("Rusty","Dog","Roll Over",100,30)
# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
ninja1 = Ninja("Irene","Nyange","Milk Bone","Pedigree",pet1)
# Have the Ninja feed, walk , and bathe their pet.
ninja1.feed().walk().bathe()
