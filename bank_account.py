import random

class BankAccount:
    def __init__(self, full_name, account_number = None): #Global to class 
        self.full_name = full_name
        self.balance = 0
        self.account_number = account_number if account_number else self.random_num()
    
    #Account number using random + 8 digits
    def random_num(self):
        return random.randint(10000000,99999999)
    
    # Deposit (balance = balance + amount)
    def deposit(self, amount):
        self.balance += amount 
        print (f"Amount deposited:  ${amount}  new balance:  ${self.balance:.2f}" )
    #Withdraw (balance = balance - withdraw)
    def withdraw(self, amount):
        self.balance -= amount
        print (f"Amount withdrew:  ${amount}  new balance:  ${self.balance:2f}" )
    
    #Print Balance
    def get_balance(self):
        print(f"Your current balance is : ${self.balance:.2f}")
    
    # Add Interest to balance (interest = balance * 8.3% )
    def add_interest(self):
        interest = self.balance * 0.0083
        self.balance +=interest
        print(f"Your current balanace with interest is : ${self.balance:.2f}")    
    # Print statment with blurred account number 
    def print_statment(self):
        print(f"Account Owner: {self.full_name}")
        masked_account_number = "****" + str(self.account_number)[-4:]
        print(f"Account No: {masked_account_number}")
        print(f"Balance: ${self.balance}")
        
        
        
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
account2.get_balance()
account2.withdraw(100)
account2.get_balance()
print("---------Third Example----------")
account3 = BankAccount("Mitchell", account_number = "03141592") 
account3.print_statment()
account3.deposit(400000)
account3.add_interest()
account3.print_statment()
account3.withdraw(150)
account3.print_statment()