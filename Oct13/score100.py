"""get the score pass or fail"""

student_mark = int(input("Enter your Score out of 100 here: "))

if student_mark <= 35:
    print(f"your mark is {student_mark}: POOR STUDENT")
elif student_mark <= 70:
    print(f"Your mark is {student_mark}: AVERAGE")
else:
    print(f"Your mark is {student_mark}: GOOD")