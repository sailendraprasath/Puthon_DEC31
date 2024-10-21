"""Check if a number is divisible by both 5 and 11"""
num = int(input("Enter a num1 value here: "))


if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by 5 and 11")
else:
    print("these are not divisible by 5 and 11")