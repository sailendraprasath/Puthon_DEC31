num1 = int(input("Enter a num1: "))
num2 = int(input("Enter a num2: "))

def check_num(a,b):
    if a > b:
        print("num1 is big")
    elif b > a:
        print("num2 is big")
    else:
        print("num1 and num2 are equal")
check_num(num1,num2)