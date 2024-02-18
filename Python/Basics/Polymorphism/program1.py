#Duck typing philosophy

class Demo:
    def fun(self):
        print("In fun")

class Memo:
    def gun(self):
        print("In gun")

def callfun(obj):

    if (id(obj)==id(obj1)):
        obj.fun()

    elif(id(obj)==id(obj2)):
        obj.gun()

obj1=Demo()
obj2=Memo()
callfun(obj1)
callfun(obj2)
        

