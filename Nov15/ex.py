n=4
c=1
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(0,i):
        print(c,end=" ")
        c+=1
    print()