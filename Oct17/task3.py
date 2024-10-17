"""
Grade Calculation:
Write a program that takes a score from the user and prints the grade using the following conditions:

A: 90 and above
B: 80-89
C: 70-79
D: 60-69
F: Below 60
"""

std = int(input("Enter your Score out of 100: "))

if std >= 90:
    print("Grade - A")
elif std >= 80:
    print("Grade - B")
elif std >= 70:
    print("Grade - C")
elif std >= 60:
    print("Grade - D")
else:
    print("Fail")