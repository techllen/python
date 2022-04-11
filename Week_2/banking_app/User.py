# class User:		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0
        
        
# guido = User()
# minty = User()

# print(guido.name)
# print(minty.name)

# guido.email = "kilo"
# minty.account_balance = 200

# print(minty.account_balance)

# class User2:
#     bank_name = "First National Bank"
    
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# kilo = User2()
# majani = User2()

# User2.bank_name = "Capital One"
# majani.bank_name = "American Express"

# print(User2.bank_name)
# print(majani.bank_name)



class User2:
    bank_name = "First National Bank"
    population = 0;
    
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.account_balance = 0
        User2.population +=1
        
    def greeting(self):
        print(f"Hellow {self.name}")
        
    def deposit(self,amount):
        self.account_balance +=amount
    @classmethod
    def user_population(cls):
        print(f"{cls.population} users in the program")
        
    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid

kilo = User2("Pilika","kalipo@yah.com",30)

kilo.greeting()

kilo.deposit(200)

print(kilo.account_balance)

# calling a class method
User2.user_population()

# calling a static method
print(User2.validate_age(12))