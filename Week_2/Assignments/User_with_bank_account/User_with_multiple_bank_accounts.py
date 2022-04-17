# Create a file with the User class, including the __init__ and make_deposit methods
class User: 
    def __init__(self,name):
        # Update the User class __init__ method
        self.name = name
        # Make the self.account variable an array to allow the user to open
        # multiple accounts
        self.account = []
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
    
    # this method helps to add new accounts to the user
    def add_account(self,new_account):
        self.account.append(new_account)
        return self
    def choose_account(self):
        for user_account in self.account:
            print(f"User: {self.name}, " + str(user_account))
        return self
    
class BankAccount:
    def __init__(self, int_rate,account_type, balance = 0 ): 
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
    
    # printing a bank account object  
    def __str__(self):
        return str(self.account_type) +" "+"Balance: "+" "+ str(self.balance)
    
    @classmethod
    def print_all_instances(cls,bank_account):
        bank_account.display_account_info()
    
# First user
# opening multiple accounts for the user
user1 = User("Mkami Malcelina")
# adding account to the user and calling a choose method for the user to choose the account
user1.add_account(BankAccount(7.89,"Savings",198)).add_account(BankAccount(13.35,"Checking",15469)).choose_account()
# second user
# opening multiple accounts for the user
user2 = User("Aly Shawari")
# adding account to the user and calling a choose method for the user to choose the account
user2.add_account(BankAccount(8.9,"Performance",9876)).add_account(BankAccount(14.5,"Checking-Platinumz",19143)).choose_account()



