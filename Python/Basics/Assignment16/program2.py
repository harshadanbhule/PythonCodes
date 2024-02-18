class Vehicle:

        brand="RoyalEnfield"
        model="Gt650"
        year=19
        speed=100
        print("Brand name is :", brand)
        print("Model name is :", model)
        print("Year name is :", year)
        print("Brand speed is :", speed)

    def acceleration(self):
        pass

    def brake(self):
        pass

    def honk(self):
        pass

class Child(Parent):

    
    
    def acceleration(self):
        print("accelearte")
    
    def brake(self):
        print("brake")
    
    def honk(self):
        print("honk")

obj=Child()
obj.acceleration()
obj.brake()
pobj.honk()

