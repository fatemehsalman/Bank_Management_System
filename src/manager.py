class Manager:
    def __init__(self, ID, Password):
        self.ID = ID
        self.Password = Password


    def check_password(self, Password):
        return self.Password == Password

    def change_password(self, new_password):
        self.Password = new_password
        print("Password changed successfully!")
