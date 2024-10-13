""" get input for a number and find its even or odd """

getValue = int(input("Enter yoour number: "))

if getValue % 2 == 0:
    print(f"{getValue} is a Even Number")
else:
    print(f"{getValue} is a Odd Number")