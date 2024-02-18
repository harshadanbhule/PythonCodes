class Parent:
    def __init__(self):
        print("In Constructor")
        self.x=30
        self.y=40

    def DispParent(self):
        print(self.x)
        print(self.y)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("In Parent Constructor")
        self.x=10
        self.y=20
    
    def DispChild(self):
        print(self.x)
        print(self.y)

obj=Child()
obj.DispParent()
obj.DispChild()

#In Constructor
#In Parent Constructor
#10
#20
#10
#20
