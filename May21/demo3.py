num = 153

count = 0
store = 0

while num > 0:
    store = num % 10
    for i in range(1):
        count += store ** 3
    num = num // 10

if count == num:
    print("Armstrong")
else:
    print("Not Armstrong")