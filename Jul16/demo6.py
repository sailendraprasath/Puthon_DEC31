words = "HellO"

final_result = ""

for word in words:
    if word.isupper():
        final_result += word.lower()
    else:
        final_result += word.upper()

print(final_result)