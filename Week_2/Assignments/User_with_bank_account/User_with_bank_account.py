# Create a file with the User class, including the __init__ and make_deposit methods
class User: 
    def __init__(self,name):
        # Update the User class __init__ method
        self.name = name
        self.account = BankAccount(int_rate=2,balance=0)
        # Update the User class make_deposit method
    def make_deposit(self,amount):
        self.account +=amount
        return self
        # Update the User class make_withdrawal method
    def make_withdrawal(self,amount):
        self.account -=amount
        return self
        # Update the User class display_user_balance method
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account}")
        return self
    def transfer_money(self,other_user,amount):
        print(F"AFTER TRANSFER {amount} from {self.name} to {other_user.name}")
        print(f"User:{self.name}, Balance:{self.account-amount}")
        print(f"User:{other_user.name}, Balance:{other_user.account+amount}")
        return self
    
class BankAccount:
    def __init__(self, int_rate,account_type, balance = 0): 
            self.int_rate = round(int_rate/100,2)
            self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= (amount):
            self.balance -= (amount)
        else:
            print("Insufficient funds:Charging a 5$ fee")
            self.balance -= -5
        return self
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self
    
    @classmethod
    def print_all_instances(cls,bank_account):
        bank_account.display_account_info()
    

