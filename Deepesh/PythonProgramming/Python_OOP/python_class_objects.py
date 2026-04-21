"""
Class: class is blue print of an object where it contains method/attribute/variables.
Object: object is an entity that access all properties defined in the class.
Constuctor: Constructor that initialize, memory for the object is being created.
        ->  There is default constructor being called, whenever we create object of the class.
        ->  If we provide parameter to constructor, then it is called parametrize construtor.
method : when define any function inside the class then become method.


"""
# class
class Car:
    # class variable
    CompanyName = "TATA"

    # constructor
    def __init__(self, car_name, car_price, car_model):
        print("-----Welcome to Car Class-----")

        self.CarName = car_name # instance variable
        self.CarPrice = car_price # instance variable
        self.CarModel = car_model # instance variable

    # instance method
    def ShowCarName(self):
        print("Car Name:", self.CarName)

    # instance method
    def ShowCarPrice(self):
        print("Car Price :", self.CarPrice)

    # instance method
    def showCarModel(self):
        print("Car Model:", self.CarModel)

    
    def ShowCarDetails(self):
        # accessing method inside method in the class using self
        self.ShowCarName()
        self.ShowCarPrice()
        self.showCarModel()
        print("Compnay Name :", self.CompanyName)


    @classmethod
    def showCompanyName(cls):
        print("Company Name :", cls.CompanyName)


    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact*i

        return fact


    


# create object of the class
obj = Car("Harrier", "25 Lakh", 2026)
obj.ShowCarName()
print(obj.CompanyName)
obj.ShowCarDetails()
##Car.ShowCarDetails(obj)

# access class method and static method with help of class name.
Car.showCompanyName()
print(Car.get_factorial(5))
        




