""" the user has a ticket, print "Entry Allowed"; else print "No Entry"."""

ticket = input("Enter you yes or no: ")

entry = ticket.lower()

if entry == "yes":
    print(f"{entry} you have to go")
else:
    print(f"{entry} you must have take ticket so now you dont go")