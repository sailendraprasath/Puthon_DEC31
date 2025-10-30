class Demo:
    def add(self,*args):
        digit = 0
        print("welcome")
        for val in args:
            digit += val
        return digit

obj = Demo()
sailesh = obj.add(10,50,36,15)
hema = obj.add(25,60,77)
vaishu = obj.add(33,45,12,75)

print(sailesh);print(hema);print(vaishu)