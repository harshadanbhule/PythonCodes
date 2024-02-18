class Parent:
    def property(self):
        print("Gold,car,bunglow")

    def career(self):
        print("Engg")

class Child(Parent):
    def career(self):
        print("Youtuber")

obj=Child()
obj.property()
obj.career()
