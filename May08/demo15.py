print("\tMeal suggestion")
time = int(input("Enter a Time: "))


if time >= 8 and time <= 10:
    print("BreakFast")
elif time >= 12 and time <= 14:
    print("lunch")
elif time >= 19 and time <= 21:
    print("Dinner")
else:
    print("No meal suggestion")
