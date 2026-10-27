input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if input_username == "Shivam_7090":
    if input_password == "Shiv@7090":
        print("Login Successful")
    else:
        print("Invalid password")
elif input_password == "Shiv@7090":
    print("Invalid username")
else:
    print("Login Failed")

