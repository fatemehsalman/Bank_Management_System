from Src.Bank import Bank

class Branch(Bank):
    def __init__(self, Name:str, Bank_ID:str, City_Name:str):
        super().__init__(Name, Bank_ID)
        self.City_Name = City_Name
        self.number_of_Customers = 0
        self.budget = 0
