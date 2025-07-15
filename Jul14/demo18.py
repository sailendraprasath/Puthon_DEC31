num = 155

num2 = num
count = 0
while num2 > 0:
    val = num2 % 10
    fact = 1
    for i in range(1,val+1):
        fact *= i
    count += fact
    num2 //= 10

if count == num:
    print("Strong number")      
else:
    print("Not a Strong number")