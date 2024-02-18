class city:
    cityname="Satara"

    def __init__(self):
        print("In constructor")
        self.rtonum=11
        self.state="Maharashtra"

    def dispInfo(self):
        print(self.rtonum)
        print(self.state)
        print(self.cityname)

obj=city()
obj.dispInfo()
