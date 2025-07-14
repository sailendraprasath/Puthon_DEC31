num = 1234
count = 0
while num > 0:
    val = num  % 10
    count += val
    num //= 10
print("Sum of digits:", count)