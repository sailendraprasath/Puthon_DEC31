def get_fibonacci(num):
    a,b = 0,1
    for _ in range(num):
        print(a,end=" ")
        a = b
        b = a+b

num = int(input("Enter The number of terms: "))
get_fibonacci(num)