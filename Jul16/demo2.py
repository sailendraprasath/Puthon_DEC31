words = "Sailendra prasath will be getting Citizen at Finland"

split_words = words.split()
longest = ""

for word in split_words:
    if len(word) > len(longest):
        longest = word
print(longest)
