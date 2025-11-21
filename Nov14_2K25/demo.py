class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

std = Student("Sailesh",1001)
print(f"Name: {std.name}, Roll No: {std.roll_no}")
