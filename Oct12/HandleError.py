"""
2. Handle errors when converting non-numeric strings to integers.
Question: What would you do if you tried converting a string containing non-numeric characters into an integer and it raised an error?
"""

user_input = input("Enter your value: ")


print(f"your values is: {user_input}")
try:
    num = int(user_input)
    print(f"converted num is: {num}")
except ValueError:
    print("Error:recheck your values")