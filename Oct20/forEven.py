"""count the even num between 1 to 10 using for loop"""
value1 = int(input("Enter a value1 here: "))
value2 = int(input("Enter a value2 here: "))
count=0

for even in range(value1,value2):
    if even % 2 == 0:
        count +=1
print(f"you has given num is {value1} to between {value2} even num is {count} ")