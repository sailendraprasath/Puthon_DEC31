num = 3
row = 1

while row <= num:
    space = num - row
    star = 1

    while space > 0:
        print(" ",end="")
        space -= 1

    while star <= row:
        print("*",end=" ")
        star += 1
    print()
    row += 1