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
        return ("Amount deposited: + ${amount} + new balance: + ${self.balance}" )
    
    
account1 = BankAccount("Megan Clapinski")
print(f"Account Owner: {account1.full_name}")
print(f"Account Number: {account1.account_number}")
print(f"Initial Balance: ${account1.balance}")


account1.deposit(500)  


print(f"Updated Balance: ${account1.balance}")