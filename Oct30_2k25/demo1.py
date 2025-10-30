class A:
    def demo(self):
        print("This is demo method from class A")
class B(A):
    def demo(self):
        print("This is demo method from class B")
obj = B()
res = obj.demo()
