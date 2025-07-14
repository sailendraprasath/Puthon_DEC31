#  Count the Number of Vowels in a String

words = "Madurai"
vowels = "aeiouAEIOU"
count = 0

for i in words:
    if i in vowels:
        count += 1

print("Number of vowels:", count)