class Parent:
    def __init__(self,name):
        self.name=name

    def instMethod(self):
        print("Namr is", self.name)
    @classmethod
    def classMethod(cls):
        print("In class Method")

class Child(Parent):
    pass

name=input("Enter Name:")
obj=Child(name)
obj.instMethod()
obj.classMethod()
