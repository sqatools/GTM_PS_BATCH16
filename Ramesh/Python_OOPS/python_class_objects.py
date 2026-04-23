"""
class : class is blue print of an object where it contains method/attribute/variables.
object : it is an entity that accesses the properties define in the class.
constructor : it that initialized, memory for the object being created.
        -> There is default constructor being called when ever we create object of the class.
        -> If we provide parameter to constructor, then it is called parametrize constructor.
method : when define any function inside the class then become method.


"""

class Car :
    def __init__(self, car_name, car_price, car_model):
        print("-----Welcome to car Class-----")



        self.CarName = car_name
        self.CarPrice = car_price
        self.CarModel = car_model
    
    def ShowCarName(self):
        print("Car Name:", self.CarName)
    
    def ShowCarPrice(self):
        print("Car Price:", self.CarPrice)
    
    def ShowCarModel(self):
        print("Car Model:", self.CarModel)


    def ShowCarDetails(self):
        self.CarName()
        self.CarPrice()
        self.CarModel()


obj = Car("Harrier", "23 lacs", 2026)
obj.ShowCarName()