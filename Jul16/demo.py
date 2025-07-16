words = "aaabbc"
store = {}
for i in words:
    if i in store:
        store[i] += 1
    else:
        store[i] = 1
for letter,count in store.items():
    print("letters",letter,"count",count)
print(store.items())