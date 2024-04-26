"""This is Admin class """""

from src.manager import Manager
from src.person import Person
from src.bank import Bank
from src.branch import Branch
from src.customer import Customer




class Admin(Person, Manager):
    def __init__(self, name, family_name, national_code, ID, Password):
        Person.__init__(self, name, family_name, national_code)
        Manager.__init__(self, ID, Password)
        self.user_accounts = []
        self.banks_id = []
        self.branchs_id =[]



    def Create_Account(self, name, family_name, national_code, home_town, account_number):    
        accounts = Customer(name, family_name, national_code, home_town, account_number)
        self.user_accounts.append(accounts)
        return accounts

        
 


    def Create_Bank(self, name, Bank_ID):
        bank = Bank(name, Bank_ID)
        self.banks_id.append(bank)
        return bank



    def Create_Branch(self, name, Branch_ID):
        branch = Branch(name, Branch_ID)
        self.branchs_id.append(branch)
        return bank



    def list_accounts(self):
        return self.user_accounts



    def total_balance(self):
        total_balance = sum(account.balance for account in self.user_accounts)
        return f"Total balance : ${total_balance}"



    def total_loan_amount(self):
        total_loan = sum(account.loan_taken for account in self.user_accounts)
        return f"Total loan amount : ${total_loan}"




    def toggle_loan_feature(self, enable=True):
        for account in self.user_accounts:
            account.loan_limit = 2 if enable else 0
        return "Loan feature enabled" if enable else "Loan feature disabled"


    


    