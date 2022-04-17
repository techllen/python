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
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("Pet Sound")
        return self
        
# I will create a dog and a cat class which inherits from Pet Class
# All methods will be the same because a dog can sleep,eat,play however it can make noise of different 
# sound and medical conditions

class Dog(Pet):
    # implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks,health,energy,medical_condition):
        # overiding the parent(PET) init method
        super.__init__(self,name,type,tricks,health,energy)
        # adding a medical condition
        self.medical_condition = medical_condition
        
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print("The dog is sleeping")
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print("The dog is eating")
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print("The dog is playing")
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("Woof Woof Woow")
        return self
    
# All methods will be the same because a dog can sleep,eat,play however it can make noise of different 
# sound and medical conditions

class Cat(Pet):
    # implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks,health,energy,medical_condition):
        # overiding the parent(PET) init method
        super.__init__(self,name,type,tricks,health,energy)
        # adding a medical condition
        self.medical_condition = medical_condition
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print("The cat is sleeping")
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print("The cat is eating")
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print("The cat is playing")
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("Meow Meow Meow")
        return self
    

        
