""" get the five subject values and average it then go to go or aditional class """

std_name = input("Enter your name here: ")
m1 = int(input("Enter your mark 1: "))
m2 = int(input("Enter your mark 2: "))
m3 = int(input("Enter your mark 3: "))
m4 = int(input("Enter your mark 4: "))
m5 = int(input("Enter your mark 5: "))

total = m1 + m2 + m3 + m4 + m5

avg = total / 5

if avg <= 35:
    print("you have to come Additional Class")
else:
    print(f"your total mark is {total} and Avg is {avg} so you good to goo") 