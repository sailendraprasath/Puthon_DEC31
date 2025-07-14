#  Find palindrome

words = input("Enter a word: ")
reverse_words = ""
a = len(words) - 1

for i in range(len(words)):
    reverse_words += words[a]
    a -= 1

if words == reverse_words:
    print("Palindrome")
else:
    print("Not a palindrome")
