num = 145
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    n = digit
    while n > 1:
        fact *= n
        n -= 1
    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print("Strong number")
else:
    print("Not a Strong number")
