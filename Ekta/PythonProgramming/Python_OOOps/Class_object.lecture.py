#class name 
class Car:
    #Constructor 
    def __init__(self,car_name,car_price,car_model):
        print("Constructor called automatically")
        self.CarName=car_name
        self.CarPrice=car_price
        self.CarModel=car_model
    #instance method
    def ShowCarName(self):
        print("Car name is ",self.CarName)
    #instance method
    def ShowCarPrice(self):
        print("Car price is ",self.CarPrice)  
    #instance method
    def ShowCarModel(self):
        print("Car model is ",self.CarModel)  
    #Accessed methods inside method 
    def ShowCarDetails(self):
        print("Car name is ",self.ShowCarName())
        print("Car price is ",self.ShowCarPrice())  
        print("Car model is ",self.ShowCarModel())

obj=Car("BMW",1000000,"X5")   #created object of the class and passed arguments to the constructor
obj.ShowCarName()   
obj.ShowCarPrice()
obj.ShowCarModel()
    