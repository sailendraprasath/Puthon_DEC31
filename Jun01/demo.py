for i in range(10):
    if i < 5:
        for s in range(5-i):
            print(" ", end="")
        for j in range(i+1):
            print("*",end=" ")
        print()
    elif i >= 5:
        for s in range(i-4):
            print(" ", end="")
        for j in range(10-i):
            print("*",end=" ")
        print()