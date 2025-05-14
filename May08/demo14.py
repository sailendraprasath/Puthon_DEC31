print("\tTraffic signal meaning")
color = input("Enter a color: ")

if color == "red" or color == "RED":
    print("Stop")
elif color == "yellow" or color == "YELLOW":
    print("wait")
elif color == "green" or color == "GREEN":
    print("Go")
else:
    print("Invalid color")