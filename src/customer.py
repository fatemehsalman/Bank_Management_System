"""This is customer class """


import random
from src.person import Person



class Customer(Person):
    def __init__(self, name, family_name, national_code, home_town):
        super().__init__(name, family_name, national_code)
        self.home_town = home_town
        self.balance = 0
        self.account_number = int(str(random.randint(10000000, 99999999)).zfill(8))
        self.transaction_history = []
        self.loan_limit = 2
        self.loan_taken = 0




    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."



    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"${amount} withdrawn successfully."
        else:
            return "Withdrawal amount exceeded."



    def check_balance(self):
        return f"Available balance: ${self.balance}"



    def check_transaction_history(self):
        return self.transaction_history



    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.balance += amount
            self.loan_taken += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Loan taken: ${amount}")
            return f"Loan of ${amount} taken successfully."
        else:
            return "You have reached the maximum loan limit."



    



        
        



        