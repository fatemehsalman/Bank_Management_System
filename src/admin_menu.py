"""This is Admin menu """



from src.admin import Admin
from src.read_file import load_data
from src.write_file import save_data


def admin_menu():
    data = load_data()     # Read data from file

    print("\n ********************* This is Admin MENU for BANK MANAHEMENT SYSTEM ****************: ")

    print("1. Add Admin: ")
    print("2. check & change pass: ")
    print("3. Create Account for customer: ")
    print("4. Create Bank:")
    print("5. Create Branch:")
    print("6. list accounts: ")
    print("7. total balance: ")
    print("8. total loan amount: ")
    print("9. toggle loan feature: ")
    print("10. Save data: ")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":

            # get inputs from user
            name = input("Enter Admin's name: ")
            family_name = input("Enter Admin's family name: ")
            national_code = int(input("Enter Admin's national code: "))
            ID = int(input("Enter Admin's ID: "))
            Password = int(input("Enter Admin's password: "))

            # create instance for admin

            admin = Admin(name, family_name, national_code, ID, Password)
            data["Admin"].append(admin.__dict__)


        
        elif choice == "2":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            Password = input("Enter password: ")

            # create instance for admin
            admin_obj = Admin(name, family_name, national_code, ID, Password)


            # Check password by admin
            entered_password = input("Enter password to check: ")
            if admin_obj.check_password(entered_password):
                print("Password is correct!")
            else:
                print("Password is incorrect!")


            # Change password by admin
            new_password = input("Enter new password: ")
            admin_obj.change_password(new_password)
            break 



        elif choice == "3":

            # get inputs from user
            ID = input("Enter Admin's ID: ")
            name = input("Enter customer's name: ")
            family_name = input("Enter customer's family name: ")
            national_code = input("Enter customer's national code: ")
            home_town = input("Enter customer's home town: ")
            account_number = input("Enter account_number: ")

            #This is Create_Account method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    customer_account = admin_obj.Create_Account( name, family_name, national_code, account_number)
                    # data["accounts"].append(customer_account.__dict__)
                    break 
                else:
                    raise ValueError("ID don't find")



        elif choice == "4":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            name = input("Enter Bank's name: ")
            Bank_ID = input("Enter Bank's ID: ")

            #This is Create_Bank method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    bank = admin_obj.Create_Bank(name, Bank_ID)
                    # data["banks"].append(bank.__dict__)
                    break
                else:
                    raise ValueError("ID don't find")



        elif choice == "5":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            name = input("Enter Bank's name: ")
            Branch_ID= input("Enter Branch'ID: ")

            #This is Create_Branch method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    branch = admin_obj.Create_Branch(name, Branch_ID)
                    # data["branchs"].append(branch.__dict__)
                    break
                else:
                    raise ValueError("ID don't find")



        elif choice == "6":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 

            #This is list_accounts method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    list_account = admin_obj.list_accounts()
                    # data["list_account"].append(list_accounts.__dict__)
                    print(list_account)
                    break
                else:
                    raise ValueError("ID don't find")



        elif choice == "7":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 

            #This is total_balance method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    total_balance_account = admin_obj.total_balance()
                    # data["total_balance"].append(total_balance_account.__dict__)
                    print(list_account)
                    break
                else:
                    raise ValueError("ID don't find")



        elif choice == "8":

            # get inputs from user 
            ID = input("Enter Admin's ID: ")

            #This is total_loan_amount method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    total_loan_amount_account = admin_obj.total_loan_amount()
                    # data["total_loan"].append(total_loan_amount_account.__dict__)
                    print(list_account)
                    break
                else:
                    raise ValueError("ID don't find")



        elif choice == "9":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 

            #This is toggle_loan_feature method
            for admin in data["Admin"]:
                if admin["ID"] == ID:
                    admin_obj = Admin(name, family_name, national_code, ID, Password)
                    toggle_loan_features_account = admin_obj.toggle_loan_feature()
                    # data["toggle_loan_features"].append(toggle_loan_features_account.__dict__)
                    print(list_account)
                    break
                else:
                    raise ValueError("ID don't find") 



        elif choice == "10":

            #call function which saves data

            save_data(data)
            break


        else:
            print("Invalid choice")

if __name__ == "__admin_menu__":
    admin_menu()


        












