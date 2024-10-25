"""Even or Odd:Write a program to check whether a number entered by the user is even or odd."""
value = int(input("Enter a Number: "))

if value % 2 == 0:
    print(f"{value} is Even")
else:
    print(f"{value} is Odd")