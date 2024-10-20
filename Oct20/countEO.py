"""count the even and odd num between 1 to 10"""
xyz = int(input("Enter a xyz value: "))
zyx = int(input("Enter a zyx value: "))

count = 0
count1 = 0

for Eo in range(xyz,zyx+1):
    if Eo % 2 == 0:
        count += 1
    else:
        count1 += 1

print(f"num of Even is {count} and num of Odd is {count1} ") 


# output is: 5