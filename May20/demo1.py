num = int(input("Enter a number: "))
count = 0
a = 1

while num > 0:
    val = num % 10
    count += val
    num = num // 10

print(count)