# define functions as steps to login

def enter_username(username):
    print("*** Login Page *****")
    print(f"You entered {username}")

def enter_password():
    pword = input('Enter your password: ')
    print(f"You entered ****{pword[-2:]}")

def click_login():
    print("Login was clicked")
    print("You successfully Logged in")

def logout():
    print("logging out....")
    print("You successfully logged out")

