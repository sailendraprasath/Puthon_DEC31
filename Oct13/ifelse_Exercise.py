"""get input for variable mark.if mark > 35 print pass .else print fail """

Student_Mark = int(input("Enter your mark: "))

if Student_Mark > 35:
    print(f"Yor mark is above 35 so u pass: {Student_Mark}")
else:
    print(f"your mark is below 35 so Fail: {Student_Mark}")