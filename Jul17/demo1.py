words = input("Enter a words: ")
split_words = words.split()
current_list = split_words.copy()
output_lines = []
# "Majulah Info Tech Systems"
while any(current_list): 
    collected = ""
    new_list = []

    for index, word in enumerate(current_list):
        if not word:
            new_list.append("")
            continue
        if index % 2 == 0:
            part = word[:2]
            new_word = word[2:]
        else:
            part = word[-2:]
            new_word = word[:-2]

        collected += part
        new_list.append(new_word)

    output_lines.append(collected)
    current_list = new_list

print(output_lines)
for line in output_lines:
    print(line)
