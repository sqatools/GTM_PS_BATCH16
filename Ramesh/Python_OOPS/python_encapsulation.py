class Car :
    # its called class variable
    companyName = "TATA"


    def __init__(self, car_name, car_price, car_model):
        print("-----Welcome to car Class-----")



        self.CarName = car_name
        self._CarPrice = car_price
        self.__CarModel = car_model
    
    def ShowCarName(self):
        print("Car Name:", self.CarName)
    
    def _ShowCarPrice(self):
        print("Car Price:", self._CarPrice)
    
    def __ShowCarModel(self):
        print("Car Model:", self.__CarModel)


obj = Car("Defemder", "1 Cr", "2026")
obj.ShowCarName() # public method
obj._ShowCarPrice() # protected method
obj._Car__ShowCarModel() # private method