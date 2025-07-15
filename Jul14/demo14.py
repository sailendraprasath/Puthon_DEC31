#  Find max and min in a list

nums = [23, 11, 45, 9, 34]
max_num = nums[0]

for i in nums:
    if i > max_num:
        max_num = i
min_num = nums[0]
for j in nums:
    if j < min_num:
        min_num = j

print("Maximum number is:", max_num)
print("Minimum number is:", min_num)