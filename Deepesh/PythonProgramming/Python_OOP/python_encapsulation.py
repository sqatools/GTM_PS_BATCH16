class Car:
    # class variable
    CompanyName = "TATA"

    # constructor
    def __init__(self, car_name, car_price, car_model):
        print("-----Welcome to Car Class-----")

        self.CarName = car_name # instance variable
        self._CarPrice = car_price # instance variable
        self.__CarModel = car_model # instance variable

    # instance method
    def ShowCarName(self):
        print("Car Name:", self.CarName)

    # instance method
    def _ShowCarPrice(self):
        print("Car Price :", self._CarPrice)

    # instance method
    def __showCarModel(self):
        print("Car Model:", self.__CarModel)


obj = Car("Defender", "1 Cr", "2026")
obj.ShowCarName() # public method
obj._ShowCarPrice() # protected method
obj._Car__showCarModel()  #Private method   

print(obj._Car__CarModel)
