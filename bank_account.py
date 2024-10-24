import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.balance = 0
        self.account_number = self.random_num()
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
        
        
        
        
        
account1 = BankAccount("Megan Clapinski")
print(f"Account Owner: {account1.full_name}")
print(f"Account Number: {account1.account_number}")
print(f"Initial Balance: ${account1.balance}")


account1.deposit(500)  


account1.withdraw(250)

##Balace should be 500 -  250 = 250 

##print(f"Updated Balance: ${account1.balance}")
account1.get_balance()