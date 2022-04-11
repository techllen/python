class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # if (int_rate < 0 and int_rate > 99):
            self.int_rate = round(int_rate/100,2)
        # else:
        #     print("Enter Interest Rate between 0 and 99.")
            self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= (amount):
            self.balance -= (amount)
        else:
            print("Insufficient funds:Charging a 5$ fee")
            self.balance -= -5
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        # your code here
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



