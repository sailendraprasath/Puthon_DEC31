# Amstrong 

num = 153
count = 0
num2 = num

while num2 > 0:
    val = num2 % 10
    count += val ** 3
    num2 //= 10

if count == num:
    print("Amstrong")
else:
    print("Not Amstrong")