mark = int(input("Enter your mark: "))

if mark <0 or mark >= 101:
    print("Invalid mark")
elif mark >= 90 and mark <= 100:
    print("Your Grade is A")
elif mark >= 70 and mark <= 89:
    print("Your Grade is B")
elif mark >= 50 and mark <= 69:
    print("Your Grade is C")
elif mark >=0 and mark <= 49:
    print("You are Fail")