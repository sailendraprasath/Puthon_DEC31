num = [12,4,5,6,21,4]

largest = num[0]

for i in num:
    if i > largest:
        largest = i

print(largest)
num.remove(largest)
sec_largest = num[0]
for i in num:
    if i > sec_largest:
        sec_largest = i

print("2nd largest",sec_largest)