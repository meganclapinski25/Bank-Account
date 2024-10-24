import random

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.balance = 0
        self.account_number = random_num()
    def random_num():
        return random.randint(10000000,99999999)