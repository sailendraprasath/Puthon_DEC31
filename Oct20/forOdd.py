"""count the odd number between 1 to 10 using for loop"""

num1 = int(input("Enter num1 value here: "))
num2 = int(input("Enter num2 value here: "))
count = 0

for odd in range(num1,num2):
    if odd % 2 != 0:
       count += 1
print(f"the num {num1} to {num2} between the odd count is {count}")