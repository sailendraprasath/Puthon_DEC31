"""we have to do store in list and sum the value using for loop"""


Empty_list = []
count = 0
finalSL = []

for i in range(1,6):
    Empty_list.append(i)

print(Empty_list)


for j in Empty_list:
    count += j

finalSL.append(count)

print(finalSL)



