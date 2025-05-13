val = int(input("Enter a value: "))

if val % 3 == 0:
    if val % 5 == 0:
        print("The value is divisible by 3 and 5")
else:
    print("The value is not divisible by 3 and 5")