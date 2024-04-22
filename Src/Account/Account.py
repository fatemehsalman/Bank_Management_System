

class Account:
    def __init__(self, Account_Number:str, Account_Amount:float):
        self.Account_Number = Account_Number
        self.Account_Amount = Account_Amount

        
    def Show_details(self) -> None:
        print(f"Account Number: {self.Account_Number}, Amount: {self.Account_Amount}")