num1 = int(input("Enter num1 value: "))
num2 = int(input("Enter num2 value: "))
num3 = int(input("Enter num3 value: "))

if num1 < num2:
    if num1 < num3:
        print("num1 is the smallest")
    else:
        print("num3 is the smallest")
elif num2 < num3:
    print("num2 is the smallest")
else:
    print("num3 is the smallest")       

