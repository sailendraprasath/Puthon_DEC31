num = 6
sum_num = 0

for i in range(1,num):
    if num % i == 0:
        sum_num += i

if num == sum_num:
    print("Perfect number")
else:
    print("Not a Perfect Number")