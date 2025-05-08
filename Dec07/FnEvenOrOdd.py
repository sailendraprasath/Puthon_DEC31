value = int(input("Enter a number: "))

def EvenOrOdd():
    if value % 2 == 0:
        print(f"The value of {value} is EVEN")
    else:
        print(f"The value of {value} is ODD")

EvenOrOdd()