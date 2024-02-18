class Icc:
    def iccInfo(self):
        print("In ICC")

class Bcci(Icc):
    def bcciInfo(self):
        print("In BCCI")

class Ipl(Bcci):
    def iplInfo(self):
        print("In IPL")

obj=Ipl()
obj.iccInfo()
obj.bcciInfo()
obj.iplInfo()

