a = 0
b = 1
num = int(input("Enter a number: "))
#  Example for n = 10: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34    
for i in range(num):
    print(a)
    c = a + b
    a = b
    b = c
