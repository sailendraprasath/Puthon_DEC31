age = int(input("Enter your Age: "))

if age == 0 or age <= 0:
    print("Invalid age")
elif age >= 1 and age <= 12  :
   print("you are kid")
elif age >= 13 and  age <= 19:
    print("you are teenager")
elif age >= 20 and age <= 35:
    print("you are Adult")
else:
    print("you are Old")