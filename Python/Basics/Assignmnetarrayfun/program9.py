class IPL:
    IPLname="TataIPL"

    def __init__(self):
        print("In constructor")
        self.teamname="MI"
        self.captain="Rohit Sharma"

    def dispInfo(self):
        print(self.IPLname)
        print(self.teamname)
        print(self.captain)

obj=IPL()
obj.dispInfo()
