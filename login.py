# Initialize empty username and password variables
username = ""
password = ""

# Ask the user to set a username and password
while not username:
    username = input("Set your username: ")

while not password:
    password = input("Set your password: ")

print("Username and password set successfully!")

# Ask the user to log in
login_attempts = 3

while login_attempts > 0:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    
    if entered_username == username and entered_password == password:
        print("Login successful!")
        break
    else:
        login_attempts -= 1
        print(f"Incorrect username or password! You have {login_attempts} attempts left.")

if login_attempts == 0:
    print("Out of login attempts. Access denied.")
