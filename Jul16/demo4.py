#  Reverse Each words

words = "Sailendra prasath"
list_words = words.split()
final_result = []

for letter in list_words:
    reverse_one_word = ""
    letter_count = len(letter) - 1

    for i in range(len(letter)):
        reverse_one_word += letter[letter_count]
        letter_count -= 1
    final_result.append(reverse_one_word)

print(final_result)


words = "Sailendra prasath"
reversed_words = [word[::-1] for word in words.split()]
print(" ".join(reversed_words))