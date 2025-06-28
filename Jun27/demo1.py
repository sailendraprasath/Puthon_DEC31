a = "aabb"
b = "ab"
list1 = list(a)
list2 = list(b)

for i in list1:
    if i in list2:
        list2.remove(i)
        if len(list2) == 0:
            print("Anagram")
            break
else:
    print("Not an anagram")