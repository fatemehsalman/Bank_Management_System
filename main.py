"""This Main Menu"""
from src.admin_menu import admin_menu
from src.customer_menu import customer_menu


def main():

    print("***********************WELCOME TO BANK MANAGEMENT SYSYTEM******************\n")
    print(">> ACCOUNT_TYPE MENU ")
    print("1) Are you Admin: ")
    print("2) Are you Customer:")
    print("3) Exit")

    
    while True:
        choice = int(input("> Please select an option: "))
        
        if (choice == 1):
            admin_menu()


        elif (choice == 2):
            customer_menu()
            break
                     
           
        elif (choice == 3):
            quit()
            break


        else:
            print("!!! Invalid Option! Please read the option carefully !!!\n")

if __name__ == "__main__":
    main()       