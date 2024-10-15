"""build a mini calculator"""
value1 = int(input("Enter a num 1: "))
value2 = int(input("Enter a num 2: "))

option = input("Enter add,sub,mul,div: ")

if option.lower() == "add":
    print(f"{value1 + value2} this is your Addition Answer")

elif option.lower() == "sub":
    print(f"{value1 - value2} this is your Subract Answer")

elif option.lower() == "mul":
    print(f"{value1 * value2} this is your Multiply Answer")

elif option.lower() == "div":
    print(f"{round(value1 / value2 , 2)} this is your Division Answer")
else:
    print("ERROR: check and write your given option...!!")