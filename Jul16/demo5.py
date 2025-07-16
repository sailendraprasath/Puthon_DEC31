words = "Sailendra prasath"
list_words = words.split()
vowels = "aeiouAEIOU"

count_vowels = 0
count_consonent = 0

for i in list_words:
    for j in i:
        if j in vowels:
            count_vowels+=1
        else:
            count_consonent+=1

print("Consonent",count_consonent)
print("Vowels",count_vowels)
    