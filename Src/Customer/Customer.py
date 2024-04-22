from Src.User import User
from Src.panels import Customer_Menu


class Customer(User):
    def __init__(self, Name: str, Family_Name: str, National_Code: str, Home_Town: str):
        super().__init__(Name, Family_Name, National_Code)
        self.Home_Town = Home_Town
        self.Accounts = []
        self.loan_number = None

    def Show_All_Accounts(self, National_Code: str) -> None:

        current_balance=0
        print("\nYou choose '1. View Transaction'")
        print("----------------------------------")
        with open('Data.json', 'r') as file:
            data = json.load(file)
        print(data['accounts'][self.national_code])
        print(">> Current Balance: ",current_balance)
        print("--- Return to Customer Menu ---\n\n")
        Customer_Menu()



    def Deposit(self, account_number: str, amount: float) -> None:
        print("\nYou choose '2. Deposit'")
        print("----------------------------------")
        with open('Data.json', 'r') as file:
            data = json.load(file)
        data['accounts'][self.national_code]['balance'] += amount
        with open('Data.json', 'w') as file:
            json.dump(data, file)
            print("*** BALANCE SUCSSESFULLY DEPOSIT! ***")
            print("--- Return to Customer Menu ---\n")
            Customer_Menu()
            return True
        print("!!! You enter wrong ID or Password !!!")
        print("--- Return to Customer Menu ---\n\n")
        Customer_Menu()
        return False

    def Withdraw(self, account_number: str, amount: float) -> None:
        print("\nYou choose '3. Withdrawal'")
        print("----------------------------------")
        with open('Data.json', 'r') as file:
            data = json.load(file)
        if data['accounts'][self.national_code]['balance'] - amount >= 30000:
            data['accounts'][self.national_code]['balance'] -= amount
            with open('Data.json', 'w') as file:
                json.dump(data, file)
        else:
            print("Minimum balance requirement not met.")

            Customer_Menu()
            return True
        print("!!! You enter wrong ID or Password !!!")
        print("--- Return to Customer Menu ---\n\n")
        Customer_Menu()
        return False


    # def Request_Loan(self, national_code: str, account_number: str, loan_amount: float) -> None:
    #     # Logic to request a loan from the specified branch
    #     pass


    # def Create_Account():
    #     pass