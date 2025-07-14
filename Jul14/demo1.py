#Reverse a String 

words = "Madurai"
revers_words = "" 
a = len(words) - 1

for i in range(len(words)):
    revers_words += words[a]
    a-=1
print(revers_words)