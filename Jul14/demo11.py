#  Reverse a number

num = 153
reverser_num = 0

while num > 0:
    val = num % 10
    reverser_num = reverser_num * 10 + val
    num //= 10
print("Reversed number:", reverser_num)