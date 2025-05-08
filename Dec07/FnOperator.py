def add():
    print("Addition")
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    print(f"Answer is {a+b}")

def sub():
    print("Subraction")
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    print(f"Answer is {a-b}")

def mul():
    print("Multiply")
    a = int(input("Enter 1st Value: "))
    b = int(input("Enter 2nd Value: "))
    print(f"Answer is {a*b}")

def div():
    print("Division")
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    print(f"Answer is {round(a/b)}")


add()
sub()
mul()
div()