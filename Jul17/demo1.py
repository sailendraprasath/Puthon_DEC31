words = "Majulah Info Tech Systems"
split_words = words.split()
result = ""

while True:
    if words == None:
        break
    else:
        for i in split_words:
            result += i[:2]
        else:
            result += i[-2:]