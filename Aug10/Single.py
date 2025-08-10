class Parent:
    def __init__(self):
        self.name = "Sailesh"

class Child(Parent):
    def __init__(self):
        super().__init__()

    def display(self):
        print("Name:",self.name)
    
obj1 = Child()
obj1.display()
