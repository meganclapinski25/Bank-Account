import random

class BankAccount:
    def __init__(self, full_name, account_number = None):
        self.full_name = full_name
        self.balance = 0
        self.account_number = account_number if account_number else self.random_num()
    def random_num(self):
        return random.randint(10000000,99999999)
    
    def deposit(self, amount):
        self.balance += amount 
        print (f"Amount deposited:  ${amount}  new balance:  ${self.balance:.2f}" )
    
    def withdraw(self, amount):
        self.balance -= amount
        print (f"Amount withdrew:  ${amount}  new balance:  ${self.balance:2f}" )
    
    def get_balance(self):
        print(f"Your current balance is : ${self.balance:.2f}")
    
    def add_interest(self):
        interest = self.balance * 0.0083
        self.balance -=interest
        print(f"Your current balanace with interest is : ${self.balance:.2f}")    
        
    def print_statment(self):
        print(f"Account Owner: {self.full_name}")
        print(f"Account Number: {self.account_number}")
        print(f" Balance: ${self.balance}")
        
        
        
print("---------First Example-----------")
account1 = BankAccount("Megan Clapinski")
account1.deposit(500)  
account1.withdraw(250)

account1.get_balance()
account1.add_interest()
account1.print_statment()
print("---------Second Example--------")
account2 = BankAccount("Katie Jones")
account2.print_statment()
account2.deposit(1000)
account2.add_interest()
account2.get_bal