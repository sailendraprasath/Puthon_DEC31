# words = "a1b2c3d2"

# for i in range(0, len(words),2):
#     letter = words[i]
#     count = int(words[i + 1])
#     print(letter*count,end="")

words = input()
b = {}
for i in words:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
for i,j in b.items():
    print("words",i,"Count",j)
