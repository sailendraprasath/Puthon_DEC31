""" get input for number a and b """  
""" sample input is: a=8,b=15  output become: 9,10,11,12,13,14 """

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

for a in range(a+1,b):
    print(a)


