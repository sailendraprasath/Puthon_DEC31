"""
1. Convert a string input to a float and round it to 2 decimal places.
Question: How would you handle a situation where you need to convert a user input from a string to a float, and then round it to 2 decimal places?
"""
# get the values from thw user 
user_input = input("Enter your num: ")
# here i do given user_input value convert in float 
convert = float(user_input)
# do here convert value after . get 2 num
result = round(convert,2)

print(result)

# output
# Enter your num: 1234.6565
# 1234.66
