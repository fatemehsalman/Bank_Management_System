"""This is customer menu """



from src.customer import Customer
from src.read_file import load_data
from src.write_file import save_data


def customer_menu():
    data = load_data()     # Read data from file

    print("\n ********************* This is Customer MENU for BANK MANAHEMENT SYSTEM ****************: ")

    print("1. Add Customer: ")
    print("2. Deposit: ")
    print("3. withdraw: ")
    print("4. check_balance:")
    print("5. check_transaction_history:")
    print("6. take_loan: ")
    print("7. Save data: ")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":

            # get inputs from user
            name = input("EnterCustomer's name: ")
            family_name = input("Enter Customer's family name: ")
            national_code = int(input("Enter Customer's national_code: "))
            home_town = input("Enter Customer's home_town: ")
            

            # create instance for customer

            customer = Customer(name, family_name, national_code, home_town)
            data["Customer"].append(customer.__dict__)


        
        elif choice == "2":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            family_name = input("Enter family_name: ")
            account_number = input("Enter account_number: ")
            deposit_amount= input("Enter amount of deposit: ")

            # This is deposit method
            for customer in data["Customer"]:
                if customer["account_number"] == account_number:
                    customer_obj = Customer(name, family_name, national_code, home_town)
                    deposit_to_account = customer_obj.deposit( deposit_amount)
                    break
                else:
                    raise ValueError("account number don't find")
            



        elif choice == "3":
            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            family_name = input("Enter family_name: ")
            account_number = input("Enter account_number: ")
            withdraw_amount= input("Enter amount of withdraw: ")

            # This is deposit method
            for customer in data["Customer"]:
                if customer["account_number"] == account_number:
                    customer_obj = Customer(name, family_name, national_code, home_town)
                    withdraw_to_account = customer_obj.withdraw(withdraw_amount)
                    break
                else:
                    raise ValueError("account number don't find") 

            



        elif choice == "4":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            family_name = input("Enter family_name: ")
            account_number = input("Enter account_number: ")
            

            # This is check_balance method
            for customer in data["Customer"]:
                if customer["account_number"] == account_number:
                    customer_obj = Customer(name, family_name, national_code, home_town)
                    balance_cheker = customer_obj.check_balance()
                    print(balance_cheker)
                    break
                else:
                    raise ValueError("account number don't find") 

            


        elif choice == "5":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            family_name = input("Enter family_name: ")
            account_number = input("Enter account_number: ")
            

            # This is check_transaction_history method
            for customer in data["Customer"]:
                if customer["account_number"] == account_number:
                    customer_obj = Customer(name, family_name, national_code, home_town)
                    transaction_history_cheker = customer_obj.check_transaction_history()
                    print(transaction_history_cheker)
                    break
                else:
                    raise ValueError("account number don't find") 



        elif choice == "6":

            # get inputs from user
            ID = input("Enter Admin's ID: ") 
            family_name = input("Enter family_name: ")
            account_number = input("Enter account_number: ")
            Branch_ID = input("Enter Branch's ID")
            loan_amount= input("Enter amount of loan: ")

            # This is deposit method
            for customer in data["Customer"]:
                if customer["account_number"] == account_number:
                    customer_obj = Customer(name, family_name, national_code, home_town)
                    take_loan_from_account = customer_obj.take_loan(loan_amount)
                    break
                else:
                    raise ValueError("account number don't find")  

            



        elif choice == "7":

            #call function which saves data

            save_data(data)
            break


        else:
            print("Invalid choice")

if __name__ == "__customer_menu__":
    customer_menu()