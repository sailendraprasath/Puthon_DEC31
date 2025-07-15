words = "a1b2c3d2"

for i in range(0, len(words),2):
    letter = words[i]
    count = int(words[i + 1])
    print(letter*count,end="")