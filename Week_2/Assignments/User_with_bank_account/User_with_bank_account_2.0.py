# Create a file with the User class, including the __init__ and make_deposit methods
class User: 
    def __init__(self,name,account_type):
        # Update the User class __init__ method
        self.name = name
        self.account = BankAccount(account_type,int_rate=2,balance=0)
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
            self.account_type = account_type
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
    
# Create 2 accounts
bankAccount1 = BankAccount(5,100)
bankAccount2 = BankAccount(10,1000)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
bankAccount1.deposit(500).deposit(500).deposit(2000).withdraw(100).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
bankAccount2.deposit(500).deposit(500).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_instances(bankAccount1)
BankAccount.print_all_instances(bankAccount2)
