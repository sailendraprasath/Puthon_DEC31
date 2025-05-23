# num = int(input("Enter a number: "))

def find_prime(val):
    a=2
    while a < val:
        if val % a == 0:
            print("Not a prime")
            break
        a += 1
    else:
        print("Prime")
b=1
while b <= 10:
    find_prime(b)
    b += 1