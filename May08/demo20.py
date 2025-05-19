
while True:
    user_name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    if user_name == "admin" and password == 12345:
        print("login successfully")
        break
    # else:
    #     print("Login failed")
