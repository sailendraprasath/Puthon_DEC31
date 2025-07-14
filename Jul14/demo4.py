#  Find the  second largest numbers in a list

num = [5, 2, 9, 1, 7]
val = num[0]

for i in num:
    if i > val:
        val = i
num.remove(val)
val2 = num[0]

for i in num:
    if i > val2:
        val2 = i

print("Largest number is:", val)
print("Second largest number is:", val2)