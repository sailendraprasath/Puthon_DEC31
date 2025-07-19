def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter sorted array: ").split()))
key = int(input("Enter value to search: "))

index = binary_search(arr, key)
if index != -1:
    print("✅ Found at index", index)
else:
    print("❌ Not found")
