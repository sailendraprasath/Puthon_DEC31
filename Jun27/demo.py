num = [2,4,5,5]
target = 10

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] + num[j] == target:
            print("Found ",num[i], "and", num[j],"equals to",target)
            break
    else:
        continue