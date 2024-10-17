"""Positive, Negative, or Zero: Create a program that takes a number from the user and prints whether the number is positive, negative, or zero."""
num = int(input("Enter your num: "))

if num > 0:
    print(f"{num} is positive value")
elif num < 0:
    print(f"{num} is Negative value")
else:
    print("The number is zero")