num = 153
store = 0
val = 0
num2 = num
while num2 > 0:
    store = num2 % 10
    val += store ** 3
    num2 //= 10

print(val)
print(num)
if val == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

