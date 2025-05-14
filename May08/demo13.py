temp = int(input("Enter the temperature: "))

if temp > 35:
    print("Hot")
elif temp >= 20 and temp <= 35:
    print("Warm")
elif temp < 20 and temp >= 0:
    print("Cold")
else:
    print("Freezing")
