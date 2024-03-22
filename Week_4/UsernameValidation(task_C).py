user = input("Enter the user name: ")
if len(user) < 5:
    print("The user name must be 5 characters long.")
elif not user.isalnum():
    print("Invalid username. The username must not contain any special characters or spaces.")
else:
    print("Valid username")
