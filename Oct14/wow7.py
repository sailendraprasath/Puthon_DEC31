"""Question: If the score is 50 or above, print "Pass"; else print "Fail"."""

score = int(input("Enter your score here out of 100: "))

if score >= 50:
    print(f"your score is {score} so you PASS")
else:
    print(f"your score is {score} so you FAIL")
    