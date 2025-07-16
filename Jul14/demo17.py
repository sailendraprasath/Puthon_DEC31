# Anagram

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not anagrams")
else:
    num1 = {}
    num2 = {}

    for num in s1:
        if num in num1:
            num1[num] += 1
        else:
            num1[num] = 1
    
    for num in s2:
        if num in num2:
            num2[num] += 1
        else:
            num2[num] = 1
    if num1 == num2:
        print("Anagrams")
    else:
        print("Not anagrams")

