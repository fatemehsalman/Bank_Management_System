import json

from Src.User import User
from Src.panels import Admin_menu



class Admin(User):
    def __init__(self, Name: str, Family_Name: str, National_Code: str, password: str):
        super().__init__(Name, Family_Name, National_Code)
        self.password = password
        self.banks = {}
        self.branches = {}

    def Create_Bank (self, Bank_Name, Bank_Number) :
        print("\n You choose '1) Create Bank'")
        print("-------------------------------")
        self.banks[Bank_Name] = Bank_Number
        with open('Data.json', 'w') as file:
            json.dump(self.banks, file)

        print("*** NEW BANK CREATED! ***")
        print("--- RETURN TO ADMIN MENU ---\n")

        Admin_menu()
        


    def Create_Branch(self, Branch_name, Branch_number):
        print("\nYou choose '2. Create NEW Branch'")
        print("----------------------------------")
        self.branches[Branch_name] = Branch_number
        with open('Data.json', 'w') as file:
            json.dump(self.branches, file)
        print("*** NEW BRANCH CREATED! ***")
        print("--- RETURN TO ADMIN MENU ---\n")
        Admin_menu()
            
        

    def Create_Account(self, Customer_Name, Customer_Family_Name, Customer_National_Code, Branch_Name, Initial_Balance) :
        print("\nYou choose '3. Create NEW Account'")
        print("----------------------------------")
        account_data = {
            "Name": Customer_Name ,
            "Family_Name": Customer_Family_Name,
            "National_Code": Customer_National_Code,
            "Branch": Branch_Name,
            "Balance": Initial_Balance
        }
        with open('Data.json', 'w') as file:
            json.dump(account_data, file)
        print("*** NEW ACCOUNT CREATED! ***")
        print("--- RETURN TO ADMIN MENU ---\n")

        Admin_menu()


    def Approve_Loan_Request(self, Loan_Amount):
        if account_balance >= 30000 and branch_budget <= 1000000000:
            return True
        return False
        

    # def Set_Branch_Budget ():
    #     pass

    # def Display_Information ():
       
    #     pass

    # def Update_Branch_Budget():
    #     pass

    # def Change_Password():
    #     pass

