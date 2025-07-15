#  Merge TWO lists and remove dublicates

a = [1, 2, 3, 4]  
b = [3, 4, 5, 6]

merged_list = a + b

new_merged_list = []

for num in merged_list:
    if num not in new_merged_list:
        new_merged_list.append(num)

print("Merged list without duplicates:", new_merged_list)