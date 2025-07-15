nums = [1, 2, 2, 3, 1, 4, 2]
num_count = {}

for num in nums:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1
for key in num_count:
    print("Number:", key, "Count:",num_count[key])