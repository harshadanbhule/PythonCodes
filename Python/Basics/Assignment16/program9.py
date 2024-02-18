class Company:
    def __init__(self,name,employeeNo,idNo):
        self.name=name
        self.employeeNo=employeeNo
        self.idNo=idNo
    @staticmethod
    def instMethod(self):
        print("Namr is", self.name)
        print("employeeNo",self.employeeNo)
        print("id is",self.idNo)
    @classmethod
    def classMethod(cls):
        print("In class Method")

name=input("Enter Name:")
employeeNo=int(input("Enter employee no:"))
idNo=int(input("Enter id:"))
obj=Child(name)
obj.instMethod()
obj.classMethod()
        
