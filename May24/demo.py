def greetings():
    print()
    print("\tWelcome to The Bank")
    print()
    print("option 1: Deposite")
    print("option 2: Withdraw")
    print("Option 3: Check Balance")
    print("Option 4: Exit")
    print()
def check_balance(amt):
    bal = amt
    print("Your balance is: ",bal)
def withdraw(with_amt):
    val = int(input("Enter the amount to withdraw: "))
    if val <= 0:
        print("Invalid amount")
        print("Please enter a valid amount")
    else:
        if val > with_amt:
            print("insufficient balance")
            print("Please enter a valid amount")
        else:
            with_amt -= val
            check_balance(with_amt)
def deposite(dept_amt):
    val = int(input("Enter the amount to deposite: "))
    if val <= 0:
        print("Invalid amount")
        print("please enter a valid amount")
    else:
        dept_amt += val
        check_balance(dept_amt)
        print("Deposite sucessfully")
balance = 1000
while True:
    greetings()
    num = int(input("Enter a Option: "))
    match num:
        case 1:
            deposite(balance)
        case 2:
            withdraw(balance)
        case 3:
            check_balance(balance)
        case 4:
            print("Exit")
            break
        case _:
            print("Invalid option")
        