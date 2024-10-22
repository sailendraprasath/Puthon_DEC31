"""count the value which is divisible by 5 and 11 between 1 to 100"""

count = 0

for i in range(1,101):
    if i % 5 == 0 and i % 11 == 0:
        count += 1

print(f"both 5 and 11 divisible in total {count} times")