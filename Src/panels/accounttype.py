from Src.panels import Admin_login
from Src.panels import customer_Menu


def accounttype_menu ():

    print("***WELCOME TO BANK MANAGEMENT SYSYTEM***\n")
    print(">> ACCOUNT_TYPE MENU ")
    print("1) Admin")
    print("2) Customer")
    print("3) Exit")

    choice = int(input("> Please select an option: "))
    while(choice != '4'):
        if (choice == 1):
            Admin_login()
            pass
            
        elif (choice == 2):
            customer_Menu()
            pass
           
        elif (choice == 3):
            quit()
        else:
            print("!!! Invalid Option! Please read the option carefully !!!\n")

        choice = int(input("> Please select an option: "))

accounttype_menu ()
