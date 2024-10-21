"""count the value which is divisible by 3 and 5 between 1 to 100"""

count = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print(f"both 3 and 5 divisible in total {count} times")

