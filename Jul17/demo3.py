num = int(input("Enter a count: "))
words = input("Enter a String: ")
splited_words = list(words)

count = 0
final_result = []

while count < num:
    for i in splited_words:
        if count < num:
            final_result.append(i)
            count += 1
        else:
            break


print("Final Result:", ''.join(final_result))
