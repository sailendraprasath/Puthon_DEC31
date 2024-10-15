""" check the score percentage and eligble or not """

name = input("Enter your Name: ")
dept = input("Enter your Department here: ")
locate = input("Enter your Location: ")


try:
    score = int(input("Enter your Score percentage here: "))

    if score < 0 or score > 100:
        print("Enter a num between (0) - (100)")
    elif score >= 70:
        print(f"Your name is {name}")
        print(f"Your Department is {dept.upper()}")
        print(f"Your location is {locate}")
        print(f"Your score is {score}% so you are eligible")
    else:
        print(f"Your Score is {score} so not eligble")
except ValueError:
    print("ERROR: Check the num values")
