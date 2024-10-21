num1 = int(input("Enter a num1 value here: "))
num2 = int(input("Enter a num2 value here: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print(f"those num are {num1,num2} is equal")
