
input_str = input("Enter the array elements separated by space: ") 
arr = list(map(int, input_str.split()))

n = int(input("Enter number of times to rotate: "))

for _ in range(n):
    last = arr.pop()
    arr.insert(0, last)

print("Rotated Array:", arr)
