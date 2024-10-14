""" If the user is an adult (age >= 18), print "Adult"; else print "Minor"."""

age = int(input("Enter your age here: "))

if age >= 18:
    print(f"your age is {age} so you are ADULT")
else:
    print(f" your age is {age} its below 18 so you are MINOR")