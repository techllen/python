class Ninja(Pet):
    # implement __init__( first_name , last_name , treats , pet_food , pet )

def __init__(self,first_name,last_name,treats,per_food,pet):
    self.first_name = first_name
    self.last_name = last_name
    self.treats = treats
    self.per_food = per_food
    self.pet = pet
        	
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
def walk(self):
    return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
def feed(self):
    pass
    return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
def bather(self):
    pass
    return self

class Pet:
    # implement __init__( name , type , tricks ):
def __init__(self,name,type,tricks,health,energy):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy
    # implement the following methods:
    # sleep() - increases the pets energy by 25
def sleep(self):
    self.energy += 25
    return self
    # eat() - increases the pet's energy by 5 & health by 10
def eat(self):
    self.energy += 5
    self.health += 10
    return self
    # play() - increases the pet's health by 5
def play(self):
    self.health += 5
    # noise() - prints out the pet's sound
def noise(self):
    print("Sound")
