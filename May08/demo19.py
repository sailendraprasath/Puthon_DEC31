num = int(input("Enter a number here: "))
a = 2
isPrime = True

if num <= 1:
    print("Is Not Prime")
else:   
    while a <= num-1:
        if num % a == 0:
            isPrime = False
            break
        a+=1
if isPrime:
    print("This is prime number") 
else:
    print("Is Not Prime number")
