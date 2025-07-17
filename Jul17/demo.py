def long_subset(arr):
    result = []
    unique_val = set(arr)

    for num in unique_val:
        subset = []

        for x in arr:
            if x == num or x == num+2:
                subset.append(x)
        if len(subset) > len(result):
            result = subset
    return result 
arr = [2, 2, 4, 4, 5, 5, 7, 5, 7]
print(long_subset(arr))