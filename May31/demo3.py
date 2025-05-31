num = int(input("Enter a number: "))

a=2
while a < num:
    if num % a == 0:
        print("Not a prime")
        break
    a += 1
else:
    print("prime")