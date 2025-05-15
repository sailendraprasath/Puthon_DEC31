num = int(input("Enter a number: "))
a=2
prime_num = True

while a < num:
    if num % a == 0:
        prime_num = False
        break
    a += 1

if prime_num:
    print("is prime number")
else:
    print("is not prime number")
    