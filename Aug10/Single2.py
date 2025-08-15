class Teacher:
    def __init__(self,name):
        self.name = name

class Student(Teacher):

    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print("Student Teacher Name is:",self.name)

obj = Student("Sailesh")
obj.display()
