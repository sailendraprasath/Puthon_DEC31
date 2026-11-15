num = 7
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print(count)
print(bool(count == 2))
if count == 2:
    print("prime")
else:
    print("not prime")