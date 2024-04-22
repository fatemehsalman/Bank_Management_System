from Src.Customer import Show_Details
from Src.Customer import Deposit
from Src.Customer import Withdraw
from Src.Customer import Request_Loan
from Src.Customer import Create_Account
from Src.Customer import accounttype_menu




def customer_Menu():
    print(">> Customer MENU:\n")
    print("1. Show All Accounts")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Request Loan")
    print("5. Create Account")
    print("6. Back to Main Menu")
    choice = int(input("Select an option: "))
    
    while(choice != '6'):
        if (choice == 1):
            Show_Details()
        elif(choice == 2):
            Deposit()
        elif(choice == 3):
            Withdraw()
        elif(choice == 4):
            Request_Loan()
        elif(choice == 5):
            Create_Account()    
        elif(choice == 6):
            print("*** Good bye! Have a nice day! ***\n\n")
            accounttype_menu()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        choice = int(input("Select an option: "))

customer_Menu()