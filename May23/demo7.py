def factorial():
    num = int(input("Enter a nnumber: "))
    count = 1
    while num > 0:
        count *= num
        num -= 1
    print(count)
factorial()