num = int(input("Enter a number: "))
def sum_of_series(val):
    count = 0
    while val >0:
        count += val
        val-=1
    print(count)
sum_of_series(num)