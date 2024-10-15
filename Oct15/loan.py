"""get tha data name age salary for loan purpose"""
name = input("Enter your Name: ")
salary = int(input("Enter your Salary here: "))
age = int(input("Enter your Age: "))

if salary >= 20000 or age <= 25:
    print("your are Eligble this process be continue")
    amt = int(input("Enter your loan amount: "))
    if amt > 50000 or amt < 0:
        print(f"Maximum loan amoount is 50000")
    else:
        print(f"dear {name} your salary is {salary} and age is {age}")
        print(f"your required {amt} Amount is eligble for loan")
        print(f"transaction will soo get your amount on monday")
else:
    print("your are not eligble for this process ")