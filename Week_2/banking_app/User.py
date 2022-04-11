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
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def greeting(self):
        print(f"Hellow {self.name}")
        
    def deposit(self,amount):
        self.account_balance +=amount

kilo = User2("Pilika","kalipo@yah.com")

kilo.greeting()

kilo.deposit(200)

print(kilo.account_balance)