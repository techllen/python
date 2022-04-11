# Create a file with the User class, including the __init__ and make_deposit methods
class User: 
    def __init__(self,name,account_balance):
        self.name = name
        self.account_balance = account_balance
    # Adding deposit functionality
    def make_deposit(self,amount):
        self.account_balance +=amount
        return self
    # Add a make_withdrawal method to the User class
    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    # Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account_balance}")
        return self

    def transfer_money(self,other_user,amount):
        print(F"AFTER TRANSFER {amount} from {self.name} to {other_user.name}")
        print(f"User:{self.name}, Balance:{self.account_balance-amount}")
        print(f"User:{other_user.name}, Balance:{other_user.account_balance+amount}")
        return self

    # Create 3 instances of the User class
user1 = User("Irene Nyange",300)
user2 = User("Malcela Mkami",400)
user3 = User("Majani Kilo",1000)
     
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# 3 deposit
user1.deposit(300).deposit(400).deposit(900).make_withdrawal(600).display_user_balance()
# user1.deposit(400)
# user1.deposit(900)
# 1 withdrawal
# user1.make_withdrawal(600)
# user1.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# 2 deposits
user2.deposit(700).deposit(800).display_user_balance()
# user2.deposit(800)
# user2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# 1 deposit
user3.deposit(1000).make_withdrawal(300).make_withdrawal(200).make_withdrawal(500).display_user_balance().transfer_money(user3,300)

# 3 withdrawals
# user3.make_withdrawal(300)
# user3.make_withdrawal(200)
# user3.make_withdrawal(500)
# user3.display_user_balance()

# user1.transfer_money(user3,300)



