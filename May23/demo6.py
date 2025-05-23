def vote():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("you eligible to vote")
    else:
        print("you not eligible to vote")
vote()