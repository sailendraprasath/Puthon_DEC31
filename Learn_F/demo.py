class Emp:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        return self.name, self.salary

emp1 = Emp("Sailesh","45,000")
emp2 = Emp("MrTetPie","1 Crore per month")

print(emp1.display())
print(emp2.display())