
def confirmation():
        username=input("Username: ")
        password=input("Password: ")
        confusername=input("Confirm Username: ")
        confpassword=input("Confirm Password: ")
        if confpassword==password and confusername==username:
            print("Successfull Confirmation !")
        else:
            print("Something went wrong")
confirmation()