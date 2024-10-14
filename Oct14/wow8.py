""" If the day is Saturday or Sunday, print "Weekend"; else print "Weekday"."""

enter_day = input("Enter your Day: ")

days = enter_day.lower()

if days == "saturday" or days == "sunday":
    print(f"day is {days} so it is a weekend")
else:
    print(f"day is {days} so it is a working day")