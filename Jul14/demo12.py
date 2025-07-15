#  Remove Duplicates From la list

nums = [1, 2, 2, 3, 4, 4, 5]
num2 = []

for i in nums:
    if i not in num2:
        num2.append(i)
print("List after removing duplicates:", num2)