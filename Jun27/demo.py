def addTwo(num1,target1):
    for i in range(len(num1)):
        for j in range(i+1,len(num1)):
            if num1[i] + num1[j] == target1:
                return num1[i]+num1[j]
get_num = int(input("Enter a number: "))
num = []
for i in range(get_num):
    number = int(input("Enter a Digit: "))
    num.append(number)
get_target = int(input("Enter your target: "))
target = get_target
val = addTwo(num,target)
print(val,"is catch a targeted value ",target)