words = input("type here: ")

for i in range(0, len(words), 2):
    letter = words[i]
    count = int(words[i + 1])
    print(letter * count, end="")


# def reverse_words(s):
#     return " ".join(word[::-1] for word in s.split())

# words = input("Enter here: ")  # e.g., sailesh age
# print(reverse_words(words))    # hselias ega



