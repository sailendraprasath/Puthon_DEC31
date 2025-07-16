#  Remove duplicates print each word

word = "hello"
result_word = ""
for i in word:
    if i not in result_word:
        result_word += i

print(result_word)


print(''.join(set(word)))
