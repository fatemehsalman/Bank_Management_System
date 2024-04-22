from Src.panels import Admin_menu


def Admin_login():
    print("\n+++ Admin Login Menu +++")

    admin_ID = str(input("> Enter Your Admin ID: "))
    admin_Pass = str(input("> Enter your Password: "))

    admin_file = open("admin_db,txt", "r")
    for line in admin_file:
        login_admin = line.strip().split(",")
        if (admin_ID == login_admin[0] and admin_Pass == login_admin[2]):
            print("\n\n=== WELCOME, "<login_admin[1], "===")
            Admin_menu()
            return True
        
    print("!!! You enter wrong ID or Password !!!")
    print("--- Return to Admin Login ---\n\n")
    Admin_login()
    return False
Admin_login()       
