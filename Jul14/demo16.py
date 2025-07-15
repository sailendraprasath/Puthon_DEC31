nums = [4, 3, 2, 4, 1, 3, 2, 5]

nums2 = {}

for num in nums:
    if num in nums2:
        nums2[num] += 1
    else:
        nums2[num] = 1

elm = []
for key in nums2:
    if nums2[key] == 1:
        elm.append(key)
print("Unique elements:", elm)