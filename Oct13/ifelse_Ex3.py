"""get input for a number and check whether it is divisible by both 
3 and 5 or not.if yes thern print,the number is divisible
by 3 and 5 else print the number is not divisible by 3 and 5"""

values = int(input("Enter your values: "))

if values % 3 == 0 and values % 5 == 0:
    print(f"{values} its divisible both 3 and 5 return both 0 so crt")
else:
    print(f"{values} its not divisible by 3 and 5 doesn't return 0")
