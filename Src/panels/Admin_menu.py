from Src.Admin import Create_Bank 
from Src.Admin import Create_Branch
from Src.Admin import Create_Account
from Src.Admin import Approve_Loan_Request
from Src.Admin import Set_Branch_Budget 
from Src.Admin import Display_Information 
from Src.Admin import Update_Branch_Budget
from Src.Admin import Change_Password
from Src.panels import accounttype_menu






def Admin_menu():
    print("\n>> Admin MENU:")
    print("1. Create Bank")
    print("2. Create Branch")
    print("3. Approve Loan Request")
    print("4. Set Branch Budget")
    print("5. Display Information")
    print("6. Update Branch Budget")
    print("7. Change Password")
    print("8. Back to Main Menu")
    choice = int(input("Select an option: "))

    while(choice != '9'):
        if (choice == 1):
            Create_Bank ()
        elif (choice == 2):
            Create_Branch ()
        elif (choice == 3):
            Approve_Loan_Request()
        elif (choice == 4):
            Set_Branch_Budget ()
        elif (choice == 5):
            Display_Information()
        elif (choice == 6):
            Update_Branch_Budget()
        elif (choice == 7):
            Change_Password ()
        elif (choice == 8):
            Create_Account ()
        elif (choice == 9):
            print("=== GOOD BYE, SEE YOU AGAIN! ===\n\n")
            accounttype_menu()
        else:
            print ("!!! Invalid Option! Please read the option carefully! !!!\n")
        choice = int(input("Select an option: "))

Admin_menu()