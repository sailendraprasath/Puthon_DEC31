words = "a1b2c3"
letters = []
num = []
for i in range(len(words)):
    if i % 2 != 0:
        num.append(words[i])       
    else:
        letters.append(words[i])   
else:
    for i in range(len(num)):
        for j in range(int(num[i])):
            print(letters[i],end="")